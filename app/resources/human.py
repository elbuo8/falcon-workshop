import falcon
from mongoengine import ValidationError, DoesNotExist, NotUniqueError


class Human(object):
    def on_get(self, req, resp, ssn):
        try:
            human = req.context['models']['Human'].objects.get(ssn=ssn)
        except DoesNotExist:
            resp.status = falcon.HTTP_404
            return
        except Exception as e:
            # TODO Add logger
            resp.status = falcon.HTTP_500
            return
        req.context['result'] = {
            'human': human.to_json()
        }

    def on_delete(self, req, resp, ssn):
        try:
            req.context['models']['Human'].objects.get(ssn=ssn).delete()
        except DoesNotExist as error:
            resp.status = falcon.HTTP_201
            return
        except Exception as error:
            resp.status = falcon.HTTP_500
            return

        resp.status = falcon.HTTP_201


class Humans(object):
    def on_get(self, req, resp):
        page = req.get_param_as_int('page') or 1
        perPage = req.get_param_as_int('page') or 10
        offset = (page - 1) * perPage
        humas = []
        try:
            humans = list(req.context['models']['Human']
                          .objects.skip(offset).limit(perPage))
        except Exception as e:
            # TODO Add logging
            resp.status = falcon.HTTP_500
            return

        humans = map(lambda x: x.to_json(), humans)
        req.context['result'] = {
            'humans': humans
        }

    def on_post(self, req, resp):
        human = req.context['models']['Human'](**req.context['body'])

        try:
            human.save()
        except ValidationError as error:
            resp.status = falcon.HTTP_400
            req.context['result'] = {'error': error.to_dict()}
            return
        except NotUniqueError:
            resp.status = falcon.HTTP_400
            req.context['result'] = {'error': {'ssn': 'Value is not unique'}}
            return
        except Exception as e:
            # TODO: Add logging
            resp.status = falcon.HTTP_500
            return

        resp.status = falcon.HTTP_201
        req.context['result'] = {'human': human.to_json()}
