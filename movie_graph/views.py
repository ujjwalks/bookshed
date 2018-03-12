import json

import falcon


class Index(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({u'message': u'Hello world!'})
