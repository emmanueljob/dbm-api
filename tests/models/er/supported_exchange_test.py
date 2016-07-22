import unittest
import json

from dbmclient.conf.properties import Properties
from dbmclient.service.connection import Connection
from dbmclient.models.er.supported_exchange import SupportedExchange

import logging
logging.getLogger('boto').setLevel(logging.CRITICAL)


class SupportedExchangeTest(unittest.TestCase):

    

    def __init__(self, *args, **kwargs):

        props = Properties("test")
        self.access_key = props.access_key
        self.secret = props.secret
        self.bucket = props.bucket

        super(SupportedExchangeTest, self).__init__(*args, **kwargs)

    def test_get_latest_file(self):
        loader = SupportedExchange(self.access_key,
                                   self.secret)

        latest_file = loader._get_latest_file()
        assert latest_file != None

    def test_load_all(self):
        loader = SupportedExchange(self.access_key,
                                   self.secret)
        data = loader.load_all()
        print data
        


