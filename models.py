# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    active = models.IntegerField()
    title = models.CharField(max_length=50)
    title_visible = models.IntegerField()
    logo = models.CharField(max_length=100)
    logo_visible = models.IntegerField()
    css_header_background_color = models.CharField(max_length=10)
    title_color = models.CharField(max_length=10)
    css_header_text_color = models.CharField(max_length=10)
    css_header_link_color = models.CharField(max_length=10)
    css_header_link_hover_color = models.CharField(max_length=10)
    css_module_background_color = models.CharField(max_length=10)
    css_module_text_color = models.CharField(max_length=10)
    css_module_link_color = models.CharField(max_length=10)
    css_module_link_hover_color = models.CharField(max_length=10)
    css_module_rounded_corners = models.IntegerField()
    css_generic_link_color = models.CharField(max_length=10)
    css_generic_link_hover_color = models.CharField(max_length=10)
    css_save_button_background_color = models.CharField(max_length=10)
    css_save_button_background_hover_color = models.CharField(max_length=10)
    css_save_button_text_color = models.CharField(max_length=10)
    css_delete_button_background_color = models.CharField(max_length=10)
    css_delete_button_background_hover_color = models.CharField(max_length=10)
    css_delete_button_text_color = models.CharField(max_length=10)
    list_filter_dropdown = models.IntegerField()
    related_modal_active = models.IntegerField()
    related_modal_background_color = models.CharField(max_length=10)
    related_modal_rounded_corners = models.IntegerField()
    logo_color = models.CharField(max_length=10)
    recent_actions_visible = models.IntegerField()
    favicon = models.CharField(max_length=100)
    related_modal_background_opacity = models.CharField(max_length=5)
    env_name = models.CharField(max_length=50)
    env_visible_in_header = models.IntegerField()
    env_color = models.CharField(max_length=10)
    env_visible_in_favicon = models.IntegerField()
    related_modal_close_button_visible = models.IntegerField()
    language_chooser_active = models.IntegerField()
    language_chooser_display = models.CharField(max_length=10)
    list_filter_sticky = models.IntegerField()
    form_pagination_sticky = models.IntegerField()
    form_submit_sticky = models.IntegerField()
    css_module_background_selected_color = models.CharField(max_length=10)
    css_module_link_selected_color = models.CharField(max_length=10)
    logo_max_height = models.PositiveSmallIntegerField()
    logo_max_width = models.PositiveSmallIntegerField()
    foldable_apps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class Akb(models.Model):
    akb_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    obiekti_vvt = models.CharField(db_column='Obiekti_vvt', max_length=255)  # Field name made lowercase.
    kem_vidano = models.CharField(db_column='Kem_vidano', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kogda_vidano = models.DateField(db_column='Kogda_vidano', blank=True, null=True)  # Field name made lowercase.
    spisanie = models.CharField(db_column='Spisanie', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'akb'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Avtoshini(models.Model):
    avtoshin_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obiekti_vvt = models.CharField(db_column='Obiekti_vvt', max_length=255)  # Field name made lowercase.
    kem_vidano = models.CharField(db_column='Kem_vidano', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kogda_vidano = models.DateField(blank=True, null=True)
    spisanie = models.CharField(db_column='Spisanie', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'avtoshini'


class AvtoshiniNew(models.Model):
    id_shin = models.AutoField(primary_key=True)
    type_shin = models.CharField(max_length=50)
    id_techniki = models.ForeignKey('Main', models.DO_NOTHING, db_column='id_techniki')
    razmer_shin = models.CharField(max_length=50)
    kolichestvo_shin = models.IntegerField()
    kem_vidano = models.CharField(max_length=50, blank=True, null=True)
    field_nariad_kogda_vidano = models.CharField(db_column='╣_nariad_kogda_vidano', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    data_ustanovki_shini = models.CharField(max_length=50)
    srok_sluzhbi_v_km = models.IntegerField()
    january_2020 = models.IntegerField(db_column='January_2020', blank=True, null=True)  # Field name made lowercase.
    february_2020 = models.IntegerField(db_column='February_2020', blank=True, null=True)  # Field name made lowercase.
    march_2020 = models.IntegerField(db_column='March_2020', blank=True, null=True)  # Field name made lowercase.
    april_2020 = models.IntegerField(db_column='April_2020', blank=True, null=True)  # Field name made lowercase.
    may_2020 = models.IntegerField(db_column='May_2020', blank=True, null=True)  # Field name made lowercase.
    june_2020 = models.IntegerField(db_column='June_2020', blank=True, null=True)  # Field name made lowercase.
    july_2020 = models.IntegerField(db_column='July_2020', blank=True, null=True)  # Field name made lowercase.
    august_2020 = models.IntegerField(db_column='August_2020', blank=True, null=True)  # Field name made lowercase.
    september_2020 = models.IntegerField(db_column='September_2020', blank=True, null=True)  # Field name made lowercase.
    october_2020 = models.IntegerField(db_column='October_2020', blank=True, null=True)  # Field name made lowercase.
    november_2020 = models.IntegerField(db_column='November_2020', blank=True, null=True)  # Field name made lowercase.
    december_2020 = models.IntegerField(db_column='December_2020', blank=True, null=True)  # Field name made lowercase.
    january_2021 = models.IntegerField(db_column='January_2021', blank=True, null=True)  # Field name made lowercase.
    february_2021 = models.IntegerField(db_column='February_2021', blank=True, null=True)  # Field name made lowercase.
    march_2021 = models.IntegerField(db_column='March_2021', blank=True, null=True)  # Field name made lowercase.
    april_2021 = models.IntegerField(db_column='April_2021', blank=True, null=True)  # Field name made lowercase.
    may_2021 = models.IntegerField(db_column='May_2021', blank=True, null=True)  # Field name made lowercase.
    june_2021 = models.IntegerField(db_column='June_2021', blank=True, null=True)  # Field name made lowercase.
    july_2021 = models.IntegerField(db_column='July_2021', blank=True, null=True)  # Field name made lowercase.
    august_2021 = models.IntegerField(db_column='August_2021', blank=True, null=True)  # Field name made lowercase.
    september_2021 = models.IntegerField(db_column='September_2021', blank=True, null=True)  # Field name made lowercase.
    october_2021 = models.IntegerField(db_column='October_2021', blank=True, null=True)  # Field name made lowercase.
    november_2021 = models.IntegerField(db_column='November_2021', blank=True, null=True)  # Field name made lowercase.
    december_2021 = models.IntegerField(db_column='December_2021', blank=True, null=True)  # Field name made lowercase.
    january_2022 = models.IntegerField(db_column='January_2022', blank=True, null=True)  # Field name made lowercase.
    february_2022 = models.IntegerField(db_column='February_2022', blank=True, null=True)  # Field name made lowercase.
    march_2022 = models.IntegerField(db_column='March_2022', blank=True, null=True)  # Field name made lowercase.
    april_2022 = models.IntegerField(db_column='April_2022', blank=True, null=True)  # Field name made lowercase.
    may_2022 = models.IntegerField(db_column='May_2022', blank=True, null=True)  # Field name made lowercase.
    june_2022 = models.IntegerField(db_column='June_2022', blank=True, null=True)  # Field name made lowercase.
    july_2022 = models.IntegerField(db_column='July_2022', blank=True, null=True)  # Field name made lowercase.
    august_2022 = models.IntegerField(db_column='August_2022', blank=True, null=True)  # Field name made lowercase.
    september_2022 = models.IntegerField(db_column='September_2022', blank=True, null=True)  # Field name made lowercase.
    october_2022 = models.IntegerField(db_column='October_2022', blank=True, null=True)  # Field name made lowercase.
    november_2022 = models.IntegerField(db_column='November_2022', blank=True, null=True)  # Field name made lowercase.
    december_2022 = models.IntegerField(db_column='December_2022', blank=True, null=True)  # Field name made lowercase.
    january_2023 = models.IntegerField(db_column='January_2023', blank=True, null=True)  # Field name made lowercase.
    february_2023 = models.IntegerField(db_column='February_2023', blank=True, null=True)  # Field name made lowercase.
    march_2023 = models.IntegerField(db_column='March_2023', blank=True, null=True)  # Field name made lowercase.
    april_2023 = models.IntegerField(db_column='April_2023', blank=True, null=True)  # Field name made lowercase.
    may_2023 = models.IntegerField(db_column='May_2023', blank=True, null=True)  # Field name made lowercase.
    june_2023 = models.IntegerField(db_column='June_2023', blank=True, null=True)  # Field name made lowercase.
    july_2023 = models.IntegerField(db_column='July_2023', blank=True, null=True)  # Field name made lowercase.
    august_2023 = models.IntegerField(db_column='August_2023', blank=True, null=True)  # Field name made lowercase.
    september_2023 = models.IntegerField(db_column='September_2023', blank=True, null=True)  # Field name made lowercase.
    october_2023 = models.IntegerField(db_column='October_2023', blank=True, null=True)  # Field name made lowercase.
    november_2023 = models.IntegerField(db_column='November_2023', blank=True, null=True)  # Field name made lowercase.
    december_2023 = models.IntegerField(db_column='December_2023', blank=True, null=True)  # Field name made lowercase.
    proideno_km_from_beginning = models.IntegerField(blank=True, null=True)
    proideno_km_from_beginning_uchetom_zapasnogo = models.IntegerField(blank=True, null=True)
    ostalos_km_do_spisania = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avtoshini_new'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Goroda(models.Model):
    gorod_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goroda'


class Main(models.Model):
    field_p_p = models.AutoField(db_column='╣_p/p', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100)  # Field name made lowercase.
    rod_voiska = models.CharField(max_length=50)
    gorod = models.CharField(max_length=50)
    field_voinsnkoi_chasti = models.CharField(db_column='╣_voinsnkoi_chasti', max_length=50)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    podrazdelenia = models.CharField(db_column='Podrazdelenia', max_length=50)  # Field name made lowercase.
    osnov_postanovki_tech_na_uchet = models.CharField(db_column='Osnov_postanovki_tech_na_uchet', max_length=255)  # Field name made lowercase.
    marka_avto = models.CharField(db_column='Marka_avto', max_length=50)  # Field name made lowercase.
    voenni_reg_nomer = models.CharField(max_length=50)
    photo_front = models.CharField(max_length=100, blank=True, null=True)
    photo_site = models.CharField(max_length=100, blank=True, null=True)
    photo_back = models.CharField(max_length=100, blank=True, null=True)
    photo_engine = models.CharField(max_length=100, blank=True, null=True)
    photo_trunk = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vid = models.CharField(max_length=50, blank=True, null=True)
    gruppa_ekspluatacii = models.CharField(max_length=50, blank=True, null=True)
    field_shassi = models.CharField(db_column='╣_shassi', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.CharField(db_column='╣_dvigatelia', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_kabini = models.CharField(db_column='╣_kabini', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    god_vipuska = models.TextField(blank=True, null=True)  # This field type is a guess.
    seria_nomer_pasporta = models.CharField(db_column='seria&nomer_pasporta', max_length=50)  # Field renamed to remove unsuitable characters.
    color = models.CharField(max_length=50, blank=True, null=True)
    nomer_svedit_o_reg = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True, null=True)
    january_2020 = models.IntegerField(db_column='January_2020', blank=True, null=True)  # Field name made lowercase.
    february_2020 = models.IntegerField(db_column='February_2020', blank=True, null=True)  # Field name made lowercase.
    march_2020 = models.IntegerField(db_column='March_2020', blank=True, null=True)  # Field name made lowercase.
    april_2020 = models.IntegerField(db_column='April_2020', blank=True, null=True)  # Field name made lowercase.
    may_2020 = models.IntegerField(db_column='May_2020', blank=True, null=True)  # Field name made lowercase.
    june_2020 = models.IntegerField(db_column='June_2020', blank=True, null=True)  # Field name made lowercase.
    july_2020 = models.IntegerField(db_column='July_2020', blank=True, null=True)  # Field name made lowercase.
    august_2020 = models.IntegerField(db_column='August_2020', blank=True, null=True)  # Field name made lowercase.
    september_2020 = models.IntegerField(db_column='September_2020', blank=True, null=True)  # Field name made lowercase.
    october_2020 = models.IntegerField(db_column='October_2020', blank=True, null=True)  # Field name made lowercase.
    november_2020 = models.IntegerField(db_column='November_2020', blank=True, null=True)  # Field name made lowercase.
    december_2020 = models.IntegerField(db_column='December_2020', blank=True, null=True)  # Field name made lowercase.
    january_2021 = models.IntegerField(db_column='January_2021', blank=True, null=True)  # Field name made lowercase.
    february_2021 = models.IntegerField(db_column='February_2021', blank=True, null=True)  # Field name made lowercase.
    march_2021 = models.IntegerField(db_column='March_2021', blank=True, null=True)  # Field name made lowercase.
    april_2021 = models.IntegerField(db_column='April_2021', blank=True, null=True)  # Field name made lowercase.
    may_2021 = models.IntegerField(db_column='May_2021', blank=True, null=True)  # Field name made lowercase.
    june_2021 = models.IntegerField(db_column='June_2021', blank=True, null=True)  # Field name made lowercase.
    july_2021 = models.IntegerField(db_column='July_2021', blank=True, null=True)  # Field name made lowercase.
    august_2021 = models.IntegerField(db_column='August_2021', blank=True, null=True)  # Field name made lowercase.
    september_2021 = models.IntegerField(db_column='September_2021', blank=True, null=True)  # Field name made lowercase.
    october_2021 = models.IntegerField(db_column='October_2021', blank=True, null=True)  # Field name made lowercase.
    november_2021 = models.IntegerField(db_column='November_2021', blank=True, null=True)  # Field name made lowercase.
    december_2021 = models.IntegerField(db_column='December_2021', blank=True, null=True)  # Field name made lowercase.
    speedometer_01_01_2022 = models.IntegerField(blank=True, null=True)
    videleno_motoresurs_na_year = models.IntegerField()
    january_2022 = models.IntegerField(db_column='January_2022', blank=True, null=True)  # Field name made lowercase.
    february_2022 = models.IntegerField(db_column='February_2022', blank=True, null=True)  # Field name made lowercase.
    march_2022 = models.IntegerField(db_column='March_2022', blank=True, null=True)  # Field name made lowercase.
    april_2022 = models.IntegerField(db_column='April_2022', blank=True, null=True)  # Field name made lowercase.
    may_2022 = models.IntegerField(db_column='May_2022', blank=True, null=True)  # Field name made lowercase.
    june_2022 = models.IntegerField(db_column='June_2022', blank=True, null=True)  # Field name made lowercase.
    july_2022 = models.IntegerField(db_column='July_2022', blank=True, null=True)  # Field name made lowercase.
    august_2022 = models.IntegerField(db_column='August_2022', blank=True, null=True)  # Field name made lowercase.
    september_2022 = models.IntegerField(db_column='September_2022', blank=True, null=True)  # Field name made lowercase.
    october_2022 = models.IntegerField(db_column='October_2022', blank=True, null=True)  # Field name made lowercase.
    november_2022 = models.IntegerField(db_column='November_2022', blank=True, null=True)  # Field name made lowercase.
    december_2022 = models.IntegerField(db_column='December_2022', blank=True, null=True)  # Field name made lowercase.
    january_2023 = models.IntegerField(db_column='January_2023', blank=True, null=True)  # Field name made lowercase.
    february_2023 = models.IntegerField(db_column='February_2023', blank=True, null=True)  # Field name made lowercase.
    march_2023 = models.IntegerField(db_column='March_2023', blank=True, null=True)  # Field name made lowercase.
    april_2023 = models.IntegerField(db_column='April_2023', blank=True, null=True)  # Field name made lowercase.
    may_2023 = models.IntegerField(db_column='May_2023', blank=True, null=True)  # Field name made lowercase.
    june_2023 = models.IntegerField(db_column='June_2023', blank=True, null=True)  # Field name made lowercase.
    july_2023 = models.IntegerField(db_column='July_2023', blank=True, null=True)  # Field name made lowercase.
    august_2023 = models.IntegerField(db_column='August_2023', blank=True, null=True)  # Field name made lowercase.
    september_2023 = models.IntegerField(db_column='September_2023', blank=True, null=True)  # Field name made lowercase.
    october_2023 = models.IntegerField(db_column='October_2023', blank=True, null=True)  # Field name made lowercase.
    november_2023 = models.IntegerField(db_column='November_2023', blank=True, null=True)  # Field name made lowercase.
    december_2023 = models.IntegerField(db_column='December_2023', blank=True, null=True)  # Field name made lowercase.
    izrashodovano_s_nachalo_year = models.IntegerField(blank=True, null=True)
    ostatok_resursov_do_konca_year = models.IntegerField(blank=True, null=True)
    mileage_from_beginning = models.IntegerField(blank=True, null=True)
    tech_sostoianie = models.CharField(db_column='Tech_Sostoianie', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vid_and_data_remonta = models.CharField(max_length=255, blank=True, null=True)
    primechanie = models.CharField(max_length=1000, blank=True, null=True)
    motoresurs_to_1 = models.IntegerField(blank=True, null=True)
    motoresurs_to_2 = models.IntegerField(blank=True, null=True)
    ostalos_motoresurs_tp = models.IntegerField(db_column='ostalos_motoresurs_TP', blank=True, null=True)  # Field name made lowercase.
    ostalos_motoresurs_cp = models.IntegerField(db_column='ostalos_motoresurs_CP', blank=True, null=True)  # Field name made lowercase.
    ostalos_motoresurs_kp = models.IntegerField(db_column='ostalos_motoresurs_KP', blank=True, null=True)  # Field name made lowercase.
    ostalos_motoresurs_spisanie = models.IntegerField(blank=True, null=True)
    type_akb = models.CharField(max_length=50, blank=True, null=True)
    kolichestvo_akb = models.IntegerField(blank=True, null=True)
    kev_vidano = models.CharField(max_length=50, blank=True, null=True)
    field_nariad_kogda_vidano = models.CharField(db_column='╣_nariad_kogda_vidano', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    srok_sluzhbi_akb = models.IntegerField(blank=True, null=True)
    data_ustanovki_akb = models.DateField(blank=True, null=True)
    data_spisania_akb_po_godam = models.DateField(blank=True, null=True)
    srok_sluzhbi_akb_v_km_do_spisania = models.IntegerField(blank=True, null=True)
    akb_january_2020 = models.IntegerField(db_column='Akb_January_2020', blank=True, null=True)  # Field name made lowercase.
    akb_february_2020 = models.IntegerField(db_column='Akb_February_2020', blank=True, null=True)  # Field name made lowercase.
    akb_march_2020 = models.IntegerField(db_column='Akb_March_2020', blank=True, null=True)  # Field name made lowercase.
    akb_april_2020 = models.IntegerField(db_column='Akb_April_2020', blank=True, null=True)  # Field name made lowercase.
    akb_may_2020 = models.IntegerField(db_column='Akb_May_2020', blank=True, null=True)  # Field name made lowercase.
    akb_june_2020 = models.IntegerField(db_column='Akb_June_2020', blank=True, null=True)  # Field name made lowercase.
    akb_july_2020 = models.IntegerField(db_column='Akb_July_2020', blank=True, null=True)  # Field name made lowercase.
    akb_august_2020 = models.IntegerField(db_column='Akb_August_2020', blank=True, null=True)  # Field name made lowercase.
    akb_september_2020 = models.IntegerField(db_column='Akb_September_2020', blank=True, null=True)  # Field name made lowercase.
    akb_october_2020 = models.IntegerField(db_column='Akb_October_2020', blank=True, null=True)  # Field name made lowercase.
    akb_november_2020 = models.IntegerField(db_column='Akb_November_2020', blank=True, null=True)  # Field name made lowercase.
    akb_december_2020 = models.IntegerField(db_column='Akb_December_2020', blank=True, null=True)  # Field name made lowercase.
    akb_january_2021 = models.IntegerField(db_column='Akb_January_2021', blank=True, null=True)  # Field name made lowercase.
    akb_february_2021 = models.IntegerField(db_column='Akb_February_2021', blank=True, null=True)  # Field name made lowercase.
    akb_march_2021 = models.IntegerField(db_column='Akb_March_2021', blank=True, null=True)  # Field name made lowercase.
    akb_april_2021 = models.IntegerField(db_column='Akb_April_2021', blank=True, null=True)  # Field name made lowercase.
    akb_may_2021 = models.IntegerField(db_column='Akb_May_2021', blank=True, null=True)  # Field name made lowercase.
    akb_june_2021 = models.IntegerField(db_column='Akb_June_2021', blank=True, null=True)  # Field name made lowercase.
    akb_july_2021 = models.IntegerField(db_column='Akb_July_2021', blank=True, null=True)  # Field name made lowercase.
    akb_august_2021 = models.IntegerField(db_column='Akb_August_2021', blank=True, null=True)  # Field name made lowercase.
    akb_september_2021 = models.IntegerField(db_column='Akb_September_2021', blank=True, null=True)  # Field name made lowercase.
    akb_october_2021 = models.IntegerField(db_column='Akb_October_2021', blank=True, null=True)  # Field name made lowercase.
    akb_november_2021 = models.IntegerField(db_column='Akb_November_2021', blank=True, null=True)  # Field name made lowercase.
    akb_december_2021 = models.IntegerField(db_column='Akb_December_2021', blank=True, null=True)  # Field name made lowercase.
    akb_january_2022 = models.IntegerField(db_column='Akb_January_2022', blank=True, null=True)  # Field name made lowercase.
    akb_february_2022 = models.IntegerField(db_column='Akb_February_2022', blank=True, null=True)  # Field name made lowercase.
    akb_march_2022 = models.IntegerField(db_column='Akb_March_2022', blank=True, null=True)  # Field name made lowercase.
    akb_april_2022 = models.IntegerField(db_column='Akb_April_2022', blank=True, null=True)  # Field name made lowercase.
    akb_may_2022 = models.IntegerField(db_column='Akb_May_2022', blank=True, null=True)  # Field name made lowercase.
    akb_june_2022 = models.IntegerField(db_column='Akb_June_2022', blank=True, null=True)  # Field name made lowercase.
    akb_july_2022 = models.IntegerField(db_column='Akb_July_2022', blank=True, null=True)  # Field name made lowercase.
    akb_august_2022 = models.IntegerField(db_column='Akb_August_2022', blank=True, null=True)  # Field name made lowercase.
    akb_september_2022 = models.IntegerField(db_column='Akb_September_2022', blank=True, null=True)  # Field name made lowercase.
    akb_october_2022 = models.IntegerField(db_column='Akb_October_2022', blank=True, null=True)  # Field name made lowercase.
    akb_november_2022 = models.IntegerField(db_column='Akb_November_2022', blank=True, null=True)  # Field name made lowercase.
    akb_december_2022 = models.IntegerField(db_column='Akb_December_2022', blank=True, null=True)  # Field name made lowercase.
    akb_january_2023 = models.IntegerField(db_column='Akb_January_2023', blank=True, null=True)  # Field name made lowercase.
    akb_february_2023 = models.IntegerField(db_column='Akb_February_2023', blank=True, null=True)  # Field name made lowercase.
    akb_march_2023 = models.IntegerField(db_column='Akb_March_2023', blank=True, null=True)  # Field name made lowercase.
    akb_april_2023 = models.IntegerField(db_column='Akb_April_2023', blank=True, null=True)  # Field name made lowercase.
    akb_may_2023 = models.IntegerField(db_column='Akb_May_2023', blank=True, null=True)  # Field name made lowercase.
    akb_june_2023 = models.IntegerField(db_column='Akb_June_2023', blank=True, null=True)  # Field name made lowercase.
    akb_july_2023 = models.IntegerField(db_column='Akb_July_2023', blank=True, null=True)  # Field name made lowercase.
    akb_august_2023 = models.IntegerField(db_column='Akb_August_2023', blank=True, null=True)  # Field name made lowercase.
    akb_september_2023 = models.IntegerField(db_column='Akb_September_2023', blank=True, null=True)  # Field name made lowercase.
    akb_october_2023 = models.IntegerField(db_column='Akb_October_2023', blank=True, null=True)  # Field name made lowercase.
    akb_november_2023 = models.IntegerField(db_column='Akb_November_2023', blank=True, null=True)  # Field name made lowercase.
    akb_december_2023 = models.IntegerField(db_column='Akb_December_2023', blank=True, null=True)  # Field name made lowercase.
    proideno_km_from_beginning_akb = models.IntegerField(blank=True, null=True)
    akb_ostalos_km_do_spisania = models.IntegerField(db_column='Akb_ostalos_km_do_spisania', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main'


class ObiektiVvt(models.Model):
    id_vvt = models.AutoField(primary_key=True)
    marka_vvt = models.CharField(db_column='Marka_VVT', max_length=50)  # Field name made lowercase.
    voenni_reg_nomer = models.CharField(max_length=50, blank=True, null=True)
    god_vipuska = models.TextField(blank=True, null=True)  # This field type is a guess.
    field_shassi = models.IntegerField(db_column='╣_shassi', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.IntegerField(db_column='╣_dvigatelia', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_pasport_formulara = models.IntegerField(db_column='╣_pasport_formulara', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100)  # Field name made lowercase.
    gorod = models.CharField(max_length=50, blank=True, null=True)
    gruppa_ekspluatacii = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True, null=True)
    norma_rashoda = models.CharField(max_length=50, blank=True, null=True)
    type_of_mark = models.CharField(max_length=50, blank=True, null=True)
    rod_voiska = models.CharField(max_length=50)
    voiskovaia_chast = models.CharField(max_length=50)
    podrazdelenia = models.CharField(max_length=50, blank=True, null=True)
    tp = models.IntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    cp = models.IntegerField(db_column='CP', blank=True, null=True)  # Field name made lowercase.
    kp = models.IntegerField(db_column='KP', blank=True, null=True)  # Field name made lowercase.
    spisanie = models.CharField(db_column='Spisanie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sostoianie = models.CharField(db_column='Sostoianie', max_length=255, blank=True, null=True)  # Field name made lowercase.
    need = models.IntegerField(db_column='Need', blank=True, null=True)  # Field name made lowercase.
    available = models.IntegerField(blank=True, null=True)
    shortage = models.IntegerField(blank=True, null=True)
    excess = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obiekti_vvt'


class Peremeshenie(models.Model):
    premesh_id = models.AutoField(primary_key=True)
    field_prikaza_nomer_date_field = models.IntegerField(db_column='╣_prikaza(nomer, date)')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    obiekti_vvt = models.CharField(db_column='Obiekti_vvt', max_length=50)  # Field name made lowercase.
    voiskovaia_chast = models.CharField(db_column='Voiskovaia_chast', max_length=50)  # Field name made lowercase.
    podrazdelenia = models.CharField(db_column='Podrazdelenia', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peremeshenie'


class Podrazdelenia(models.Model):
    id_podrazdelenia = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'podrazdelenia'


class VoiskovieChasti(models.Model):
    id_voiskovie_chasti = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    gorod = models.CharField(db_column='Gorod', max_length=50)  # Field name made lowercase.
    rgk = models.CharField(db_column='RGK', max_length=100)  # Field name made lowercase.
    rod_voiska = models.CharField(db_column='Rod_voiska', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voiskovie_chasti'


class Vvt(models.Model):
    id_vvt = models.AutoField(primary_key=True)
    marka_vvt = models.CharField(db_column='Marka_VVT', max_length=50)  # Field name made lowercase.
    nomer_znak = models.CharField(max_length=50, blank=True, null=True)
    god_vipuska = models.TextField(blank=True, null=True)  # This field type is a guess.
    color = models.CharField(max_length=50, blank=True, null=True)
    field_shassi = models.CharField(db_column='╣_shassi', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_dvigatelia = models.CharField(db_column='╣_dvigatelia', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_seria_pasporta = models.CharField(db_column='╣_seria_pasporta', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_kuzova = models.CharField(db_column='╣_kuzova', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_tech_talon = models.CharField(db_column='╣_tech_talon', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    rgk = models.CharField(db_column='RGK', max_length=100)  # Field name made lowercase.
    garnizon = models.CharField(max_length=100, blank=True, null=True)
    gorod = models.CharField(max_length=50, blank=True, null=True)
    gruppa_ekspluatacii = models.CharField(max_length=50, blank=True, null=True)
    vid = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    norma_rashoda = models.CharField(max_length=50, blank=True, null=True)
    type_of_mark = models.CharField(max_length=50, blank=True, null=True)
    rod_voiska = models.CharField(max_length=50, blank=True, null=True)
    voiskovaia_chast = models.CharField(max_length=50)
    podrazdelenia = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    tp = models.IntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    cp = models.IntegerField(db_column='CP', blank=True, null=True)  # Field name made lowercase.
    kp = models.IntegerField(db_column='KP', blank=True, null=True)  # Field name made lowercase.
    primechanie = models.CharField(db_column='Primechanie', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sostoianie = models.CharField(db_column='Sostoianie', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vvt'
