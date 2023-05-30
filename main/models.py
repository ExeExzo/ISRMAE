from distutils.command.upload import upload
from email.policy import default
from pickle import NONE
from django.db import models
from django.urls import reverse

from datetime import datetime
from datetime import timedelta

from django.utils.safestring import mark_safe
# Create your models here.

class Akb(models.Model):
    akb_id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(db_column='Name', max_length=50, verbose_name="Наименование")  # Field name made lowercase.
    obiekti_vvt = models.CharField(db_column='Obiekti_vvt', max_length=255,verbose_name="Обьекты ВВТ")  # Field name made lowercase.
    kem_vidano = models.CharField(db_column='Kem_vidano', max_length=50, blank=True, null=True,verbose_name="Кем выдано")  # Field name made lowercase.
    kogda_vidano = models.DateField(db_column='Kogda_vidano', blank=True, null=True, verbose_name="Когда выдано")  # Field name made lowercase.
    spisanie = models.CharField(db_column='Spisanie', max_length=50, blank=True, null=True, verbose_name="Списание")  # Field name made lowercase.
     
    class Meta:
        managed = False
        db_table = 'akb'
        verbose_name = 'АКБ'
        verbose_name_plural = 'АКБ'

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id':self.pk})


# class AkbNew(models.Model):
#     akb_id = models.AutoField(primary_key=True,verbose_name='id АКБ')
#     type_akb = models.CharField(max_length=50,verbose_name='Тип шины')
#     kolichestvo_akb = models.IntegerField(verbose_name='Количество АКБ')
#     field_p_p = models.ForeignKey('Main', models.DO_NOTHING, db_column='№_p/p',verbose_name='Тип шины')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     kev_vidano = models.CharField(max_length=50,verbose_name='Кем выдано')
#     field_nariad_kogda_vidano = models.CharField(db_column='№_nariad_kogda_vidano', max_length=50,verbose_name='№ наряда и когда выдано')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     srok_sluzhbi = models.IntegerField(verbose_name='Срок службы')
#     data_ustanovki_akb = models.DateField(verbose_name='Дата установки АКБ')
#     data_spisania_akb_po_godam = models.DateField(blank=True, null=True,verbose_name='Дата списания АКБ по годам')
#     srok_sluzhbi_v_km_do_spisania = models.IntegerField(verbose_name='Списание АКБ по км.')
#     january = models.IntegerField(db_column='January', blank=True, null=True,verbose_name='Январь')  # Field name made lowercase.
#     february = models.IntegerField(db_column='February', blank=True, null=True,verbose_name='Февраль')  # Field name made lowercase.
#     march = models.IntegerField(db_column='March', blank=True, null=True,verbose_name='Март')  # Field name made lowercase.
#     april = models.IntegerField(db_column='April', blank=True, null=True,verbose_name='Апрель')  # Field name made lowercase.
#     may = models.IntegerField(db_column='May', blank=True, null=True,verbose_name='Май')  # Field name made lowercase.
#     june = models.IntegerField(db_column='June', blank=True, null=True,verbose_name='Июль')  # Field name made lowercase.
#     july = models.IntegerField(db_column='July', blank=True, null=True,verbose_name='Июнь')  # Field name made lowercase.
#     august = models.IntegerField(db_column='August', blank=True, null=True,verbose_name='Август')  # Field name made lowercase.
#     september = models.IntegerField(db_column='September', blank=True, null=True,verbose_name='Сентябрь')  # Field name made lowercase.
#     october = models.IntegerField(db_column='October', blank=True, null=True,verbose_name='Октябрь')  # Field name made lowercase.
#     november = models.IntegerField(db_column='November', blank=True, null=True,verbose_name='Ноябрь')  # Field name made lowercase.
#     december = models.IntegerField(db_column='December', blank=True, null=True,verbose_name='Декабрь')  # Field name made lowercase.
#     proideno_km_from_beginning = models.IntegerField(blank=True, null=True,verbose_name=' Пройдено км с момента установки АКБ')
#     ostalos_km_do_spisania = models.IntegerField(blank=True, null=True,verbose_name='Осталось км. до списания')

#     class Meta:
#         managed = False
#         db_table = 'akb_new'
#         verbose_name = 'АКБ новый'
#         verbose_name_plural = 'АКБ новый'

#     def save(self, *args, **kwargs):
#         if self.january != NONE or self.february != NONE or self.march != NONE or self.april != NONE or self.may != NONE or self.june != NONE or self.july != NONE or self.august != NONE or self.september != NONE or self.october != NONE or self.november != NONE or self.december != NONE :
#             self.proideno_km_from_beginning = self.january + self.february + self.march + self.april + self.may + self.june + self.july + self.august + self.september + self.october + self.november + self.december 
#         if  self.srok_sluzhbi_v_km_do_spisania != None:
#             self.ostalos_km_do_spisania = self.srok_sluzhbi_v_km_do_spisania - (self.january + self.february + self.march + self.april + self.may + self.june + self.july + self.august + self.september + self.october + self.november + self.december)
#         if  self.data_ustanovki_akb != None:
#             self.data_spisania_akb_po_godam = (self.data_ustanovki_akb  + timedelta(days=1095) ).strftime('%Y-%m-%d')
#         super(AkbNew, self).save(*args, **kwargs)

class Avtoshini(models.Model):
    avtoshin_id = models.AutoField(primary_key=True,verbose_name="ID")
    name = models.CharField(db_column='Name', max_length=50,verbose_name="Наименование")  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True,verbose_name="Тип")  # Field name made lowercase.
    obiekti_vvt = models.CharField(db_column='Obiekti_vvt', max_length=255,verbose_name="Обьекты ВВТ")  # Field name made lowercase.
    kem_vidano = models.CharField(db_column='Kem_vidano', max_length=50, blank=True, null=True,verbose_name="Кем выдано")  # Field name made lowercase.
    kogda_vidano = models.DateField(blank=True, null=True,verbose_name="Когда выдано")
    spisanie = models.CharField(db_column='Spisanie', max_length=50, blank=True, null=True,verbose_name="Списание")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'avtoshini'
        verbose_name = 'Автошины'
        verbose_name_plural = 'Автошины'


