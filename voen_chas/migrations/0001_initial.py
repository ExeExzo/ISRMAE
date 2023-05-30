# Generated by Django 4.0.5 on 2022-07-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vvt',
            fields=[
                ('id_vvt', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_vvt', models.CharField(db_column='Marka_VVT', max_length=50, verbose_name='Марка ВВТ')),
                ('god_vipuska', models.DateField(blank=True, null=True, verbose_name='Год выпуска')),
                ('field_shassi', models.IntegerField(blank=True, db_column='№_shassi', null=True, verbose_name='№ шасси')),
                ('field_dvigatelia', models.IntegerField(blank=True, db_column='№_dvigatelia', null=True, verbose_name='№ двигателя')),
                ('field_pasport_formulara', models.IntegerField(blank=True, db_column='№_pasport_formulara', null=True, verbose_name='№ Паспорт формуляра')),
                ('rgk', models.CharField(db_column='RGK', max_length=100, verbose_name='РГК')),
                ('gorod', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('gruppa_ekspluatacii', models.CharField(max_length=50, verbose_name='группа эксплуатаций')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='Категория')),
                ('norma_rashoda', models.CharField(blank=True, max_length=50, null=True, verbose_name='Норма расхода')),
                ('type_of_mark', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип марки')),
                ('rod_voiska', models.CharField(max_length=50, verbose_name='Род войска')),
                ('voiskovaia_chast', models.CharField(max_length=50, verbose_name='Войсковая часть')),
                ('podrazdelenia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Подразделения')),
                ('mileage', models.IntegerField(blank=True, null=True, verbose_name='Пробег .км')),
                ('tp', models.IntegerField(blank=True, db_column='TP', null=True, verbose_name='ТР')),
                ('cp', models.IntegerField(blank=True, db_column='CP', null=True, verbose_name='СР')),
                ('kp', models.IntegerField(blank=True, db_column='KP', null=True, verbose_name='КР')),
                ('spisanie', models.CharField(blank=True, db_column='Spisanie', max_length=50, null=True, verbose_name='Списание')),
                ('sostoianie', models.CharField(blank=True, db_column='Sostoianie', max_length=255, null=True, verbose_name='Состояние')),
                ('need', models.IntegerField(blank=True, db_column='Need', null=True, verbose_name='Потребность')),
                ('available', models.IntegerField(blank=True, null=True, verbose_name='Имеется')),
                ('shortage', models.IntegerField(blank=True, null=True, verbose_name='Некомплект')),
                ('excess', models.IntegerField(blank=True, null=True, verbose_name='Излишествует')),
                ('verification', models.CharField(max_length=50, verbose_name='Проверка')),
            ],
            options={
                'verbose_name': 'Обьекты ВВТ',
                'verbose_name_plural': 'Обьекты ВВТ',
                'db_table': 'vvt',
                'managed': False,
            },
        ),
    ]
