# Generated by Django 4.0.5 on 2022-07-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vvt',
            fields=[
                ('id_vvt', models.AutoField(primary_key=True, serialize=False)),
                ('marka_vvt', models.CharField(db_column='Marka_VVT', max_length=50)),
                ('voenni_reg_nomer', models.CharField(blank=True, max_length=50, null=True)),
                ('god_vipuska', models.DateField(blank=True, null=True)),
                ('field_shassi', models.IntegerField(blank=True, db_column='╣_shassi', null=True)),
                ('field_dvigatelia', models.IntegerField(blank=True, db_column='╣_dvigatelia', null=True)),
                ('field_pasport_formulara', models.IntegerField(blank=True, db_column='╣_pasport_formulara', null=True)),
                ('rgk', models.CharField(db_column='RGK', max_length=100)),
                ('gorod', models.CharField(blank=True, max_length=50, null=True)),
                ('gruppa_ekspluatacii', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('norma_rashoda', models.CharField(blank=True, max_length=50, null=True)),
                ('type_of_mark', models.CharField(blank=True, max_length=50, null=True)),
                ('rod_voiska', models.CharField(max_length=50)),
                ('voiskovaia_chast', models.CharField(max_length=50)),
                ('podrazdelenia', models.CharField(blank=True, max_length=50, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('tp', models.IntegerField(blank=True, db_column='TP', null=True)),
                ('cp', models.IntegerField(blank=True, db_column='CP', null=True)),
                ('kp', models.IntegerField(blank=True, db_column='KP', null=True)),
                ('spisanie', models.CharField(blank=True, db_column='Spisanie', max_length=50, null=True)),
                ('sostoianie', models.CharField(blank=True, db_column='Sostoianie', max_length=255, null=True)),
                ('need', models.IntegerField(blank=True, db_column='Need', null=True)),
                ('available', models.IntegerField(blank=True, null=True)),
                ('shortage', models.IntegerField(blank=True, null=True)),
                ('excess', models.IntegerField(blank=True, null=True)),
                ('verification', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'vvt',
                'managed': False,
            },
        ),
    ]
