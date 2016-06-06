import unittest
import json

from dbmclient.models.insertion_order import InsertionOrder
from tests.base import Base


class InsertionOrderTest(Base):

    def testGetByAdvertiser(self):
        loader = InsertionOrder(InsertionOrderTest.conn)
        insertionOrders = loader.find_by_advertiser(4617)

        for insertionOrder in insertionOrders:
            print insertionOrder['id']
            assert insertionOrder['id'] is not None
        
