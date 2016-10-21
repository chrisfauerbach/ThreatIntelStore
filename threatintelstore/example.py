"""
What does this module do?  
Does it do things?

"""


import logging
import transport
from transport.client_factory import TaxiiClientFactory
from config import Config
from transform import makestix
from persist import persiststix


__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'


class Client():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.stix_transformer = makestix.Transformer()
        self.stix_persist = persiststix.Persister(self.config)

    def go(self):

        taxii_client = TaxiiClientFactory.get_client(self.config)
        service = self.config.service
        feeds = service.feeds
        self.logger.error("Found feeds: %s", feeds)


        for coll in taxii_client.get_collections():
            self.logger.debug("Found collection: %s", coll)

        for feed in feeds:
            self.logger.error("Looking into feed: %s", feed)
            count = 0
            for block in taxii_client.get_stix_blocks(feed ):
                self.handle_stix_block( block )
                count += 1
                if count >20: return



    def handle_stix_block(self, block):
        #self.logger.error("Found stix block: %s", block)
        stix_object = self.stix_transformer.to_stix(block)
        for tp, top_level_object in self.stix_transformer.top_level_items(stix_object):
            try:
                self.logger.info("Stix Object Found: [%s] %s", tp, type(top_level_object))
                self.stix_persist.persist(tp, top_level_object)
            except:
                self.logger.exception("Error processing: %s", block)