class AvtoshiniNew(models.Model):
    id_shin = models.AutoField(primary_key=True,verbose_name='id шин')
    type_shin = models.CharField(max_length=50,verbose_name='Тип шины')
    id_techniki = models.ForeignKey('Main', models.DO_NOTHING, db_column='id_techniki',verbose_name='ID техники')
    razmer_shin = models.CharField(max_length=50,verbose_name='Размер шин')
    kolichestvo_shin = models.IntegerField(verbose_name='Количество шин')
    kem_vidano = models.CharField(max_length=50, blank=True, null=True,verbose_name='Кем выдано')
    field_nariad_kogda_vidano = models.CharField(db_column='№_nariad_kogda_vidano', max_length=50, blank=True, null=True,verbose_name='№ наряда и когда выданы шины')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    data_ustanovki_shini = models.CharField(max_length=50,verbose_name='Дата установки шин')
    srok_sluzhbi_v_km = models.IntegerField(verbose_name='Срок службы в км. до списания шин')
    january_2020 = models.IntegerField(db_column='January_2020', blank=True, null=True,verbose_name='Январь_2020')  # Field name made lowercase.
    february_2020 = models.IntegerField(db_column='February_2020', blank=True, null=True,verbose_name='Февраль_2020')  # Field name made lowercase.
    march_2020 = models.IntegerField(db_column='March_2020', blank=True, null=True,verbose_name='Март_2020')  # Field name made lowercase.
    april_2020 = models.IntegerField(db_column='April_2020', blank=True, null=True,verbose_name='Апрель_2020')  # Field name made lowercase.
    may_2020 = models.IntegerField(db_column='May_2020', blank=True, null=True,verbose_name='Май_2020')  # Field name made lowercase.
    june_2020 = models.IntegerField(db_column='June_2020', blank=True, null=True,verbose_name='Июнь_2020')  # Field name made lowercase.
    july_2020 = models.IntegerField(db_column='July_2020', blank=True, null=True,verbose_name='Июль_2020')  # Field name made lowercase.
    august_2020 = models.IntegerField(db_column='August_2020', blank=True, null=True,verbose_name='Август_2020')  # Field name made lowercase.
    september_2020 = models.IntegerField(db_column='September_2020', blank=True, null=True,verbose_name='Сентябрь_2020')  # Field name made lowercase.
    october_2020 = models.IntegerField(db_column='October_2020', blank=True, null=True,verbose_name='Октябрь_2020')  # Field name made lowercase.
    november_2020 = models.IntegerField(db_column='November_2020', blank=True, null=True,verbose_name='Ноябрь_2020')  # Field name made lowercase.
    december_2020 = models.IntegerField(db_column='December_2020', blank=True, null=True,verbose_name='Декабрь_2020')  # Field name made lowercase.
    january_2021 = models.IntegerField(db_column='January_2021', blank=True, null=True,verbose_name='Январь_2021')  # Field name made lowercase.
    february_2021 = models.IntegerField(db_column='February_2021', blank=True, null=True,verbose_name='Февраль_2021')  # Field name made lowercase.
    march_2021 = models.IntegerField(db_column='March_2021', blank=True, null=True,verbose_name='Март_2021')  # Field name made lowercase.
    april_2021 = models.IntegerField(db_column='April_2021', blank=True, null=True,verbose_name='Апрель_2021')  # Field name made lowercase.
    may_2021 = models.IntegerField(db_column='May_2021', blank=True, null=True,verbose_name='Май_2021')  # Field name made lowercase.
    june_2021 = models.IntegerField(db_column='June_2021', blank=True, null=True,verbose_name='Июнь_2021')  # Field name made lowercase.
    july_2021 = models.IntegerField(db_column='July_2021', blank=True, null=True,verbose_name='Июль_2021')  # Field name made lowercase.
    august_2021 = models.IntegerField(db_column='August_2021', blank=True, null=True,verbose_name='Август_2021')  # Field name made lowercase.
    september_2021 = models.IntegerField(db_column='September_2021', blank=True, null=True,verbose_name='Сентябрь_2021')  # Field name made lowercase.
    october_2021 = models.IntegerField(db_column='October_2021', blank=True, null=True,verbose_name='Октябрь_2021')  # Field name made lowercase.
    november_2021 = models.IntegerField(db_column='November_2021', blank=True, null=True,verbose_name='Ноябрь_2021')  # Field name made lowercase.
    december_2021 = models.IntegerField(db_column='December_2021', blank=True, null=True,verbose_name='Декабрь_2021')  # Field name made lowercase.
    january_2022 = models.IntegerField(db_column='January_2022', blank=True, null=True,verbose_name='Январь_2022')  # Field name made lowercase.
    february_2022 = models.IntegerField(db_column='February_2022', blank=True, null=True,verbose_name='Февраль_2022')  # Field name made lowercase.
    march_2022 = models.IntegerField(db_column='March_2022', blank=True, null=True,verbose_name='Март_2022')  # Field name made lowercase.
    april_2022 = models.IntegerField(db_column='April_2022', blank=True, null=True,verbose_name='Апрель_2022')  # Field name made lowercase.
    may_2022 = models.IntegerField(db_column='May_2022', blank=True, null=True,verbose_name='Май_2022')  # Field name made lowercase.
    june_2022 = models.IntegerField(db_column='June_2022', blank=True, null=True,verbose_name='Июнь_2022')  # Field name made lowercase.
    july_2022 = models.IntegerField(db_column='July_2022', blank=True, null=True,verbose_name='Июль_2022')  # Field name made lowercase.
    august_2022 = models.IntegerField(db_column='August_2022', blank=True, null=True,verbose_name='Август_2022')  # Field name made lowercase.
    september_2022 = models.IntegerField(db_column='September_2022', blank=True, null=True,verbose_name='Сентябрь_2022')  # Field name made lowercase.
    october_2022 = models.IntegerField(db_column='October_2022', blank=True, null=True,verbose_name='Октябрь_2022')  # Field name made lowercase.
    november_2022 = models.IntegerField(db_column='November_2022', blank=True, null=True,verbose_name='Ноябрь_2022')  # Field name made lowercase.
    december_2022 = models.IntegerField(db_column='December_2022', blank=True, null=True,verbose_name='Декабрь_2022')  # Field name made lowercase.
    january_2023 = models.IntegerField(db_column='January_2023', blank=True, null=True,verbose_name='Январь_2023')  # Field name made lowercase.
    february_2023 = models.IntegerField(db_column='February_2023', blank=True, null=True,verbose_name='Февраль_2023')  # Field name made lowercase.
    march_2023 = models.IntegerField(db_column='March_2023', blank=True, null=True,verbose_name='Март_2023')  # Field name made lowercase.
    april_2023 = models.IntegerField(db_column='April_2023', blank=True, null=True,verbose_name='Апрель_2023')  # Field name made lowercase.
    may_2023 = models.IntegerField(db_column='May_2023', blank=True, null=True,verbose_name='Май_2023')  # Field name made lowercase.
    june_2023 = models.IntegerField(db_column='June_2023', blank=True, null=True,verbose_name='Июнь_2023')  # Field name made lowercase.
    july_2023 = models.IntegerField(db_column='July_2023', blank=True, null=True,verbose_name='Июль_2023')  # Field name made lowercase.
    august_2023 = models.IntegerField(db_column='August_2023', blank=True, null=True,verbose_name='Август_2023')  # Field name made lowercase.
    september_2023 = models.IntegerField(db_column='September_2023', blank=True, null=True,verbose_name='Сентябрь_2023')  # Field name made lowercase.
    october_2023 = models.IntegerField(db_column='October_2023', blank=True, null=True,verbose_name='Октябрь_2023')  # Field name made lowercase.
    november_2023 = models.IntegerField(db_column='November_2023', blank=True, null=True,verbose_name='Ноябрь_2023')  # Field name made lowercase.
    december_2023 = models.IntegerField(db_column='December_2023', blank=True, null=True,verbose_name='Декабрь_2023')  # Field name made lowercase.
    proideno_km_from_beginning = models.IntegerField(blank=True, null=True,verbose_name='Пройдено километров с момента установки шин')
    proideno_km_from_beginning_uchetom_zapasnogo = models.IntegerField(blank=True, null=True,verbose_name='Пройдено км с момента установки с учетом запасного колеса')
    ostalos_km_do_spisania = models.IntegerField(blank=True, null=True,verbose_name='Осталось километров до списания (с учетом запасного колеса)')

    class Meta:
        managed = False
        db_table = 'avtoshini_new'
        verbose_name = 'Автошины НУО'
        verbose_name_plural = 'Автошины НУО'
        

    def save(self, *args, **kwargs):
        main= Main.objects.get(field_p_p = self.id_techniki.field_p_p)  #gets a particular player into the variable player

        if self.january_2022 != NONE or self.february_2022 != NONE or self.march_2022 != NONE or self.april_2022 != NONE or self.may_2022 != NONE or self.june_2022 != NONE or self.july_2022 != NONE or self.august_2022 != NONE or self.september_2022 != NONE or self.october_2022 != NONE or self.november_2022 != NONE or self.december_2022 != NONE :
            self.proideno_km_from_beginning = (self.january_2020 + self.february_2020 + self.march_2020 + self.april_2020 + self.may_2020 + self.june_2020 + self.july_2020 + self.august_2020 + self.september_2020 + self.october_2020 + self.november_2020 + self.december_2020) + (self.january_2021 + self.february_2021 + self.march_2021 + self.april_2021 + self.may_2021 + self.june_2021 + self.july_2021 + self.august_2021 + self.september_2021 + self.october_2021 + self.november_2021 + self.december_2021) + (self.january_2022 + self.february_2022 + self.march_2022 + self.april_2022 + self.may_2022 + self.june_2022 + self.july_2022 + self.august_2022 + self.september_2022 + self.october_2022 + self.november_2022 + self.december_2022) + (self.january_2023 + self.february_2023 + self.march_2023 + self.april_2023 + self.may_2023 + self.june_2023 + self.july_2023 + self.august_2023 + self.september_2023 + self.october_2023 + self.november_2023 + self.december_2023)

        if self.january_2022 != NONE or self.february_2022 != NONE or self.march_2022 != NONE or self.april_2022 != NONE or self.may_2022 != NONE or self.june_2022 != NONE or self.july_2022 != NONE or self.august_2022 != NONE or self.september_2022 != NONE or self.october_2022 != NONE or self.november_2022 != NONE or self.december_2022 != NONE :
            self.proideno_km_from_beginning_uchetom_zapasnogo = (((self.january_2020 + self.february_2020 + self.march_2020 + self.april_2020 + self.may_2020 + self.june_2020 + self.july_2020 + self.august_2020 + self.september_2020 + self.october_2020 + self.november_2020 + self.december_2020) + (self.january_2021 + self.february_2021 + self.march_2021 + self.april_2021 + self.may_2021 + self.june_2021 + self.july_2021 + self.august_2021 + self.september_2021 + self.october_2021 + self.november_2021 + self.december_2021) + (self.january_2022 + self.february_2022 + self.march_2022 + self.april_2022 + self.may_2022 + self.june_2022 + self.july_2022 + self.august_2022 + self.september_2022 + self.october_2022 + self.november_2022 + self.december_2022) + (self.january_2023 + self.february_2023 + self.march_2023 + self.april_2023 + self.may_2023 + self.june_2023 + self.july_2023 + self.august_2023 + self.september_2023 + self.october_2023 + self.november_2023 + self.december_2023)) / self.kolichestvo_shin) * (self.kolichestvo_shin - 1)

        if self.january_2022 != NONE or self.february_2022 != NONE or self.march_2022 != NONE or self.april_2022 != NONE or self.may_2022 != NONE or self.june_2022 != NONE or self.july_2022 != NONE or self.august_2022 != NONE or self.september_2022 != NONE or self.october_2022 != NONE or self.november_2022 != NONE or self.december_2022 != NONE :
            self.ostalos_km_do_spisania = self.srok_sluzhbi_v_km - ((((self.january_2020 + self.february_2020 + self.march_2020 + self.april_2020 + self.may_2020 + self.june_2020 + self.july_2020 + self.august_2020 + self.september_2020 + self.october_2020 + self.november_2020 + self.december_2020) + (self.january_2021 + self.february_2021 + self.march_2021 + self.april_2021 + self.may_2021 + self.june_2021 + self.july_2021 + self.august_2021 + self.september_2021 + self.october_2021 + self.november_2021 + self.december_2021) + (self.january_2022 + self.february_2022 + self.march_2022 + self.april_2022 + self.may_2022 + self.june_2022 + self.july_2022 + self.august_2022 + self.september_2022 + self.october_2022 + self.november_2022 + self.december_2022) + (self.january_2023 + self.february_2023 + self.march_2023 + self.april_2023 + self.may_2023 + self.june_2023 + self.july_2023 + self.august_2023 + self.september_2023 + self.october_2023 + self.november_2023 + self.december_2023)) / self.kolichestvo_shin) * (self.kolichestvo_shin - 1))
        super(AvtoshiniNew, self).save(*args, **kwargs)


