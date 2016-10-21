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

    def to_stix(self,  block ):
        block_as_io = StringIO.StringIO(block)
        stix_package = None
        try:
            stix_package = STIXPackage.from_xml(block_as_io)
        except UnsupportedVersionError as ex:
            updated = ramrod.update(block_as_io)
            document = updated.document.as_stringio()
            stix_package = STIXPackage.from_xml(document)
        except ValueError:
            self.logger.exception("Value Error")
        except:
            self.logger.exception("Unknown issue while parsing Stix.")
            self.logger.error(block_as_io.getvalue())
        return stix_package
