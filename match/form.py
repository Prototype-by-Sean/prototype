from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Member

# =========ET=========
class SearchForm(forms.ModelForm):
    pic = forms.BooleanField()
    height_max = forms.IntegerField(max_value=300,min_value=50)
    height_min = forms.IntegerField(max_value=300,min_value=50)
    weight_max = forms.IntegerField(max_value=300,min_value=20)
    weight_min = forms.IntegerField(max_value=300,min_value=20)
    age_max = forms.IntegerField()
    age_min = forms.IntegerField()
    class Meta:
        model = Member
        fields = ('pic',
                  'sexuality',
                  'height_min','height_max',
                  'weight_min','weight_max',
                  'age_min','age_max',
                  'blood_type',
                  'location',

                  )
        widgets = {
            'location':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, submit_title='Submit', *args,  **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', submit_title))
# =========ET=========
