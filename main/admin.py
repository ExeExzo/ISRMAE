from django.contrib import admin
from .models import *
from django.shortcuts import redirect

from django.utils.safestring import mark_safe
# Register your models here.


# Admin themes: https://pypi.org/project/django-admin-interface/

class AkbAdmin(admin.ModelAdmin):
    list_display = ['akb_id','name','obiekti_vvt','kem_vidano','kogda_vidano','spisanie']
    list_display_links = ('akb_id','name','obiekti_vvt')
    search_fields = ('akb_id','name','obiekti_vvt','kem_vidano','kogda_vidano','spisanie')


# class AkbNewAdmin(admin.ModelAdmin):
#     list_display = ['type_akb','kolichestvo_akb','field_p_p','kev_vidano','field_nariad_kogda_vidano','srok_sluzhbi','data_ustanovki_akb','data_spisania_akb_po_godam','srok_sluzhbi_v_km_do_spisania','january','february','march','april','may','june','july','august','september','october','november','december','proideno_km_from_beginning','ostalos_km_do_spisania']
#     list_display_links = ('type_akb','kolichestvo_akb','field_p_p','kev_vidano','field_nariad_kogda_vidano','srok_sluzhbi','data_ustanovki_akb','data_spisania_akb_po_godam','srok_sluzhbi_v_km_do_spisania','january','february','march','april','may','june','july','august','september','october','november','december','proideno_km_from_beginning','ostalos_km_do_spisania')
#     search_fields = ('type_akb','kolichestvo_akb','field_p_p','kev_vidano','field_nariad_kogda_vidano','srok_sluzhbi','data_ustanovki_akb','data_spisania_akb_po_godam','srok_sluzhbi_v_km_do_spisania','january','february','march','april','may','june','july','august','september','october','november','december','proideno_km_from_beginning','ostalos_km_do_spisania')
    

class AvtoshiniAdmin(admin.ModelAdmin):
    list_display = ['avtoshin_id','name','type','obiekti_vvt','kem_vidano','kogda_vidano','spisanie']
    list_display_links = ('avtoshin_id','name','obiekti_vvt')
    search_fields = ('avtoshin_id','name','type','obiekti_vvt','kem_vidano','kogda_vidano','spisanie')


class AvtoshiniNewAdmin(admin.ModelAdmin):
    list_display = ['id_shin','type_shin', 'get_id','razmer_shin','kolichestvo_shin','kem_vidano','field_nariad_kogda_vidano','data_ustanovki_shini','srok_sluzhbi_v_km','january_2020','february_2020','march_2020','april_2020','may_2020','june_2020','july_2020','august_2020','september_2020','october_2020','november_2020','december_2020','january_2021','february_2021','march_2021','april_2021','may_2021','june_2021','july_2021','august_2021','september_2021','october_2021','november_2021','december_2021','january_2022','february_2022','march_2022','april_2022','may_2022','june_2022','july_2022','august_2022','september_2022','october_2022','november_2022','december_2022','january_2023','february_2023','march_2023','april_2023','may_2023','june_2023','july_2023','august_2023','september_2023','october_2023','november_2023','december_2023','proideno_km_from_beginning','proideno_km_from_beginning_uchetom_zapasnogo','ostalos_km_do_spisania']
    list_display_links = ('id_shin','type_shin', 'get_id','razmer_shin','kolichestvo_shin','kem_vidano','field_nariad_kogda_vidano','data_ustanovki_shini','srok_sluzhbi_v_km','january_2020','february_2020','march_2020','april_2020','may_2020','june_2020','july_2020','august_2020','september_2020','october_2020','november_2020','december_2020','january_2021','february_2021','march_2021','april_2021','may_2021','june_2021','july_2021','august_2021','september_2021','october_2021','november_2021','december_2021','january_2022','february_2022','march_2022','april_2022','may_2022','june_2022','july_2022','august_2022','september_2022','october_2022','november_2022','december_2022','january_2023','february_2023','march_2023','april_2023','may_2023','june_2023','july_2023','august_2023','september_2023','october_2023','november_2023','december_2023','proideno_km_from_beginning','proideno_km_from_beginning_uchetom_zapasnogo','ostalos_km_do_spisania')
    search_fields = ('id_shin','type_shin', 'get_id','razmer_shin','kolichestvo_shin','kem_vidano','field_nariad_kogda_vidano','data_ustanovki_shini','srok_sluzhbi_v_km','january_2020','february_2020','march_2020','april_2020','may_2020','june_2020','july_2020','august_2020','september_2020','october_2020','november_2020','december_2020','january_2021','february_2021','march_2021','april_2021','may_2021','june_2021','july_2021','august_2021','september_2021','october_2021','november_2021','december_2021','january_2022','february_2022','march_2022','april_2022','may_2022','june_2022','july_2022','august_2022','september_2022','october_2022','november_2022','december_2022','january_2023','february_2023','march_2023','april_2023','may_2023','june_2023','july_2023','august_2023','september_2023','october_2023','november_2023','december_2023','proideno_km_from_beginning','proideno_km_from_beginning_uchetom_zapasnogo','ostalos_km_do_spisania')
    def get_id(self,obj):
        return obj.id_techniki.field_p_p

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/carDetails/{obj.id_techniki.field_p_p}')

    def response_change(self, request, obj):
        return redirect(f'/carDetails/{obj.id_techniki.field_p_p}')
        


