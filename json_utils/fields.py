from django.db import models

from json_utils import utils

class JSONField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        """Convert loaded JSON string to a python object."""
        if isinstance(value, basestring):
            return utils.to_python(value)
        return value

    def get_db_prep_save(self, value):
        """Convert python object to a JSON string before saving."""
        value = utils.to_json(value)
        return super(JSONField, self).get_db_prep_save(value)
