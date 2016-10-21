"""
What does this module do?  
Does it do things?

"""
import cabby
import logging
import datetime
import pytz

__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'


class TaxiiClient(object):

    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.service = config.service
        self.name = self.service.name

    def _get_cabby_client(self):
        client = cabby.create_client(discovery_path=self.service.discovery_url)
        return client


    def get_client(self):
        client = self._get_cabby_client()
        return client

    def _get_collections(self):
        client = self.get_client()
        return client.get_collections()

    def get_collections(self):
        out_values = []
        for collection in self._get_collections():
            out_values.append(collection.name)
        return out_values


    def _get_stix_blocks(self, collection):
        self.logger.error("In _get_stix_blocks")
        client = self._get_cabby_client()
        self.logger.info("Incoming Start time: %s", self.config.start_time)
        self.logger.info("Incoming End time: %s", self.config.end_time)

        _real_start_time =  datetime.datetime.now() - datetime.timedelta(days=self.config.start_time)
        _real_end_time = datetime.datetime.now() - datetime.timedelta(days=self.config.end_time)
        if not _real_start_time.tzinfo:
            _real_start_time = pytz.utc.localize(_real_start_time)
        if not _real_end_time.tzinfo:
            _real_end_time = pytz.utc.localize(_real_end_time)

        #_real_start_time = parse( self.config.start_time)
        #_real_end_time = parse( self.config.end_time)
        self.logger.info("Start time: %s", _real_start_time)
        self.logger.info("End time: %s", _real_end_time)

        for block in client.poll(collection_name=collection, begin_date=_real_start_time, end_date=_real_end_time):
            yield block.content


    def get_stix_blocks(self, collection):
        self.logger.error("In get_stix_blocks: %s", collection)
        for block in self._get_stix_blocks( collection ):
            self.logger.debug("Found block here: %s", block)
            yield block


