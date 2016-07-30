import falcon
from ..models.human import Human


class Models(object):

    def process_request(self, req, res):
        req.context['models'] = {'Human': Human}
