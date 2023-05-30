from django.db import models
from django.urls import reverse
# Create your models here.


class VoiskovieChasti(models.Model):
    id_voiskovie_chasti = models.AutoField(primary_key=True,verbose_name="ID")
    name = models.CharField(db_column='Name', max_length=50,verbose_name="Название")  # Field name made lowercase.
    gorod = models.CharField(db_column='Gorod', max_length=50,verbose_name="Город")  # Field name made lowercase.
    rgk = models.CharField(db_column='RGK', max_length=100,verbose_name="РГК")  # Field name made lowercase.
    rod_voiska = models.CharField(db_column='Rod_voiska', max_length=50,verbose_name="Род войск")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voiskovie_chasti'
        verbose_name = 'Войсковые части'
        verbose_name_plural = 'Войсковые части'


class Vvt(models.Model):
    id_vvt = models.AutoField(primary_key=True,verbose_name="ID")
    marka_vvt = models.CharField(db_column='Marka_VVT', max_length=50,verbose_name="Марка АТ")  # Field name made lowercase.
    nomer_znak = models.CharField(max_length=50, blank=True, null=True, verbose_name="Номерной знак")
    god_vipuska = models.DateField(blank=True, null=True,verbose_name="Год выпуска")
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name="Цвет")
    field_shassi = models.CharField(db_column='№_shassi', max_length=50, blank=True, null=True, verbose_name="№ шасси")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.CharField(db_column='№_dvigatelia', max_length=50, blank=True, null=True,verbose_name="№ двигателя")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_seria_pasporta = models.CharField(db_column='№_seria_pasporta', max_length=50, blank=True, null=True, verbose_name = "№ серия паспорта")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_kuzova = models.CharField(db_column='№_kuzova', max_length=50, blank=True, null=True, verbose_name = "№ кузова")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_tech_talon = models.CharField(db_column='№_tech_talon', max_length=50, blank=True, null=True, verbose_name = "№ технического талона")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100,verbose_name="РГК")  # Field name made lowercase.
    gorod = models.CharField(max_length=50, blank=True, null=True,verbose_name="Город")
    gruppa_ekspluatacii = models.CharField(max_length=50, blank=True, null=True,verbose_name="группа эксплуатаций")
    vid = models.CharField(max_length=50, blank=True, null=True, verbose_name="Вид")
    category = models.CharField(max_length=50, blank=True, null=True,verbose_name="Категория")
    norma_rashoda = models.CharField(max_length=50, blank=True, null=True,verbose_name="Норма расхода")
    type_of_mark = models.CharField(max_length=50, blank=True, null=True,verbose_name="Тип марки")
    rod_voiska = models.CharField(max_length=50, blank=True, null=True,verbose_name="")
    voiskovaia_chast = models.CharField(max_length=50,verbose_name="Войсковая часть")
    podrazdelenia = models.CharField(max_length=50, blank=True, null=True,verbose_name="Подразделения")
    mileage = models.IntegerField(blank=True, null=True,verbose_name="Пробег .км")
    tp = models.IntegerField(db_column='TP', blank=True, null=True,verbose_name="ТР")  # Field name made lowercase.
    cp = models.IntegerField(db_column='CP', blank=True, null=True,verbose_name="СР")  # Field name made lowercase.
    kp = models.IntegerField(db_column='KP', blank=True, null=True,verbose_name="КР")  # Field name made lowercase.
    primechanie = models.CharField(db_column='Primechanie', max_length=50, blank=True, null=True,verbose_name="Примечание")  # Field name made lowercase.
    sostoianie = models.CharField(db_column='Sostoianie', max_length=255, blank=True, null=True,verbose_name="Состояние")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vvt'
        verbose_name = 'Обьекты ВВТ'
        verbose_name_plural = 'Обьекты ВВТ'
