"""
What does this module do?
Does it do things?

"""
import StringIO
from stix.core import STIXPackage
from stix.utils.parser import UnsupportedVersionError
import logging
import ramrod

__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'

class Transformer():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def to_stix(self,  block: str ):...

    def top_level_items(self, stix_package: STIXPackage) -> object: ...
