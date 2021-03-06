from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Member

# =========ET=========
class SearchForm(forms.ModelForm):
    pic = forms.BooleanField()
    find_girl = forms.BooleanField()
    find_boy = forms.BooleanField()
    height_min = forms.IntegerField(max_value=300,min_value=50)
    height_max = forms.IntegerField(max_value=300,min_value=height_min)
    weight_min = forms.IntegerField(max_value=300,min_value=20)
    weight_max = forms.IntegerField(max_value=300,min_value=weight_min)
    age_min = forms.IntegerField()
    age_max = forms.IntegerField(min_value=age_min)
    class Meta:
        model = Member
        fields = ('pic',
                  'find_girl',
                  'find_boy',
                  'height_min','height_max',
                  'weight_min','weight_max',
                  'age_min','age_max',
                  'blood_type',
                  'location',
                  'religion',
                  'relationship',
                  'relationship_status',
                  )
        widgets = {
            'blood_type':forms.CheckboxSelectMultiple(),
            'location':forms.CheckboxSelectMultiple(),
            'religion':forms.CheckboxSelectMultiple(),
            'relationship':forms.CheckboxSelectMultiple(),
            'relationship_status':forms.CheckboxSelectMultiple(),
        }
    def __init__(self, submit_title='Submit', *args,  **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['blood_type'].empty_label = None
        self.fields['location'].empty_label = None
        self.fields['religion'].empty_label = None
        self.fields['relationship'].empty_label = None
        self.fields['relationship_status'].empty_label = None
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', submit_title))
# =========ET=========
