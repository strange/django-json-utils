from django.db import models

import datetime

from django.db import models

class Thing(models.Model):
    char = models.CharField(max_length=100, default='char')
    decimal = models.DecimalField(max_digits=3, decimal_places=2,
                                  default='1.0')
    date = models.DateField(default=datetime.datetime.now)
    date_time = models.DateTimeField(default=datetime.datetime.now)
    email = models.EmailField(default='test@test.com')
