"""
What does this module do?  
Does it do things?

"""
from edge import EdgeClient
from taxii_client import  TaxiiClient

__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail..com'


class TaxiiClientFactory():
    EDGE = 'edge'
    EDGE = 'edge'

    @staticmethod
    def get_client(config):
        output = None
        if config.service.client_type == TaxiiClientFactory.EDGE:
            output =  EdgeClient(config)
        #elif config.client_type == TaxiiClientFactory.FLARE:
            #output = FlareClient(config)
        else:
            output = TaxiiClient(config)

        return output


