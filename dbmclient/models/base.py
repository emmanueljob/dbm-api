import json
import requests


class Base(dict):

    connection = None

    def __init__(self, connection):
        Base.connection = connection
        super(Base, self).__init__()

    def encode_for_id(self, id):
        # TERRIBLE!!!!! BUT GOOGLE DOESNT SEND US AN ID.
        # remove '=' because it messes up urls. we never decode so its not a big deal.
        id = base64.b64encode(id).strip('=')

    def decode_id(self, id):
        # TERRIBLE!!!!! BUT GOOGLE DOESNT SEND US AN ID.
        # remove '=' because it messes up urls. we never decode so its not a big deal.
        
        missing_padding = 4 - len(id) % 4
        if missing_padding:
            id += b'='* missing_padding
        id = base64.b64encode(id).strip('=')
        return id
