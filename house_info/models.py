from django.db import models

# Create your models here.
class HouseInfo(models.Model):
    build_status = models.IntegerField()
    is_active = models.BooleanField()
    start_month = models.IntegerField()
    construction_type = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(0, 'Tipo 0'), (1, 'Tipo 1'), (2, 'Tipo 2')], default=None)
    date_diff = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    date_in = models.DateTimeField()
    property_type = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(0, 'Propiedad 0'), (1, 'Propiedad 1'), (2, 'Propiedad 2'), (3, 'Propiedad 3'), (4, 'Propiedad 4')], default=None)
    end_week = models.IntegerField()
    typology_type = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(0, 'Tipologia 0'), (1, 'Tipologia 1'), (2, 'Tipologia 2'), (3, 'Tipologia 3'), (4, 'Tipologia 4'), (5, 'Tipologia 5'), (6, 'Tipologia 6')], default=None)
    id = models.IntegerField(unique=True, primary_key=True)
    lat = models.DecimalField(max_digits=50, decimal_places=50)
    lng = models.DecimalField(max_digits=50, decimal_places=50)
    bondary_id = models.IntegerField()
    id_uda = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    listing_type = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(0, 'Tipo 0'), (1, 'Tipo 1')], default=None)
    date = models.DateTimeField()
