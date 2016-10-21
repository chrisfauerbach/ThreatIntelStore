#!/usr/bin/python
"""
Threat Intel Store - Main entry point

This is the main entry point to the threat intel store
It will read environment variables, config files, command line parameters
All kinds of goodies then it will dish out those parameters to
various functions within the package

"""

import argparse
import logging
import sys

import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from services import Service
from config import Config
import example



def get_yaml_config(file_name):
    with open(file_name, 'rb') as open_file:
        contents = yaml.load(open_file)
        LOGGER.debug(contents)
        return contents
    return None


def main_function():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_time", type=int, default=1, required=False,
                        help="Time range: start (number of days relative to today)")
    parser.add_argument("--end_time", type=int, default=0, required=False,
                        help="Time range: end: (number of days relative to today")
    parser.add_argument("--service", required=False, default="hailataxii.com",
                        help="Currently only accepting hailataxii.com")
    args = parser.parse_args()

    LOGGER.debug("Found start time: %s", args.start_time)
    LOGGER.debug("Found end time: %s", args.end_time)
    LOGGER.debug("Found service: %s", args.end_time)
    config = Config()

    loaded_configuration_file = get_yaml_config("config.yaml")

    for service in loaded_configuration_file.get('services', []):
        service_object = Service()
        service_object.name = service.get('name')
        if not service_object.name:
            raise Exception("Missing service client name.")


        if service.get('feeds'):
            LOGGER.debug("Found feeds: %s", service.get('feeds'))
            service_object.feeds = service.get('feeds',[])

        if service.get('username'):
            service_object.username = service.get('username')
        if service.get('password'):
            service_object.password = service.get('password')
        if service.get('client_type'):
            service_object.client_type = service.get('client_type')
        if service.get('discovery_url'):
            service_object.discovery_url = service.get('discovery_url', None)
        if not service_object.name:
            raise Exception("Missing service discovery url (discovery_url)")
        config.service_lookups[service_object.name] = service_object

    config.start_time = args.start_time
    config.end_time = args.end_time
    config.set_service(args.service)

    if not config.service:
        raise Exception("Unable to find service: {}".format(args.service))

    LOGGER.info("Looking at service:  %s", config.service)
    example_client = example.Client(config)
    example_client.go()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.DEBUG)

    try:


        main_function()
    except:
        LOGGER.exception("Unknown exception during execution.")
        sys.exit(-2)

    sys.exit(1)
