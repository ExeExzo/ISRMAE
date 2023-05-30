# Generated by Django 4.0.6 on 2022-09-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_vvt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('field_p_p', models.AutoField(db_column='№_p/p', primary_key=True, serialize=False)),
                ('rgk', models.CharField(db_column='RGK', max_length=100)),
                ('rod_voiska', models.CharField(max_length=50)),
                ('gorod', models.CharField(max_length=50)),
                ('field_voinsnkoi_chasti', models.CharField(db_column='№_voinsnkoi_chasti', max_length=50)),
                ('podrazdelenia', models.CharField(db_column='Podrazdelenia', max_length=50)),
                ('osnov_postanovki_tech_na_uchet', models.CharField(db_column='Osnov_postanovki_tech_na_uchet', max_length=255)),
                ('marka_avto', models.CharField(db_column='Marka_avto', max_length=50)),
                ('voenni_reg_nomer', models.CharField(max_length=50)),
                ('type', models.CharField(db_column='Type', max_length=50)),
                ('gruppa_ekspluatacii', models.CharField(max_length=50)),
                ('field_shassi', models.CharField(blank=True, db_column='№_shassi', max_length=50, null=True)),
                ('field_dvigatelia', models.CharField(blank=True, db_column='№_dvigatelia', max_length=50, null=True)),
                ('field_kabini', models.CharField(blank=True, db_column='№_kabini', max_length=50, null=True)),
                ('god_vipuska', models.TextField()),
                ('seria_nomer_pasporta', models.CharField(db_column='seria&nomer_pasporta', max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('nomer_svedit_o_reg', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('speedometer_na_01_01_2022', models.IntegerField(db_column='speedometer_na_01.01.2022')),
                ('videleno_motoresurs_na_year', models.IntegerField()),
                ('izrashodovano_za_month', models.IntegerField()),
                ('izrashodovano_s_nachalo_year', models.IntegerField()),
                ('ostatok_resursov_do_konca_year', models.IntegerField()),
                ('mileage_from_beginning', models.IntegerField()),
                ('tech_sostoianie', models.CharField(db_column='Tech_Sostoianie', max_length=255)),
                ('vid_and_data_remonta', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'AITU',
                'verbose_name_plural': 'AITU',
                'db_table': 'main',
                'managed': False,
            },
        ),
    ]
