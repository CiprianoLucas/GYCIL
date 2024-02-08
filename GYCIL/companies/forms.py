from django import forms
from .models import Company
from crispy_forms.helper import FormHelper

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ["slug", "enabled", "created_at"]
        
        
        labels = {
            "company_name": "Rasão social",
            "fantasy_name": "Nome fantasia",
            "representative": "Representante legal",
            "cnpj": "CNPJ",
            "email": "E-mail",
            "zipcode": "Cep",
            "street": "Endereço",
            "number": "Número",
            "city": "Cidade",
            "state": "Estado",
            "phone": "Telefone",
            "logo": "Logomarca",
        }
        
        error_messages = {
            # "name": {
            #     "required": "O campo nome é obrigatório",
            #     "unique": "Já existe um produto cadastrado com esse nome"
            # },
            # "description": {
            #     "required": "O campo descrição é obrigatório",                
            # },
            # "sale_price": {
            #     "required": "O campo preço de venda é obrigatório"
            # },
        }
        
        widgets = {
            # "expiration_date": forms.DateInput(attrs={"type":"date"}, format="%Y-%m-%d")
        }