import json
import falcon
from bson import json_util


class JSON_Wrangler(object):

    def process_request(self, req, resp):
        if req.method in ['POST', 'PUT']:
            body = req.stream.read()

            try:
                req.context['body'] = json.loads(body)
            except:
                raise falcon.HTTPError(falcon.HTTP_400)

    def process_response(self, req, resp, resource):
        if 'result' in req.context:
            resp.body = json.dumps(req.context['result'],
                                   default=json_util.default)
