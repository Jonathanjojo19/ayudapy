from django import forms
from leaflet.forms.fields import PointField
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.safestring import mark_safe

from .models import HelpRequest


class HelpRequestForm(forms.ModelForm):
    location = PointField(
        label="Lokasi",
        error_messages={'required': mark_safe('Anda belum menandakan lokasi Anda di peta\n <br>Jika Anda memiliki masalah dengan langkah ini, lihat <a href="#" class="is-link modal-button" data-target="#myModal" aria-haspopup="true">bantuan ini</a></p><p id="div_direccion" style="font-size: 10px; margin-bottom: 5px;"></p>')},
        help_text=mark_safe('<p style="margin-bottom:5px;font-size:10px;">Pilih lokasi Anda sehingga orang dapat menemukan Anda. Jika tidak ingin menandai rumah Anda, Anda bisa menandai kantor polisi terdekat atau tempat umum terdekat lainnya.\
            <br>Jika Anda memiliki masalah dengan langkah ini, lihat <a href="#" class="is-link modal-button" data-target="#myModal" aria-haspopup="true">bantuan ini</a></p><p id="div_direccion" style="font-size: 10px; margin-bottom: 5px;"></p>'),
        )

    class Meta:
        model = HelpRequest
        fields = (
            "title",
            "message",
            "categories",
            "name",
            "phone",
            "location",
            "address",
            "picture"
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Contoh: Saya butuh bantuan makanan untuk keluarga saya secepatnya.",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "textarea",
                    "rows": 4,
                    "placeholder": "Contoh: Saya butuh masker dan alat kebersihan, bantuan sekecil apapun akan sangat membantu.\nTerima kasih banyak!",
                }
            ),
            "name": forms.TextInput(attrs={"class": "input"}),
            "phone": forms.TextInput(attrs={"class": "input", "type": "tel"}),
            "address": forms.TextInput(attrs={"class": "input"}),
            'categories': forms.SelectMultiple(attrs={"style": "display:none;"}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Sudah pernah didaftarkan sebelumnya.",
            }
        }
