"""
What does this module do?  
Does it do things?

"""
import logging
from taxii_client import TaxiiClient

__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'


class EdgeClient(TaxiiClient):
    def __init__(self, config):
        super(EdgeClient, self).__init__(config)
        self.logger = logging.getLogger(__name__)
