from django.contrib import admin
from .models import Vvt
# Register your models here.

# class VvtAdmin(admin.ModelAdmin):
#     list_display = ['id_vvt','marka_vvt', 'nomer_znak','god_vipuska', 'color','field_shassi','field_dvigatelia','field_seria_pasporta', 'field_kuzova', 'field_tech_talon','rgk','gorod','gruppa_ekspluatacii', 'vid', 'category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','mileage','tp','cp','kp','primechanie','sostoianie']
#     list_display_links = ('id_vvt','marka_vvt', 'nomer_znak','god_vipuska', 'color','field_shassi','field_dvigatelia','field_seria_pasporta', 'field_kuzova', 'field_tech_talon','rgk','gorod','gruppa_ekspluatacii', 'vid', 'category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','mileage','tp','cp','kp','primechanie','sostoianie')
#     search_fields = ('id_vvt','marka_vvt', 'nomer_znak','god_vipuska', 'color','field_shassi','field_dvigatelia','field_seria_pasporta', 'field_kuzova', 'field_tech_talon','rgk','gorod','gruppa_ekspluatacii', 'vid', 'category','norma_rashoda','type_of_mark','rod_voiska','voiskovaia_chast','podrazdelenia','mileage','tp','cp','kp','primechanie','sostoianie')

# admin.site.register(Vvt, VvtAdmin)    