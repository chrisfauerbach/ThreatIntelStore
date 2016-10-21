"""
What does this module do?  
Does it do things?

"""


import logging
import transport
from transport.client_factory import TaxiiClientFactory
from config import Config
from transform import makestix

__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'


class Client():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.stix_transformer = makestix.Transformer()

    def go(self):

        taxii_client = TaxiiClientFactory.get_client(self.config)
        service = self.config.service
        feeds = service.feeds
        self.logger.error("Found feeds: %s", feeds)


        for coll in taxii_client.get_collections():
            self.logger.debug("Found collection: %s", coll)

        for feed in feeds:
            self.logger.error("Looking into feed: %s", feed)
            for block in taxii_client.get_stix_blocks(feed ):
                self.handle_stix_block( block )



    def handle_stix_block(self, block):
        #self.logger.error("Found stix block: %s", block)
        stix_object = self.stix_transformer.to_stix(block)
        self.logger.info("Stix Object Found: %s", type(stix_object))

