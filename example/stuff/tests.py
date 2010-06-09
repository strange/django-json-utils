import datetime

from django.test.client import Client
from django.core.urlresolvers import reverse

from json_utils import utils

from example.stuff.models import Thing

tests = """
>>> utils.to_python(utils.to_json(Thing())).keys()
[u'pk', u'model', u'fields']

>>> utils.to_python(utils.to_json(Thing.objects.create())).keys()
[u'pk', u'model', u'fields']

>>> len(utils.to_python(utils.to_json(Thing.objects.all())))
1

>>> data = { 'test': (1, 2), 'instance': Thing(), 'date': datetime.datetime.now() }
>>> utils.to_python(utils.to_json(data)).keys()
[u'test', u'instance', u'date']

# Test responses

>>> c = Client()

>>> r = get(c, 'view1', is_ajax=False)
>>> r.status_code
400

>>> r = get(c, 'view1')
>>> r.status_code
200
>>> response = utils.to_python(r.content)
>>> response.keys()
['date', 'id']
>>> d = datetime.datetime.strptime(response['date'], '%Y-%m-%d %H:%M:%S')
>>> isinstance(d, datetime.datetime)
True

>>> r = get(c, 'view2')
>>> r.status_code
200
>>> response = utils.to_python(r.content)
>>> response.keys()
['pk', 'model', 'fields']

"""

def get(client, view_name, kwargs={}, is_ajax=True):
    url = reverse(view_name, kwargs=kwargs)
    kwargs = {}
    if is_ajax:
        kwargs['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
    return client.get(url, **kwargs)

def post(client, view_name, data, kwargs={}):
    url = reverse(view_name, kwargs=kwargs)
    return client.post(url, data)

__test__ = { 'doctest': tests }
