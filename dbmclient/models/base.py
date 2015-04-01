import json
import requests


class Base(dict):

    connection = None

    def __init__(self, connection):
        Base.connection = connection
        super(Base, self).__init__()
