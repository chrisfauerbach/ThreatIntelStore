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

    def top_level_items(self, stix_package):
        """
        Stix package can either be a package/report of meaning, or it can just hold things
          like indicators, observables, etc

        :param stix_package: stix.core.stix_package.STIXPackage
        :return:
        """
         
        stix_header = stix_package.stix_header
        """:type : STIXHeader"""
        if stix_header.title or stix_header.description or stix_header.short_description:
            """We have a stix package!"""
            yield  ("STIXHeader", stix_package, )

        for indicator in stix_package.indicators or []:
            yield  ("Indicator", indicator, )

        for observable in stix_package.observables or []:
            yield  ("Observable", observable, )

        for ttp in stix_package.ttps or []:
            yield ("TTP", ttp, )

        for incident in stix_package.incidents      or []:
            yield ("Incident", incident,)

        for campaign in stix_package.campaigns or []:
            yield ("Campaign", campaign, )

        for course_of_action in stix_package.courses_of_action or []:
            yield ("CourseOfAction", course_of_action, )

        for exploit_target in stix_package.exploit_targets or []:
            yield ("ExploitTarget", exploit_target, )

        for related_package in stix_package.related_packages or []:
            yield ("RelatedPackage", related_package, )

        for threat_actor in stix_package.threat_actors or []:
            yield ("ThreatActor", threat_actor, )





