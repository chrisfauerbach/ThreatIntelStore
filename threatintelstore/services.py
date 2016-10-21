"""
Define standard classes to use throughout the application

"""
import json


__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'


class Service():
    def __init__(self, name=None, discovery_url=None, feeds = [],
                 username=None,password=None, client_type='edge'):
        self.name = name
        self.client_type = client_type
        self.discovery_url = discovery_url
        self.username = username
        self.password = password
        self.feeds = feeds

    def __str__(self):
        return json.dumps({"name":self.name
                           ,"discovery_url":self.discovery_url
                           ,"feeds":self.feeds
                              ,"username":self.username
                              ,"password":self.password
                              ,"client_type":self.client_type
                           })
