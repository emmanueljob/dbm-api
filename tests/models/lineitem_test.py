import unittest
import json

from dbmclient.models.lineitem import Lineitem
from tests.base import Base


class LineitemTest(Base):

    def testGetByAdvertiser(self):
        loader = Lineitem(LineitemTest.conn)
        lineitems = loader.find_by_advertiser(265531)

        for lineitem in lineitems:
            assert lineitem['id'] is not None
        
