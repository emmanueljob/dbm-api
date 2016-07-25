import unittest
import json

from dbmclient.conf.properties import Properties
from dbmclient.service.connection import Connection
from dbmclient.models.er.supported_exchange import SupportedExchange
from tests.base import Base


class SupportedExchangeTest(Base):

    def test_get_latest_file(self):
        loader = SupportedExchange(SupportedExchangeTest.conn)

        latest_file = loader._get_latest_file()
        assert latest_file != None

    def test_load_all(self):
        loader = SupportedExchange(SupportedExchangeTest.conn)
        data = loader.load_all()
        assert data[0]['id'] == 1
        


