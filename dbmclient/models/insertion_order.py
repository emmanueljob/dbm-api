import csv
import json
import base64

from apiclient import discovery
from oauth2client import client

from dbmclient.models.base import Base


class InsertionOrder(Base):

    def find_by_advertiser(self, advertiser_id):
        _API_VERSION = 'v1'
        auth = InsertionOrder.connection.get_authorization()
        service = discovery.build('doubleclickbidmanager', _API_VERSION, http=auth)

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
        for raw_lineitem in csv.reader(lineitems.split('\n')):
            if len(raw_lineitem) == 0:
                continue

            if first:
                first = False
                continue
            
            insertionOrder = InsertionOrder(InsertionOrder.connection)
            # TERRIBLE!!!!! BUT GOOGLE DOESNT SEND US AN ID.
            id = base64.b64encode(raw_lineitem[4])
            if id in ids:
                continue
            ids.append(id)
            insertionOrder['id'] = id
            insertionOrder['name'] = raw_lineitem[4]
            rval.append(insertionOrder)

        return rval
