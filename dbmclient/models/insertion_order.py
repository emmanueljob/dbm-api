import csv
import json

from oauth2client import client

from dbmclient.models.base import Base


class InsertionOrder(Base):

    def find_by_advertiser(self, advertiser_id):
        service = self.get_service()

        try:
            request_body = {
                'filterType': 'ADVERTISER_ID',
                'filterIds': [advertiser_id],
                'fileTypes': ['INSERTION_ORDER']
            }
            request = service.sdf().download(body=request_body)
            response = request.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")

        if 'insertionOrders' not in response:
            return None

        ios = response['insertionOrders']
        first = True
        rval = []
        ids = []
        for raw_io in csv.reader(ios.encode('utf-8').split('\n'), quoting=csv.QUOTE_NONNUMERIC):
            if len(raw_io) == 0:
                continue

            if first:
                first = False
                continue

            insertionOrder = InsertionOrder(InsertionOrder.connection)
            id = self.encode_for_id(raw_io[0])
            if id in ids:
                continue

            ids.append(id)
            insertionOrder['id'] = id
            insertionOrder['name'] = raw_io[1]
            insertionOrder['advertiser_name'] = ''

            budget_segments = raw_io[20]
            budget_segments = budget_segments.replace('(', '')
            budget_segments = budget_segments.split(');')

            budget = 0.0
            for budget_segment in budget_segments:
                segment = budget_segment.split(';')
                #budget += int(segment[0].lstrip())
                value = segment[0].strip('" ')
                budget += float(value)

            insertionOrder['budget'] = int(budget)

            start_date = budget_segments[0].split(';')
            insertionOrder['start_date'] = start_date[1].lstrip()
            
            end_date = budget_segments[(len(budget_segments) - 1)].split(';')
            insertionOrder['end_date'] = start_date[2].lstrip()
            rval.append(insertionOrder)

        return rval

    def find_by_advertiser_old(self, advertiser_id):
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
