"""
What does this module do?  
Does it do things?

"""
import logging
import stix
import cybox
import json
import py2neo
from yaml import representer
import cybox
import cybox.objects
from cybox.objects import *
from stix.core import STIXPackage, STIXHeader
from cybox.common.object_properties import ObjectProperties
from py2neo import Node


__all__ = []
__version__ = '0.1'
__author__ = 'Chris Fauerbach'
__email__ = 'chrisfauerbach@gmail.com'


class Persister():
    def __init__(self, config):
        self.logger  = logging.getLogger(__name__)
        self.config = config

        neo4j_user = self.config.neo4j_username
        neo4j_password = self.config.neo4j_password
        neo4j_host = self.config.neo4j_host
        neo4j_port = self.config.neo4j_port

        graph_url = "http://{}:{}/db/data".format(neo4j_host, neo4j_port)
        self.logger.error("Graph URL: %s", graph_url)
        self.logger.error("Using username: %s", neo4j_user)
        self.logger.error("Using password: %s", neo4j_password)
        if neo4j_user and neo4j_password:
            neograph = py2neo.Graph(graph_url, user=neo4j_user, password=neo4j_password, bolt=False)
        else:
            neograph = py2neo.Graph(graph_url, bolt=False)


        self.graph = neograph

    def persist_dictionary (self,  label, representation ):
        if 'id' in representation:
            found_id = representation.get('id')
            found_object = Node(label, id=found_id)
            self.graph.merge(found_object)
            #found_object = self.graph.find_one(label, property_key=id, property_value=found_id)
            """:type : Node"""
            for x in representation:
                #found_object.add_label(label)
                found_object[x] = representation[x]
            found_object.push()
        else:
            self.logger.error("UNKNOWN Object with no id. \n%s", json.dumps(representation))



    def persist(self, type, target, parent=None, relationship=None):
        self.logger.error(type)

        if type=='STIXPackage':
            self.persistSTIXPackage(type, target)
        elif type=='Indicator':
            self.persistIndicator(type, target)
        elif type=='Observable':
            self.persistObservable(type, target)
        elif type == 'TTP':
            self.persistTTP(type, target)
        elif type == "ThreatActor":
            self.persistThreatActor(type, target)
        elif type == "Incident":
            self.persistIncident(type, target)
        elif type == "Campaign":
            self.persistCampaign(type, target)
        elif type == "ExploitTarget":
            self.persistExploitTarget(type, target)
        elif type == "RelatedPackage":
            self.persistRelatedPackage(type, target)


    def persistSTIXPackage(self, label, package):
        package = package
        """:type : STIXPackage"""

        header = package.stix_header
        """:type : STIXHeader"""

        representation = {}
        representation['id'] = package.id_
        representation['title'] = header.title
        representation['short_description'] = header.short_description
        representation['description'] = header.description
        stored_object = self.persist_dictionary( label, representation )


    def persistIndicator(self, label, indicator):
        indicator = indicator
        """:type : indicator"""

        representation = {}
        representation['id'] = indicator.id_
        representation['title'] = indicator.title
        representation['short_description'] = indicator.short_description
        representation['description'] = indicator.description

        stored_object = self.persist_dictionary( label, representation )

    def persistObservable(self, label, observable):
        observable = observable
        """:type : observable"""
        representation = {}
        observable.id_
        observable_object = observable.object_
        ob_properties = observable_object.properties
        """:type : ObjectProperties"""

        representation.update( ob_properties.to_dict() )

        stored_object = self.persist_dictionary( label, representation )


    def persistTTP(self, label, ttp):
        pass


    def persistThreatActor(self, label, threat_actor):
        pass


    def persistIncident(self, label, incident):
        pass

    def persistCampaign(self, label, campaign):
        pass

    def persistExploitTarget(self, label, exploit_target):
        pass

    def persistRelatedPackage(self, label, package):
        pass




