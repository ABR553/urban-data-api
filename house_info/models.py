from django.db import models
import csv
import re

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
    coordinates = models.CharField(max_length=256, null=True, blank=True)
    bondary_id = models.IntegerField()
    id_uda = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    listing_type = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(0, 'Tipo 0'), (1, 'Tipo 1')], default=None)
    date = models.DateTimeField()

    @classmethod
    def seed_data(self):
        with open('/code/assets.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in list(reader):
                if row['build_status']:
                    try:
                        construction_type = int(row['construction_type'])
                    except:
                        construction_type = None

                    HouseInfo.objects.create(
                        build_status=int(row['build_status']),
                        is_active=row['is_active'] == "True",
                        start_month=int(row['start_month']),
                        construction_type=construction_type,
                        date_diff=int(row['date_diff']),
                        description=row['description'],
                        date_in=row['date_in'],
                        property_type=int(row['property_type']),
                        end_week=int(row['end_week']),
                        typology_type=int(row['typology_type']),
                        id=int(re.sub(r"\D", "", row['id'])),
                        coordinates=row['coordinates'],
                        bondary_id=int(row['boundary_id']),
                        id_uda=row['id_uda'],
                        title=row['title'],
                        listing_type=int(row['listing_type']),
                        date=row['date']
                    )
