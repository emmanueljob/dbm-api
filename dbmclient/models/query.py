import csv
import sys
csv.field_size_limit(sys.maxsize)
import json
import base64

from oauth2client import client

from dbmclient.models.base import Base


class Query(Base):

    def find_all(self):
        service = self.get_service()

        try:
            req = service.queries().listqueries()
            resp = req.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")

        if 'queries' not in resp:
            return []
        
        rval = []
        for query in resp['queries']:
            rval.append(self.get_object(query))

        return rval

    def find(self, query_id):
        service = self.get_service()

        try:
            req = service.queries().getquery(queryId=query_id)
            resp = req.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")

        
        return self.get_object(resp)

    def create(self, query):
        service = self.get_service()

        try:
            req = service.queries().createquery(body=json.loads(query))
            resp = req.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")
            return False

        return self.get_object(resp)

    def run(self, query_id, body):
        service = self.get_service()

        try:
            req = service.queries().runquery(queryId=query_id, body=body)
            resp = req.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")
            return False
        
        return True
        
