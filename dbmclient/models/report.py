import csv
import json
import base64

from oauth2client import client

from dbmclient.models.base import Base


class Report(Base):

    def find_by_query(self, query_id):
        
        service = self.get_service()
        
        try:
            req = service.reports().listreports(queryId=query_id)
            resp = req.execute()

        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
                   "the application to re-authorize")

        if 'reports' not in resp:
            return []

        rval = []
        for report in resp['reports']:
            rval.append(self.get_object(report))

        return rval