class Goroda(models.Model):
    gorod_id = models.AutoField(primary_key=True,verbose_name="ID")
    name = models.CharField(db_column='Name', max_length=50,verbose_name="Название города")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goroda'
        verbose_name = 'Города'
        verbose_name_plural = 'Города'


class Main(models.Model):
    field_p_p = models.AutoField(db_column='№_p/p', primary_key=True,verbose_name='№ p/p')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100, verbose_name='Подчиненность')  # Field name made lowercase.
    rod_voiska = models.CharField(max_length=50, verbose_name='Род войск')
    gorod = models.CharField(max_length=50,verbose_name='Город')
    field_voinsnkoi_chasti = models.CharField(db_column='№_voinsnkoi_chasti', max_length=50,verbose_name='№ воинской части')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    podrazdelenia = models.CharField(db_column='Podrazdelenia', max_length=50,verbose_name='Подразделение')  # Field name made lowercase.
    osnov_postanovki_tech_na_uchet = models.CharField(db_column='Osnov_postanovki_tech_na_uchet', max_length=255,verbose_name='Основание постановки машины на учет')  # Field name made lowercase.
    marka_avto = models.CharField(db_column='Marka_avto', max_length=50,verbose_name='Марка автомобиля')  # Field name made lowercase.
    voenni_reg_nomer = models.CharField(max_length=50, unique=True,verbose_name='Военный номерной регистрационный знак')
    photo_front = models.ImageField(blank=True, null=True, default='images/KiaQuoris_front.jpg', upload_to='images/',verbose_name='Фото спереди')
    photo_site = models.ImageField(blank=True, null=True, default='images/KiaQuoris_front.jpg', upload_to='images/',verbose_name='Фото сбоку')
    photo_back = models.ImageField(blank=True, null=True, default='images/KiaQuoris_front.jpg', upload_to='images/',verbose_name='Фото сзади')
    photo_engine = models.ImageField(blank=True, null=True, default='images/KiaQuoris_front.jpg', upload_to='images/',verbose_name='Фото двигателя')
    photo_trunk = models.ImageField(blank=True, null=True, default='images/KiaQuoris_front.jpg', upload_to='images/',verbose_name='Фото АКБ')
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True, verbose_name='Тип')  # Field name made lowercase.
    vid = models.CharField(max_length=50, blank=True, null=True, verbose_name='Вид')
    gruppa_ekspluatacii = models.CharField(max_length=50, blank=True, null=True,verbose_name='Группа эксплуатации')
    field_shassi = models.CharField(db_column='№_shassi', max_length=50, blank=True, null=True,verbose_name='№  Шасси')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.CharField(db_column='№_dvigatelia', max_length=50, blank=True, null=True,verbose_name='№ двигателя')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_kabini = models.CharField(db_column='№_kabini', max_length=50, blank=True, null=True,verbose_name='№ кабины')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    god_vipuska = models.TextField(blank=True, null=True,verbose_name='Год выпуска')  # This field type is a guess.
    seria_nomer_pasporta = models.CharField(db_column='seria&nomer_pasporta', max_length=50,verbose_name='Серия и номер паспорта')  # Field renamed to remove unsuitable characters.
    color = models.CharField(max_length=50,blank=True, null=True,verbose_name='Цвет')
    nomer_svedit_o_reg = models.CharField(max_length=50,verbose_name='Номер свидетельства о регистрации')
    category = models.CharField(max_length=50,blank=True, null=True,verbose_name='Категория')
    january_2020 = models.IntegerField(db_column='January_2020', blank=True, null=True, verbose_name='Январь 2020')  # Field name made lowercase.
    february_2020 = models.IntegerField(db_column='February_2020', blank=True, null=True, verbose_name='Февраль 2020')  # Field name made lowercase.
    march_2020 = models.IntegerField(db_column='March_2020', blank=True, null=True, verbose_name='Март 2020')  # Field name made lowercase.
    april_2020 = models.IntegerField(db_column='April_2020', blank=True, null=True, verbose_name='Апрель 2020')  # Field name made lowercase.
    may_2020 = models.IntegerField(db_column='May_2020', blank=True, null=True, verbose_name='Май 2020')  # Field name made lowercase.
    june_2020 = models.IntegerField(db_column='June_2020', blank=True, null=True, verbose_name='Июнь 2020')  # Field name made lowercase.
    july_2020 = models.IntegerField(db_column='July_2020', blank=True, null=True, verbose_name='Июль 2020')  # Field name made lowercase.
    august_2020 = models.IntegerField(db_column='August_2020', blank=True, null=True, verbose_name='Август 2020')  # Field name made lowercase.
    september_2020 = models.IntegerField(db_column='September_2020', blank=True, null=True, verbose_name='Сентябрь 2020')  # Field name made lowercase.
    october_2020 = models.IntegerField(db_column='October_2020', blank=True, null=True, verbose_name='Октябрь 2020')  # Field name made lowercase.
    november_2020 = models.IntegerField(db_column='November_2020', blank=True, null=True, verbose_name='Ноябрь 2020')  # Field name made lowercase.
    december_2020 = models.IntegerField(db_column='December_2020', blank=True, null=True, verbose_name='Декабрь 2020')  # Field name made lowercase.
    january_2021 = models.IntegerField(db_column='January_2021', blank=True, null=True, verbose_name='Январь 2021')  # Field name made lowercase.
    february_2021 = models.IntegerField(db_column='February_2021', blank=True, null=True, verbose_name='Февраль 2021')  # Field name made lowercase.
    march_2021 = models.IntegerField(db_column='March_2021', blank=True, null=True, verbose_name='Март 2021')  # Field name made lowercase.
    april_2021 = models.IntegerField(db_column='April_2021', blank=True, null=True, verbose_name='Апрель 2021')  # Field name made lowercase.
    may_2021 = models.IntegerField(db_column='May_2021', blank=True, null=True, verbose_name='Май 2021')  # Field name made lowercase.
    june_2021 = models.IntegerField(db_column='June_2021', blank=True, null=True, verbose_name='Июнь 2021')  # Field name made lowercase.
    july_2021 = models.IntegerField(db_column='July_2021', blank=True, null=True, verbose_name='Июль 2021')  # Field name made lowercase.
    august_2021 = models.IntegerField(db_column='August_2021', blank=True, null=True, verbose_name='Август 2021')  # Field name made lowercase.
    september_2021 = models.IntegerField(db_column='September_2021', blank=True, null=True, verbose_name='Сентябрь 2021')  # Field name made lowercase.
    october_2021 = models.IntegerField(db_column='October_2021', blank=True, null=True, verbose_name='Октябрь 2021')  # Field name made lowercase.
    november_2021 = models.IntegerField(db_column='November_2021', blank=True, null=True, verbose_name='Ноябрь 2021')  # Field name made lowercase.
    december_2021 = models.IntegerField(db_column='December_2021', blank=True, null=True, verbose_name='Декабрь 2021')  # Field name made lowercase.
    speedometer_01_01_2022 = models.IntegerField(blank=True, null=True, verbose_name='Показания спидометра на 1.01.2022')
    videleno_motoresurs_na_year = models.IntegerField(verbose_name='Выделено моторесурсов на год')
    january_2022 = models.IntegerField(db_column='January_2022', blank=True, null=True, verbose_name='Январь 2022')  # Field name made lowercase.
    february_2022 = models.IntegerField(db_column='February_2022', blank=True, null=True, verbose_name='Февраль 2022')  # Field name made lowercase.
    march_2022 = models.IntegerField(db_column='March_2022', blank=True, null=True, verbose_name='Март 2022')  # Field name made lowercase.
    april_2022 = models.IntegerField(db_column='April_2022', blank=True, null=True, verbose_name='Апрель 2022')  # Field name made lowercase.
    may_2022 = models.IntegerField(db_column='May_2022', blank=True, null=True, verbose_name='Май 2022')  # Field name made lowercase.
    june_2022 = models.IntegerField(db_column='June_2022', blank=True, null=True, verbose_name='Июнь 2022')  # Field name made lowercase.
    july_2022 = models.IntegerField(db_column='July_2022', blank=True, null=True, verbose_name='Июль 2022')  # Field name made lowercase.
    august_2022 = models.IntegerField(db_column='August_2022', blank=True, null=True, verbose_name='Август 2022')  # Field name made lowercase.
    september_2022 = models.IntegerField(db_column='September_2022', blank=True, null=True, verbose_name='Сентябрь 2022')  # Field name made lowercase.
    october_2022 = models.IntegerField(db_column='October_2022', blank=True, null=True, verbose_name='Октябрь 2022')  # Field name made lowercase.
    november_2022 = models.IntegerField(db_column='November_2022', blank=True, null=True, verbose_name='Ноябрь 2022')  # Field name made lowercase.
    december_2022 = models.IntegerField(db_column='December_2022', blank=True, null=True, verbose_name='Декабрь 2022')  # Field name made lowercase.
    january_2023 = models.IntegerField(db_column='January_2023', blank=True, null=True, verbose_name='Январь 2023')  # Field name made lowercase.
    february_2023 = models.IntegerField(db_column='February_2023', blank=True, null=True, verbose_name='Февраль 2023')  # Field name made lowercase.
    march_2023 = models.IntegerField(db_column='March_2023', blank=True, null=True, verbose_name='Март 2023')  # Field name made lowercase.
    april_2023 = models.IntegerField(db_column='April_2023', blank=True, null=True, verbose_name='Апрель 2023')  # Field name made lowercase.
    may_2023 = models.IntegerField(db_column='May_2023', blank=True, null=True, verbose_name='Май 2023')  # Field name made lowercase.
    june_2023 = models.IntegerField(db_column='June_2023', blank=True, null=True, verbose_name='Июнь 2023')  # Field name made lowercase.
    july_2023 = models.IntegerField(db_column='July_2023', blank=True, null=True, verbose_name='Июль 2023')  # Field name made lowercase.
    august_2023 = models.IntegerField(db_column='August_2023', blank=True, null=True, verbose_name='Август 2023')  # Field name made lowercase.
    september_2023 = models.IntegerField(db_column='September_2023', blank=True, null=True, verbose_name='Сентябрь 2023')  # Field name made lowercase.
    october_2023 = models.IntegerField(db_column='October_2023', blank=True, null=True, verbose_name='Октябрь 2023')  # Field name made lowercase.
    november_2023 = models.IntegerField(db_column='November_2023', blank=True, null=True, verbose_name='Ноябрь 2023')  # Field name made lowercase.
    december_2023 = models.IntegerField(db_column='December_2023', blank=True, null=True, verbose_name='Декабрь 2023')  # Field name made lowercase.
    izrashodovano_s_nachalo_year = models.IntegerField(blank=True, null=True,verbose_name='Израсходовано моторесурсов с начало года')
    ostatok_resursov_do_konca_year = models.IntegerField(blank=True, null=True,verbose_name='Остаток моторесурсов до конца года')
    mileage_from_beginning = models.IntegerField(blank=True, null=True,verbose_name='Пробег с начала эксплуатации')
    tech_sostoianie = models.CharField(db_column='Tech_Sostoianie', max_length=255, blank=True, null=True,verbose_name='Техническое состояние')  # Field name made lowercase.
    vid_and_data_remonta = models.CharField(max_length=255, blank=True, null=True,verbose_name='Вид и дата проведенного ремонта')
    primechanie = models.CharField(max_length=1000, blank=True, null=True,verbose_name='Примечание')
    motoresurs_to_1 = models.IntegerField(blank=True, null=True,verbose_name='Осталось моторесурсов до ТО № 1')
    motoresurs_to_2 = models.IntegerField(blank=True, null=True,verbose_name='Осталось моторесурсов до ТО № 2')
    ostalos_motoresurs_tp = models.IntegerField(db_column='ostalos_motoresurs_TP', blank=True, null=True,verbose_name='Осталось моторесурсов до ТР')  # Field name made lowercase.
    ostalos_motoresurs_cp = models.IntegerField(db_column='ostalos_motoresurs_CP', blank=True, null=True,verbose_name='Осталось моторесурсов до СР')  # Field name made lowercase.
    ostalos_motoresurs_kp = models.IntegerField(db_column='ostalos_motoresurs_KP', blank=True, null=True,verbose_name='Осталось моторесурсов до КР')  # Field name made lowercase.
    ostalos_motoresurs_spisanie = models.IntegerField(blank=True, null=True,verbose_name='Осталось моторесурсов до списания')
    type_akb = models.CharField(max_length=50, blank=True, null=True,verbose_name='Тип АКБ')
    kolichestvo_akb = models.IntegerField(blank=True, null=True,verbose_name='Количество АКБ')
    kev_vidano = models.CharField(max_length=50, blank=True, null=True,verbose_name='Кем выдано')
    field_nariad_kogda_vidano = models.CharField(db_column='№_nariad_kogda_vidano', max_length=50, blank=True, null=True,verbose_name='№ наряда и когда выдано')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    srok_sluzhbi_akb = models.IntegerField(blank=True, null=True,verbose_name='Срок службы АКБ')
    data_ustanovki_akb = models.DateField(blank=True, null=True,verbose_name=' Дата установки АКБ')
    data_spisania_akb_po_godam = models.DateField(blank=True, null=True,verbose_name='Дата списания АКБ по годам')
    srok_sluzhbi_akb_v_km_do_spisania = models.IntegerField(blank=True, null=True,verbose_name='Срок службы в км. до списания АКБ')
    akb_january_2020 = models.IntegerField(db_column='Akb_January_2020', blank=True, null=True,verbose_name='Январь АКБ 2020')  # Field name made lowercase.
    akb_february_2020 = models.IntegerField(db_column='Akb_February_2020', blank=True, null=True,verbose_name='Февраль АКБ 2020')  # Field name made lowercase.
    akb_march_2020 = models.IntegerField(db_column='Akb_March_2020', blank=True, null=True,verbose_name='Март АКБ 2020')  # Field name made lowercase.
    akb_april_2020 = models.IntegerField(db_column='Akb_April_2020', blank=True, null=True,verbose_name='Апрель АКБ 2020')  # Field name made lowercase.
    akb_may_2020 = models.IntegerField(db_column='Akb_May_2020', blank=True, null=True,verbose_name='Май АКБ 2020')  # Field name made lowercase.
    akb_june_2020 = models.IntegerField(db_column='Akb_June_2020', blank=True, null=True,verbose_name='Июнь АКБ 2020')  # Field name made lowercase.
    akb_july_2020 = models.IntegerField(db_column='Akb_July_2020', blank=True, null=True,verbose_name='Июль АКБ 2020')  # Field name made lowercase.
    akb_august_2020 = models.IntegerField(db_column='Akb_August_2020', blank=True, null=True,verbose_name='Август АКБ 2020')  # Field name made lowercase.
    akb_september_2020 = models.IntegerField(db_column='Akb_September_2020', blank=True, null=True,verbose_name='Сентябрь АКБ 2020')  # Field name made lowercase.
    akb_october_2020 = models.IntegerField(db_column='Akb_October_2020', blank=True, null=True,verbose_name='Октябрь АКБ 2020')  # Field name made lowercase.
    akb_november_2020 = models.IntegerField(db_column='Akb_November_2020', blank=True, null=True,verbose_name='Ноябрь АКБ 2020')  # Field name made lowercase.
    akb_december_2020 = models.IntegerField(db_column='Akb_December_2020', blank=True, null=True,verbose_name='Декабрь АКБ 2020')  # Field name made lowercase.
    akb_january_2021 = models.IntegerField(db_column='Akb_January_2021', blank=True, null=True,verbose_name='Январь АКБ 2021')  # Field name made lowercase.
    akb_february_2021 = models.IntegerField(db_column='Akb_February_2021', blank=True, null=True,verbose_name='Февраль АКБ 2021')  # Field name made lowercase.
    akb_march_2021 = models.IntegerField(db_column='Akb_March_2021', blank=True, null=True,verbose_name='Март АКБ 2021')  # Field name made lowercase.
    akb_april_2021 = models.IntegerField(db_column='Akb_April_2021', blank=True, null=True,verbose_name='Апрель АКБ 2021')  # Field name made lowercase.
    akb_may_2021 = models.IntegerField(db_column='Akb_May_2021', blank=True, null=True,verbose_name='Май АКБ 2021')  # Field name made lowercase.
    akb_june_2021 = models.IntegerField(db_column='Akb_June_2021', blank=True, null=True,verbose_name='Июнь АКБ 2021')  # Field name made lowercase.
    akb_july_2021 = models.IntegerField(db_column='Akb_July_2021', blank=True, null=True,verbose_name='Июль АКБ 2021')  # Field name made lowercase.
    akb_august_2021 = models.IntegerField(db_column='Akb_August_2021', blank=True, null=True,verbose_name='Август АКБ 2021')  # Field name made lowercase.
    akb_september_2021 = models.IntegerField(db_column='Akb_September_2021', blank=True, null=True,verbose_name='Сентябрь АКБ 2021')  # Field name made lowercase.
    akb_october_2021 = models.IntegerField(db_column='Akb_October_2021', blank=True, null=True,verbose_name='Октябрь АКБ 2021')  # Field name made lowercase.
    akb_november_2021 = models.IntegerField(db_column='Akb_November_2021', blank=True, null=True,verbose_name='Ноябрь АКБ 2021')  # Field name made lowercase.
    akb_december_2021 = models.IntegerField(db_column='Akb_December_2021', blank=True, null=True,verbose_name='Декабрь АКБ 2021')  # Field name made lowercase.
    akb_january_2022 = models.IntegerField(db_column='Akb_January_2022', blank=True, null=True,verbose_name='Январь АКБ 2022')  # Field name made lowercase.
    akb_february_2022 = models.IntegerField(db_column='Akb_February_2022', blank=True, null=True,verbose_name='Февраль АКБ 2022')  # Field name made lowercase.
    akb_march_2022 = models.IntegerField(db_column='Akb_March_2022', blank=True, null=True,verbose_name='Март АКБ 2022')  # Field name made lowercase.
    akb_april_2022 = models.IntegerField(db_column='Akb_April_2022', blank=True, null=True,verbose_name='Апрель АКБ 2022')  # Field name made lowercase.
    akb_may_2022 = models.IntegerField(db_column='Akb_May_2022', blank=True, null=True,verbose_name='Май АКБ 2022')  # Field name made lowercase.
    akb_june_2022 = models.IntegerField(db_column='Akb_June_2022', blank=True, null=True,verbose_name='Июнь АКБ 2022')  # Field name made lowercase.
    akb_july_2022 = models.IntegerField(db_column='Akb_July_2022', blank=True, null=True,verbose_name='Июль АКБ 2022')  # Field name made lowercase.
    akb_august_2022 = models.IntegerField(db_column='Akb_August_2022', blank=True, null=True,verbose_name='Август АКБ 2022')  # Field name made lowercase.
    akb_september_2022 = models.IntegerField(db_column='Akb_September_2022', blank=True, null=True,verbose_name='Сентябрь АКБ 2022')  # Field name made lowercase.
    akb_october_2022 = models.IntegerField(db_column='Akb_October_2022', blank=True, null=True,verbose_name='Октябрь АКБ 2022')  # Field name made lowercase.
    akb_november_2022 = models.IntegerField(db_column='Akb_November_2022', blank=True, null=True,verbose_name='Ноябрь АКБ 2022')  # Field name made lowercase.
    akb_december_2022 = models.IntegerField(db_column='Akb_December_2022', blank=True, null=True,verbose_name='Декабрь АКБ 2022')  # Field name made lowercase.
    akb_january_2023 = models.IntegerField(db_column='Akb_January_2023', blank=True, null=True, verbose_name='Январь АКБ 2023')  # Field name made lowercase.
    akb_february_2023 = models.IntegerField(db_column='Akb_February_2023', blank=True, null=True, verbose_name='Февраль АКБ 2023')  # Field name made lowercase.
    akb_march_2023 = models.IntegerField(db_column='Akb_March_2023', blank=True, null=True, verbose_name='Март АКБ 2023')  # Field name made lowercase.
    akb_april_2023 = models.IntegerField(db_column='Akb_April_2023', blank=True, null=True, verbose_name='Апрель АКБ 2023')  # Field name made lowercase.
    akb_may_2023 = models.IntegerField(db_column='Akb_May_2023', blank=True, null=True, verbose_name='Май АКБ 2023')  # Field name made lowercase.
    akb_june_2023 = models.IntegerField(db_column='Akb_June_2023', blank=True, null=True, verbose_name='Июнь АКБ 2023')  # Field name made lowercase.
    akb_july_2023 = models.IntegerField(db_column='Akb_July_2023', blank=True, null=True, verbose_name='Июль АКБ 2023')  # Field name made lowercase.
    akb_august_2023 = models.IntegerField(db_column='Akb_August_2023', blank=True, null=True, verbose_name='Август АКБ 2023')  # Field name made lowercase.
    akb_september_2023 = models.IntegerField(db_column='Akb_September_2023', blank=True, null=True, verbose_name='Сентябрь АКБ 2023')  # Field name made lowercase.
    akb_october_2023 = models.IntegerField(db_column='Akb_October_2023', blank=True, null=True, verbose_name='Октябрь АКБ 2023')  # Field name made lowercase.
    akb_november_2023 = models.IntegerField(db_column='Akb_November_2023', blank=True, null=True, verbose_name='Ноябрь АКБ 2023')  # Field name made lowercase.
    akb_december_2023 = models.IntegerField(db_column='Akb_December_2023', blank=True, null=True, verbose_name='Декабрь АКБ 2023')  # Field name made lowercase.
    proideno_km_from_beginning_akb = models.IntegerField(blank=True, null=True,verbose_name='Пройдено км с момента установки АКБ')
    akb_ostalos_km_do_spisania = models.IntegerField(db_column='Akb_ostalos_km_do_spisania', blank=True, null=True,verbose_name='Осталось км. до списания')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main'
        verbose_name = 'Национальный Университет Обороны'
        verbose_name_plural = 'Национальный Университет Обороны'

        
    def save(self, *args, **kwargs):
        # Моторесурсы
        if self.january_2022 != NONE or self.february_2022 != NONE or self.march_2022 != NONE or self.april_2022 != NONE or self.may_2022 != NONE or self.june_2022 != NONE or self.july_2022 != NONE or self.august_2022 != NONE or self.september_2022 != NONE or self.october_2022 != NONE or self.november_2022 != NONE or self.december_2022 != NONE :
            self.izrashodovano_s_nachalo_year = self.january_2022 + self.february_2022 + self.march_2022 + self.april_2022 + self.may_2022 + self.june_2022 + self.july_2022 + self.august_2022 + self.september_2022 + self.october_2022 + self.november_2022 + self.december_2022 
        if  self.videleno_motoresurs_na_year != None:
            self.ostatok_resursov_do_konca_year = self.videleno_motoresurs_na_year - (self.january_2022 + self.february_2022 + self.march_2022 + self.april_2022 + self.may_2022 + self.june_2022 + self.july_2022 + self.august_2022 + self.september_2022 + self.october_2022 + self.november_2022 + self.december_2022)
        if self.january_2021 != NONE or self.february_2021 != NONE or self.march_2021 != NONE or self.april_2021 != NONE or self.may_2021 != NONE or self.june_2021 != NONE or self.july_2021 != NONE or self.august_2021 != NONE or self.september_2021 != NONE or self.october_2021 != NONE or self.november_2021 != NONE or self.december_2021 != NONE :
            self.mileage_from_beginning = (self.january_2020 + self.february_2020 + self.march_2020 + self.april_2020 + self.may_2020 + self.june_2020 + self.july_2020 + self.august_2020 + self.september_2020 + self.october_2020 + self.november_2020 + self.december_2020) + (self.january_2021 + self.february_2021 + self.march_2021 + self.april_2021 + self.may_2021 + self.june_2021 + self.july_2021 + self.august_2021 + self.september_2021 + self.october_2021 + self.november_2021 + self.december_2021) + (self.january_2022 + self.february_2022 + self.march_2022 + self.april_2022 + self.may_2022 + self.june_2022 + self.july_2022 + self.august_2022 + self.september_2022 + self.october_2022 + self.november_2022 + self.december_2022) + (self.january_2023 + self.february_2023 + self.march_2023 + self.april_2023 + self.may_2023 + self.june_2023 + self.july_2023 + self.august_2023 + self.september_2023 + self.october_2023 + self.november_2023 + self.december_2023)
        if  self.data_ustanovki_akb != None:
            self.data_spisania_akb_po_godam = (self.data_ustanovki_akb  + timedelta(days=1096) ).strftime('%Y-%m-%d')
        
        # АКБ все
        # Месяцы по АКБ
        # if self.january != None:
        #     self.akb_january = 0 + self.january
        # if self.february != None:
        #     self.akb_february = 0 + self.february
        # if self.march != None:
        #     self.akb_march = 0 + self.march
        # if self.april != None:
        #     self.akb_april = 0 + self.april
        # if self.may != None:
        #     self.akb_may = 0 + self.may
        # if self.june != None:
        #     self.akb_june = 0 + self.june
        # if self.july != None:
        #     self.akb_july = 0 + self.july
        # if self.august != None:
        #     self.akb_august = 0 + self.august
        # if self.september != None:
        #     self.akb_september = 0 + self.september
        # if self.october != None:
        #     self.akb_october = 0 + self.october
        # if self.november != None:
        #     self.akb_november = 0 + self.november
        # if self.december != None:
        #     self.akb_december = 0 + self.december
        if self.january_2022 != NONE or self.february_2022 != NONE or self.march_2022 != NONE or self.april_2022 != NONE or self.may_2022 != NONE or self.june_2022 != NONE or self.july_2022 != NONE or self.august_2022 != NONE or self.september_2022 != NONE or self.october_2022 != NONE or self.november_2022 != NONE or self.december_2022 != NONE:
            self.proideno_km_from_beginning_akb = (self.akb_january_2020 + self.akb_february_2020 + self.akb_march_2020 + self.akb_april_2020 + self.akb_may_2020 + self.akb_june_2020 + self.akb_july_2020 + self.akb_august_2020 + self.akb_september_2020 + self.akb_october_2020 + self.akb_november_2020 + self.akb_december_2020) + (self.akb_january_2021 + self.akb_february_2021 + self.akb_march_2021 + self.akb_april_2021 + self.akb_may_2021 + self.akb_june_2021 + self.akb_july_2021 + self.akb_august_2021 + self.akb_september_2021 + self.akb_october_2021 + self.akb_november_2021 + self.akb_december_2021) + (self.akb_january_2022 + self.akb_february_2022 + self.akb_march_2022 + self.akb_april_2022 + self.akb_may_2022 + self.akb_june_2022 + self.akb_july_2022 + self.akb_august_2022 + self.akb_september_2022 + self.akb_october_2022 + self.akb_november_2022 + self.akb_december_2022) + (self.akb_january_2023 + self.akb_february_2023 + self.akb_march_2023 + self.akb_april_2023 + self.akb_may_2023 + self.akb_june_2023 + self.akb_july_2023 + self.akb_august_2023 + self.akb_september_2023 + self.akb_october_2023 + self.akb_november_2023 + self.akb_december_2023)
        if  self.srok_sluzhbi_akb_v_km_do_spisania != None:
            self.akb_ostalos_km_do_spisania = self.srok_sluzhbi_akb_v_km_do_spisania - self.proideno_km_from_beginning_akb
        
        super(Main, self).save(*args, **kwargs)