class GorodaAdmin(admin.ModelAdmin):
    list_display = ['gorod_id','name']
    list_display_links = ('gorod_id','name')
    search_fields = ('gorod_id','name')

class MainAdmin(admin.ModelAdmin):
    type_akb = models.CharField(max_length=50, blank=True, null=True)
    list_display = ['field_p_p','rgk','rod_voiska','gorod','field_voinsnkoi_chasti','podrazdelenia','osnov_postanovki_tech_na_uchet','marka_avto','voenni_reg_nomer','get_html_photo_f','get_html_photo_s','get_html_photo_b','get_html_photo_e','get_html_photo_t','type', 'vid', 'gruppa_ekspluatacii','field_shassi','field_dvigatelia','field_kabini','god_vipuska','seria_nomer_pasporta','color','nomer_svedit_o_reg','category', 'january_2020', 'february_2020', 'march_2020', 'april_2020', 'may_2020', 'june_2020', 'july_2020', 'august_2020', 'september_2020', 'october_2020', 'november_2020', 'december_2020', 'january_2021', 'february_2021', 'march_2021', 'april_2021', 'may_2021', 'june_2021', 'july_2021', 'august_2021', 'september_2021', 'october_2021', 'november_2021', 'december_2021', 'speedometer_01_01_2022','videleno_motoresurs_na_year','january_2022','february_2022','march_2022','april_2022','may_2022','june_2022','july_2022','august_2022','september_2022','october_2022','november_2022','december_2022', 'january_2023', 'february_2023', 'march_2023', 'april_2023', 'may_2023', 'june_2023', 'july_2023', 'august_2023', 'september_2023', 'october_2023', 'november_2023', 'december_2023','izrashodovano_s_nachalo_year','ostatok_resursov_do_konca_year','mileage_from_beginning','tech_sostoianie','vid_and_data_remonta', 'primechanie','motoresurs_to_1','motoresurs_to_2','ostalos_motoresurs_tp','ostalos_motoresurs_cp','ostalos_motoresurs_kp','ostalos_motoresurs_spisanie','type_akb','kolichestvo_akb','kev_vidano','field_nariad_kogda_vidano','srok_sluzhbi_akb','data_ustanovki_akb','data_spisania_akb_po_godam','srok_sluzhbi_akb_v_km_do_spisania','akb_january_2020','akb_february_2020','akb_march_2020','akb_april_2020','akb_may_2020','akb_june_2020','akb_july_2020','akb_august_2020','akb_september_2020','akb_october_2020','akb_november_2020','akb_december_2020','akb_january_2021','akb_february_2021','akb_march_2021','akb_april_2021','akb_may_2021','akb_june_2021','akb_july_2021','akb_august_2021','akb_september_2021','akb_october_2021','akb_november_2021','akb_december_2021','akb_january_2022','akb_february_2022','akb_march_2022','akb_april_2022','akb_may_2022','akb_june_2022','akb_july_2022','akb_august_2022','akb_september_2022','akb_october_2022','akb_november_2022','akb_december_2022','akb_january_2023','akb_february_2023','akb_march_2023','akb_april_2023','akb_may_2023','akb_june_2023','akb_july_2023','akb_august_2023','akb_september_2023','akb_october_2023','akb_november_2023','akb_december_2023','proideno_km_from_beginning_akb','akb_ostalos_km_do_spisania']
    list_display_links = ('field_p_p','rgk','rod_voiska','gorod','field_voinsnkoi_chasti','podrazdelenia','osnov_postanovki_tech_na_uchet','marka_avto','voenni_reg_nomer','get_html_photo_f','get_html_photo_s','get_html_photo_b','get_html_photo_e','get_html_photo_t','type', 'vid', 'gruppa_ekspluatacii','field_shassi','field_dvigatelia','field_kabini','god_vipuska','seria_nomer_pasporta','color','nomer_svedit_o_reg','category', 'january_2020', 'february_2020', 'march_2020', 'april_2020', 'may_2020', 'june_2020', 'july_2020', 'august_2020', 'september_2020', 'october_2020', 'november_2020', 'december_2020', 'january_2021', 'february_2021', 'march_2021', 'april_2021', 'may_2021', 'june_2021', 'july_2021', 'august_2021', 'september_2021', 'october_2021', 'november_2021', 'december_2021', 'speedometer_01_01_2022','videleno_motoresurs_na_year','january_2022','february_2022','march_2022','april_2022','may_2022','june_2022','july_2022','august_2022','september_2022','october_2022','november_2022','december_2022', 'january_2023', 'february_2023', 'march_2023', 'april_2023', 'may_2023', 'june_2023', 'july_2023', 'august_2023', 'september_2023', 'october_2023', 'november_2023', 'december_2023','izrashodovano_s_nachalo_year','ostatok_resursov_do_konca_year','mileage_from_beginning','tech_sostoianie','vid_and_data_remonta', 'primechanie','motoresurs_to_1','motoresurs_to_2','ostalos_motoresurs_tp','ostalos_motoresurs_cp','ostalos_motoresurs_kp','ostalos_motoresurs_spisanie','type_akb','kolichestvo_akb','kev_vidano','field_nariad_kogda_vidano','srok_sluzhbi_akb','data_ustanovki_akb','data_spisania_akb_po_godam','srok_sluzhbi_akb_v_km_do_spisania','akb_january_2020','akb_february_2020','akb_march_2020','akb_april_2020','akb_may_2020','akb_june_2020','akb_july_2020','akb_august_2020','akb_september_2020','akb_october_2020','akb_november_2020','akb_december_2020','akb_january_2021','akb_february_2021','akb_march_2021','akb_april_2021','akb_may_2021','akb_june_2021','akb_july_2021','akb_august_2021','akb_september_2021','akb_october_2021','akb_november_2021','akb_december_2021','akb_january_2022','akb_february_2022','akb_march_2022','akb_april_2022','akb_may_2022','akb_june_2022','akb_july_2022','akb_august_2022','akb_september_2022','akb_october_2022','akb_november_2022','akb_december_2022','akb_january_2023','akb_february_2023','akb_march_2023','akb_april_2023','akb_may_2023','akb_june_2023','akb_july_2023','akb_august_2023','akb_september_2023','akb_october_2023','akb_november_2023','akb_december_2023','proideno_km_from_beginning_akb','akb_ostalos_km_do_spisania')
    search_fields = ('field_p_p','rgk','rod_voiska','gorod','field_voinsnkoi_chasti','podrazdelenia','osnov_postanovki_tech_na_uchet','marka_avto','voenni_reg_nomer','get_html_photo_f','get_html_photo_s','get_html_photo_b','get_html_photo_e','get_html_photo_t','type', 'vid', 'gruppa_ekspluatacii','field_shassi','field_dvigatelia','field_kabini','god_vipuska','seria_nomer_pasporta','color','nomer_svedit_o_reg','category', 'january_2020', 'february_2020', 'march_2020', 'april_2020', 'may_2020', 'june_2020', 'july_2020', 'august_2020', 'september_2020', 'october_2020', 'november_2020', 'december_2020', 'january_2021', 'february_2021', 'march_2021', 'april_2021', 'may_2021', 'june_2021', 'july_2021', 'august_2021', 'september_2021', 'october_2021', 'november_2021', 'december_2021', 'speedometer_01_01_2022','videleno_motoresurs_na_year','january_2022','february_2022','march_2022','april_2022','may_2022','june_2022','july_2022','august_2022','september_2022','october_2022','november_2022','december_2022', 'january_2023', 'february_2023', 'march_2023', 'april_2023', 'may_2023', 'june_2023', 'july_2023', 'august_2023', 'september_2023', 'october_2023', 'november_2023', 'december_2023','izrashodovano_s_nachalo_year','ostatok_resursov_do_konca_year','mileage_from_beginning','tech_sostoianie','vid_and_data_remonta', 'primechanie','motoresurs_to_1','motoresurs_to_2','ostalos_motoresurs_tp','ostalos_motoresurs_cp','ostalos_motoresurs_kp','ostalos_motoresurs_spisanie','type_akb','kolichestvo_akb','kev_vidano','field_nariad_kogda_vidano','srok_sluzhbi_akb','data_ustanovki_akb','data_spisania_akb_po_godam','srok_sluzhbi_akb_v_km_do_spisania','akb_january_2020','akb_february_2020','akb_march_2020','akb_april_2020','akb_may_2020','akb_june_2020','akb_july_2020','akb_august_2020','akb_september_2020','akb_october_2020','akb_november_2020','akb_december_2020','akb_january_2021','akb_february_2021','akb_march_2021','akb_april_2021','akb_may_2021','akb_june_2021','akb_july_2021','akb_august_2021','akb_september_2021','akb_october_2021','akb_november_2021','akb_december_2021','akb_january_2022','akb_february_2022','akb_march_2022','akb_april_2022','akb_may_2022','akb_june_2022','akb_july_2022','akb_august_2022','akb_september_2022','akb_october_2022','akb_november_2022','akb_december_2022','akb_january_2023','akb_february_2023','akb_march_2023','akb_april_2023','akb_may_2023','akb_june_2023','akb_july_2023','akb_august_2023','akb_september_2023','akb_october_2023','akb_november_2023','akb_december_2023','proideno_km_from_beginning_akb','akb_ostalos_km_do_spisania')

    def response_add(self, request, obj, post_url_continue=None):

        return redirect(f'/carDetails/{obj.field_p_p}')

    def response_change(self, request, obj):
        return redirect(f'/carDetails/{obj.field_p_p}')

    def get_html_photo_f(self, object):
        if object.photo_front:
            return mark_safe(f"<img src='{object.photo_front.url}' width='130'>")

    get_html_photo_f.short_description = "Фото спереди"

    def get_html_photo_s(self, object):
        if object.photo_site:
            return mark_safe(f"<img src='{object.photo_site.url}' width='130'>")

    get_html_photo_s.short_description = "Фото сбоку"

    def get_html_photo_b(self, object):
        if object.photo_back:
            return mark_safe(f"<img src='{object.photo_back.url}' width='130'>")

    get_html_photo_b.short_description = "Фото сзади"

    def get_html_photo_e(self, object):
        if object.photo_engine:
            return mark_safe(f"<img src='{object.photo_engine.url}' width='130'>")

    get_html_photo_e.short_description = "Фото двигателя"

    def get_html_photo_t(self, object):
        if object.photo_trunk:
            return mark_safe(f"<img src='{object.photo_trunk.url}' width='130'>")

    get_html_photo_t.short_description = "Фото АКБ"

    


