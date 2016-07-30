import sys
import falcon
from time import time
import logging as logger

logger.basicConfig(stream=sys.stdout, level=logger.DEBUG)


class RequestLogger(object):

    def process_request(self, req, resp):
        req.context['_starttime'] = time()

    def process_response(self, req, resp, resource):
        logger.info('%s %s %s %f ms', req.method, req.relative_uri,
                    resp.status, time() - req.context['_starttime'])
