from antigravity import geohash
from sqlite3 import InterfaceError
from urllib import request
from django.forms import ModelForm
from django import forms
from .models import *

class Postfrom(ModelForm):
    class Meta:
        model = Cities
        fields = ["name","geography","history","culture","language","infrastructure","tourist_spots"]

        def clean(self):
            super(Postfrom,self).clean()

            name = self.cleaned_data.get('name')
            geography = self.cleaned_data.get('geography')
            history = self.cleaned_data.get('history')
            culture = self.cleaned_data.get('culture')
            language = self.cleaned_data.get('language')
            infrastructure = self.cleaned_data.get('infrastructure')
            tourist = self.cleaned_data.get('tourist')
            
                

