import sys
import falcon
from wsgiref import simple_server
from mongoengine import connect

from app.resources.human import Human as HumanResource
from app.resources.human import Humans as HumansResource
from app.middlewares.json_wrangler import JSON_Wrangler
from app.middlewares.models import Models

connect('falcon-workshop')

api = falcon.API(middleware=[
    JSON_Wrangler(),
    Models()
])

api.add_route('/humans/{ssn}', HumanResource())
api.add_route('/humans', HumansResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, api)
    httpd.serve_forever()
