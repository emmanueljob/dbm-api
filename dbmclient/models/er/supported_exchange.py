import json
import re
import boto
import gcs_oauth2_boto_plugin
import collections


class SupportedExchange:

    GS_DBM_BUCKET = "gdbm-public"
    GS_DBM_BUCKET_PREFIX = "entity/"
    GS_DBM_RPT_RE = GS_DBM_BUCKET_PREFIX + r"(?P<yyyy>\d{4})(?P<mm>\d\d)(?P<dd>\d\d)\.0\.SupportedExchange\.json"

    def __init__(self, access_key=None, secret=None):
        self.access_key = access_key
        self.secret = secret

    def _get_latest_file(self):
        conn = boto.connect_gs(self.access_key, self.secret)
        bucket = conn.get_bucket(SupportedExchange.GS_DBM_BUCKET)
        data = {}
        for key in bucket.list(SupportedExchange.GS_DBM_BUCKET_PREFIX):
            # Only sync files matching the known pattern.
            match = re.match(SupportedExchange.GS_DBM_RPT_RE, key.name)
            if match:
                data[key.name] = key
        
        ordered = collections.OrderedDict(sorted(data.items()))
        latest_file = ordered.popitem()
        
        return latest_file[1]

    def load_all(self):
        latest_file = self._get_latest_file()
        data = latest_file.get_contents_as_string()
        try:
            json_data = json.loads(data)
        except Exception, e:
            print "Bad JSON Data",e
            return None

        return json_data