class ObiektiVvt(models.Model):
    id_vvt = models.AutoField(primary_key=True,verbose_name="ID")
    marka_vvt = models.CharField(db_column='Marka_VVT', max_length=50,verbose_name="Марка АТ")  # Field name made lowercase.
    voenni_reg_nomer = models.CharField(max_length=50, blank=True, null=True,verbose_name="Военный номер")
    god_vipuska = models.DateField(blank=True, null=True,verbose_name="Год выпуска")
    field_shassi = models.IntegerField(db_column='№_shassi', blank=True, null=True,verbose_name="№ шасси")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.IntegerField(db_column='№_dvigatelia', blank=True, null=True,verbose_name="№ двигателя")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_pasport_formulara = models.IntegerField(db_column='№_pasport_formulara', blank=True, null=True,verbose_name="серия и № паспорта формуляра")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100,verbose_name="РГК")  # Field name made lowercase.
    gorod = models.CharField(max_length=50, blank=True, null=True,verbose_name="Город")
    gruppa_ekspluatacii = models.CharField(max_length=50,verbose_name="группа эксплуатаций")
    category = models.CharField(max_length=50, blank=True, null=True,verbose_name="Категория")
    norma_rashoda = models.CharField(max_length=50, blank=True, null=True,verbose_name="Норма расхода")
    type_of_mark = models.CharField(max_length=50, blank=True, null=True,verbose_name="Тип марки")
    rod_voiska = models.CharField(max_length=50,verbose_name="Род войск")
    voiskovaia_chast = models.CharField(max_length=50,verbose_name="Войсковая часть")
    podrazdelenia = models.CharField(max_length=50, blank=True, null=True,verbose_name="Подразделения")
    tp = models.IntegerField(db_column='TP', blank=True, null=True,verbose_name="ТР")  # Field name made lowercase.
    cp = models.IntegerField(db_column='CP', blank=True, null=True,verbose_name="СР")  # Field name made lowercase.
    kp = models.IntegerField(db_column='KP', blank=True, null=True,verbose_name="КР")  # Field name made lowercase.
    spisanie = models.CharField(db_column='Spisanie', max_length=50, blank=True, null=True,verbose_name="Списание")  # Field name made lowercase.
    sostoianie = models.CharField(db_column='Sostoianie', max_length=255, blank=True, null=True,verbose_name="Состояние")  # Field name made lowercase.
    need = models.IntegerField(db_column='Need', blank=True, null=True,verbose_name="Потребность")  # Field name made lowercase.
    available = models.IntegerField(blank=True, null=True,verbose_name="Имеется")
    shortage = models.IntegerField(blank=True, null=True,verbose_name="Некомплект")
    excess = models.IntegerField(blank=True, null=True,verbose_name="Излишествует")

    class Meta:
        managed = False
        db_table = 'obiekti_vvt'
        verbose_name = 'Общие данные АТ'
        verbose_name_plural = 'Общие данные АТ'


