from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import simplejson
from django.utils.encoding import force_unicode
from django.utils.functional import Promise

json_serializer = serializers.get_serializer("json")()
python_serializer = serializers.get_serializer("python")()

def to_json(subject, encode=True):
    if isinstance(subject, models.Model):
        subject = python_serializer.serialize([subject])[0]
    elif isinstance(subject, models.query.QuerySet):
        subject = python_serializer.serialize(subject)
    elif isinstance(subject, list):
        subject = map(lambda s: to_json(s, False), subject)
    elif isinstance(subject, dict):
        subject = dict([(k, to_json(v, False)) for k, v in subject.items()])

    # Handle lazy strings.
    if isinstance(subject, Promise):
        subject = force_unicode(subject)

    if not encode:
        return subject

    return simplejson.dumps(subject, ensure_ascii=False,
                            cls=DjangoJSONEncoder)

def to_python(subject):
    return simplejson.loads(subject)
