import datetime
from pathlib import Path

from docxtpl import DocxTemplate
from .models import Main

doc = DocxTemplate("carDetails.docx")

context = {
    'Marka_avto': Main.objects.filter(field_p_p =  1).last().marka_avto
}

doc.render(context)
doc.save("CarDetails.docx")