class Peremeshenie(models.Model):
    premesh_id = models.AutoField(primary_key=True,verbose_name="ID")
    field_prikaza_nomer_date_field = models.IntegerField(db_column='№_prikaza(nomer, date)',verbose_name="№ приказа")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    obiekti_vvt = models.CharField(db_column='Obiekti_vvt', max_length=50,verbose_name="Обьекты ВВТ")  # Field name made lowercase.
    voiskovaia_chast = models.CharField(db_column='Voiskovaia_chast', max_length=50,verbose_name="Войсковая часть")  # Field name made lowercase.
    podrazdelenia = models.CharField(db_column='Podrazdelenia', max_length=50,verbose_name="Подразделения")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peremeshenie'
        verbose_name = 'Перемещение'
        verbose_name_plural = 'Перемещение'


class Podrazdelenia(models.Model):
    id_podrazdelenia = models.AutoField(primary_key=True,verbose_name="ID")
    name = models.CharField(db_column='Name', max_length=50,verbose_name="Название")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'podrazdelenia'
        verbose_name = 'Подразделения'
        verbose_name_plural = 'Подразделения'


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
    id_vvt = models.AutoField(primary_key=True, verbose_name="ID")
    marka_vvt = models.CharField(db_column='Marka_VVT', max_length=50,verbose_name="Марка АТ")  # Field name made lowercase.
    nomer_znak = models.CharField(max_length=50, blank=True, null=True,verbose_name="Номерной знак")
    god_vipuska = models.DateField(blank=True, null=True,verbose_name="Год выпуска")
    color = models.CharField(max_length=50, blank=True, null=True,verbose_name="Цвет")
    field_shassi = models.CharField(db_column='№_shassi', max_length=50, blank=True, null=True,verbose_name="№ шасси")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.CharField(db_column='№_dvigatelia', max_length=50, blank=True, null=True,verbose_name="№ двигателя")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_seria_pasporta = models.CharField(db_column='№_seria_pasporta', max_length=50, blank=True, null=True,verbose_name="№ серия паспорта")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_kuzova = models.CharField(db_column='№_kuzova', max_length=50, blank=True, null=True,verbose_name="№ кузова (кабины)")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_tech_talon = models.CharField(db_column='№_tech_talon', max_length=50, blank=True, null=True,verbose_name="№ технического талона")  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100,verbose_name="РГК")  # Field name made lowercase.
    garnizon = models.CharField(max_length=100, blank=True, null=True,verbose_name="Гарнизон")
    gorod = models.CharField(max_length=50, blank=True, null=True,verbose_name="Город")
    gruppa_ekspluatacii = models.CharField(max_length=50, blank=True, null=True,verbose_name="Группа эксплуатации")
    vid = models.CharField(max_length=50, blank=True, null=True,verbose_name="Вид")
    category = models.CharField(max_length=50, blank=True, null=True,verbose_name="Категория")
    norma_rashoda = models.CharField(max_length=50, blank=True, null=True,verbose_name="Норма расхода")
    type_of_mark = models.CharField(max_length=50, blank=True, null=True,verbose_name="Тип марки")
    rod_voiska = models.CharField(max_length=50, blank=True, null=True,verbose_name="Род войск")
    voiskovaia_chast = models.CharField(max_length=50,verbose_name="Войсковая часть")
    podrazdelenia = models.CharField(max_length=50, blank=True, null=True,verbose_name="Подразделения")
    mileage = models.IntegerField(blank=True, null=True,verbose_name="Пробег")
    tp = models.IntegerField(db_column='TP', blank=True, null=True,verbose_name="ТР")  # Field name made lowercase.
    cp = models.IntegerField(db_column='CP', blank=True, null=True,verbose_name="СР")  # Field name made lowercase.
    kp = models.IntegerField(db_column='KP', blank=True, null=True,verbose_name="КР")  # Field name made lowercase.
    primechanie = models.CharField(db_column='Primechanie', max_length=255, blank=True, null=True,verbose_name="Примечание")  # Field name made lowercase.
    sostoianie = models.CharField(db_column='Sostoianie', max_length=255, blank=True, null=True,verbose_name="Состояние")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vvt'
        verbose_name = 'Объекты АТ индивидуально'
        verbose_name_plural = 'Объекты АТ индивидуально'