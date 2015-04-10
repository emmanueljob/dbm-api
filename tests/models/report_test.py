import unittest
import json

from dbmclient.models.report import Report
from tests.base import Base


class ReportTest(Base):

    def testGetByQuery(self):
        loader = Report(ReportTest.conn)
        reports = loader.find_by_query(1428681298550)
        
        for report in reports:
            if report['metadata']['status']['state'] == "DONE":
                endTime = report['metadata']['status']['finishTimeMs']
                assert int(endTime) > 0
                
                # URL to download the report.
                assert report['metadata']['googleCloudStoragePath'] is not None
