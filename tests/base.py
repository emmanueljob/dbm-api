import unittest

from dbmclient.conf.properties import Properties
from dbmclient.service.connection import Connection


class Base(unittest.TestCase):

    conn = None

    def __init__(self, *args, **kwargs):

        props = Properties("test")

        self.p12 = props.p12
        Base.conn = Connection(p12=self.p12)

        super(Base, self).__init__(*args, **kwargs)
