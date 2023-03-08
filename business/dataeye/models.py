from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(TimeStampMixin):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
