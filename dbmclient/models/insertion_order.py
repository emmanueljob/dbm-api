import csv
import json

from oauth2client import client

from dbmclient.models.base import Base


class InsertionOrder(Base):

    def find_by_advertiser(self, advertiser_id):
        service = self.get_service()

        try:
            body = { 'filterType': 'ADVERTISER_ID', 'filterIds': [advertiser_id]}

            req = service.lineitems().downloadlineitems(body=body)
            resp = req.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")

        if 'lineItems' not in resp:
            return None
        
        lineitems = resp['lineItems']
        first = True
        rval = []
        ids = []
        for raw_lineitem in csv.reader(lineitems.encode('utf-8').split('\n')):
            if len(raw_lineitem) == 0:
                continue

            if first:
                first = False
                continue

            insertionOrder = InsertionOrder(InsertionOrder.connection)
            id = self.encode_for_id(raw_lineitem[4])
            if id in ids:
                continue
            ids.append(id)
            insertionOrder['id'] = id
            insertionOrder['name'] = raw_lineitem[4]
            insertionOrder['advertiser_name'] = raw_lineitem[3]
            insertionOrder['budget'] = raw_lineitem[11]
            insertionOrder['start_date'] = raw_lineitem[8]
            insertionOrder['end_date'] = raw_lineitem[9]
            rval.append(insertionOrder)

        return rval
