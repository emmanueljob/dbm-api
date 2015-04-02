import csv
import json
import base64

from apiclient import discovery
from oauth2client import client

from dbmclient.models.base import Base


class Lineitem(Base):

    def find_by_advertiser(self, advertiser_id):
        _API_VERSION = 'v1'
        auth = Lineitem.connection.get_authorization()
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
        for raw_lineitem in csv.reader(lineitems.split('\n').encode('utf-8')):
            if len(raw_lineitem) == 0:
                continue

            if first:
                first = False
                continue
            
            lineitem = Lineitem(Lineitem.connection)
            ids.append(id)
            lineitem['id'] = raw_lineitem[0]
            lineitem['name'] = raw_lineitem[5]
            lineitem['active'] = raw_lineitem[5]
            lineitem['budget'] = raw_lineitem[18]
            lineitem['start_date'] = raw_lineitem[15]
            lineitem['end_date'] = raw_lineitem[16]
            lineitem['status'] = raw_lineitem[7]
            lineitem['campaign_name'] = raw_lineitem[4]
            rval.append(lineitem)

        return rval
