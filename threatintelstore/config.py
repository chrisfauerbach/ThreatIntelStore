"""
Simple configuration class that can be passed around
Straight forward


"""

__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'

class Config():
    """General configuration for application"""

    def __init__(self):
       self.service_lookups = {}
       self.start_time = None
       self.end_time = None
       self.service = None
       self.neo4j_host = None
       self.neo4j_port = None
       self.neo4j_username = None
       self.neo4j_password = None

    def set_service(self, service_name):
        """

        :param service_name:
        :return: service
        """
        self.service = self.service_lookups.get(service_name)
        return self.service
