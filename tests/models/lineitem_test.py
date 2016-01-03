import unittest
import json

from dbmclient.models.lineitem import Lineitem
from tests.base import Base


class LineitemTest(Base):

    def testGetByAdvertiser(self):
        loader = Lineitem(LineitemTest.conn)
        # test
        # lineitems = loader.find_by_advertiser(601374)
        
        # bacardi
        lineitems = loader.find_by_advertiser(670557)

        for lineitem in lineitems:
            print lineitem.name
            assert lineitem['id'] is not None
            if lineitem.id == '4711054':
                print "UPDATING"
                lineitem.name = "Liz test"
                # lineitem.save()

        lineitem = lineitems[0]
        #update budget
        
