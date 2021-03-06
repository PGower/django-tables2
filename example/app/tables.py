# coding: utf-8
import django_tables2 as tables
from .models import Country


class CountryTable(tables.Table):
    name = tables.Column()
    population = tables.Column()
    tz = tables.Column(verbose_name='time zone')
    visits = tables.Column()
    summary = tables.Column(order_by=("name", "population"))

    class Meta:
        model = Country


class ThemedCountryTable(CountryTable):
    class Meta:
        attrs = {'class': 'paleblue'}