class ObiektiVvtAdmin(admin.ModelAdmin):
    list_display = ['id_vvt','marka_vvt','voenni_reg_nomer','god_vipuska','field_shassi','field_dvigatelia','field_pasport_formulara','rgk','gorod','gruppa_ekspluatacii','category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','tp','cp','kp','spisanie','sostoianie','need','available','shortage','excess']
    list_display_links = ('id_vvt','marka_vvt',)
    search_fields = ('id_vvt','marka_vvt','voenni_reg_nomer','god_vipuska','field_shassi','field_dvigatelia','field_pasport_formulara','rgk','gorod','gruppa_ekspluatacii','category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','tp','cp','kp','spisanie','sostoianie','need','available','shortage','excess')

class PeremeshenieAdmin(admin.ModelAdmin):
    list_display = ['premesh_id','field_prikaza_nomer_date_field','obiekti_vvt','voiskovaia_chast','podrazdelenia']
    list_display_links = ('premesh_id','field_prikaza_nomer_date_field','obiekti_vvt','voiskovaia_chast','podrazdelenia')
    search_fields = ('premesh_id','field_prikaza_nomer_date_field','obiekti_vvt','voiskovaia_chast','podrazdelenia')

class PodrazdeleniaAdmin(admin.ModelAdmin):
    list_display = ['id_podrazdelenia','name']
    list_display_links = ('id_podrazdelenia','name')
    search_fields = ('id_podrazdelenia','name')

