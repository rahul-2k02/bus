from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row

genders = (('', 'Choose your gender'),
           ('Male', 'Male'),
           ('Female', 'Female')
           )

departure = (('', 'From'),
             ('Banglore', 'Banglore'),
             ('Pune', 'Pune'),
             ('Mumbai', 'Mumbai'),
             ('Chennai', 'Chennai')
             )

arrival = (('', 'To'),
             ('Banglore', 'Banglore'),
             ('Pune', 'Pune'),
             ('Mumbai', 'Mumbai'),
             ('Chennai', 'Chennai')
             )


class ContactForm(forms.Form):
    dep=forms.ChoiceField(label='Departure',choices=departure)
    arr=forms.ChoiceField(label='Arrival',choices=arrival)
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Name'}))
    trip_date = forms.DateField(label="Journey Start", widget=forms.TextInput(
        attrs={'placeholder': 'mm/dd/yyyy'}))
    gender = forms.ChoiceField(
        label='Gender', help_text='Select Gender', choices=genders)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_class = ' container justify-content-center '
        # self.helper.label_class = ''
        # self.helper.field_class = 'col-md-6 col-xs-9'
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4  mb-12'),
                Column('gender', css_class='form-group col-md-6 mb-10'),

                css_class='form-row  center'
            ),
            Row(
                Column('dep', css_class='form-group col-md-8 mb-6'),
                Column('arr', css_class='form-group col-md-8 mb-6'),
                Column('trip_date', css_class='form-group col-md-6  mb-2'),

            ),
            Submit('submit', 'Submit', css_class="btn-success",)
        )
