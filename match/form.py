from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Member

#=========ET=========
class SearchForm(forms.ModelForm):
    pic = forms.BooleanField()
    height_max = forms.IntegerField()
    height_min = forms.IntegerField()
    class Meta:
        model = Member
        fields = ('sexuality',)
    def __init__(self,*args, **kwargs):
        super.__init__(*args, **kwargs)
#=========ET=========