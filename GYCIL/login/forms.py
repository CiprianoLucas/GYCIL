from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class UserForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'senha',
            Submit('submit', 'Enviar', css_class='btn btn-primary')
        )

class CompanyForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    cnpj = forms.CharField(label='CNPJ', max_length=100)
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('cnpj', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'senha',
            Submit('submit', 'Enviar', css_class='btn btn-primary')
        )
