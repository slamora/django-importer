"""
The `CsvModel` class is essentially shortcuts for automatically creating
serializers based on a given model class.
These tests deal with ensuring that we correctly map the model fields onto
an appropriate set of serializer fields for each case.
"""
import os
import tempfile

from django.db import models
from django.test import TestCase

from djimporter import fields, importers

from .models import ForeignKeySource, ForeignKeyTarget

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TESTDATA_DIR = os.path.join(BASE_DIR, 'data/')


class SlugFieldMapping(TestCase):
    def test_missing_slug_related(self):
        class ForeignKeySourceCsv(importers.CsvModel):
            target = fields.SlugRelatedField(
                queryset=ForeignKeyTarget.objects.all(), slug_field='name')

            class Meta:
                dbModel = ForeignKeySource
                fields = ('name', 'target')

        ForeignKeyTarget.objects.create(name='bar')

        csv_path = os.path.join(TESTDATA_DIR, 'ForeignKeySource.csv')
        importer = ForeignKeySourceCsv(csv_path)

        self.assertFalse(importer.is_valid())
