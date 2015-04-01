import unittest
import json

from dbmclient.models.advertiser import Advertiser
from tests.base import Base


class AdvertiserTest(Base):

    def testGet(self):
        loader = Advertiser(AdvertiserTest.conn)
        adv = loader.find(265531) # Apple

        assert adv['name'] == "Apple"