class VoiskovieChastiAdmin(admin.ModelAdmin):
    list_display = ['id_voiskovie_chasti','name','gorod','rgk','rod_voiska']
    list_display_links = ('id_voiskovie_chasti','name','gorod','rgk','rod_voiska')
    search_fields = ('id_voiskovie_chasti','name','gorod','rgk','rod_voiska')

class VvtAdmin(admin.ModelAdmin):
    list_display = ['id_vvt','marka_vvt', 'nomer_znak','god_vipuska', 'color','field_shassi','field_dvigatelia','field_seria_pasporta', 'field_kuzova', 'field_tech_talon','rgk','garnizon','gorod','gruppa_ekspluatacii', 'vid', 'category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','mileage','tp','cp','kp','primechanie','sostoianie']
    list_display_links = ('id_vvt','marka_vvt', 'nomer_znak','god_vipuska', 'color','field_shassi','field_dvigatelia','field_seria_pasporta', 'field_kuzova', 'field_tech_talon','rgk','garnizon','gorod','gruppa_ekspluatacii', 'vid', 'category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','mileage','tp','cp','kp','primechanie','sostoianie')
    search_fields = ('id_vvt','marka_vvt', 'nomer_znak','god_vipuska', 'color','field_shassi','field_dvigatelia','field_seria_pasporta', 'field_kuzova', 'field_tech_talon','rgk','garnizon','gorod','gruppa_ekspluatacii', 'vid', 'category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','mileage','tp','cp','kp','primechanie','sostoianie')

    def response_add(self, request, obj, post_url_continue=None):

        return redirect(f'/carDetailsRK/{obj.id_vvt}')

    def response_change(self, request, obj):
        return redirect(f'/carDetailsRK/{obj.id_vvt}')

admin.site.register(Vvt, VvtAdmin)    
admin.site.register(Akb, AkbAdmin)    
# admin.site.register(AkbNew, AkbNewAdmin)    
admin.site.register(Avtoshini,AvtoshiniAdmin) 
admin.site.register(AvtoshiniNew, AvtoshiniNewAdmin) 
admin.site.register(Goroda,GorodaAdmin) 
admin.site.register(Main,MainAdmin) 
admin.site.register(ObiektiVvt,ObiektiVvtAdmin) 
admin.site.register(Peremeshenie,PeremeshenieAdmin) 
admin.site.register(Podrazdelenia,PodrazdeleniaAdmin) 
admin.site.register(VoiskovieChasti,VoiskovieChastiAdmin)
