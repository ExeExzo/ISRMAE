import django_filters
from django_filters import CharFilter

from .models import *

class MainFilter(django_filters.FilterSet):
    marka_avto = CharFilter(field_name='marka_avto', lookup_expr='icontains', label='Марка АТ')
    voenni_reg_nomer = CharFilter(field_name='voenni_reg_nomer', lookup_expr='icontains', label='Военный номерной знак')
    field_shassi = CharFilter(field_name='field_shassi', lookup_expr='icontains', label='№  Шасси')
    field_dvigatelia = CharFilter(field_name='field_dvigatelia', lookup_expr='icontains', label='№ Двигателя')
    gorod = CharFilter(field_name='gorod', lookup_expr='icontains', label='Город')
    class Meta:
        model = Main
        fields = {
            'marka_avto',
            'voenni_reg_nomer',
            'field_shassi',
            'field_dvigatelia',
            'gorod',
        }

class VvtFilter(django_filters.FilterSet):
    marka_vvt = CharFilter(field_name='marka_vvt', lookup_expr='icontains', label='Марка АТ')
    nomer_znak = CharFilter(field_name='nomer_znak', lookup_expr='icontains', label='Номерной знак')
    voiskovaia_chast = CharFilter(field_name='voiskovaia_chast', lookup_expr='icontains', label='Войсковая часть')
    gorod = CharFilter(field_name='gorod', lookup_expr='icontains', label='Город')
    class Meta:
        model = Vvt
        fields = {
            'marka_vvt',
            'nomer_znak',
            'voiskovaia_chast',
            'gorod',
        }
