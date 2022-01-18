from django.forms import ModelForm
from hello.models import Company, Products


class CompanyForm(ModelForm):
    """
    CompanyForm
        Form to create and show company details
    """

    class Meta:
        model = Company
        fields = ["name", "company_id", "location"]


class ProductsForm(ModelForm):
    """
    ProductsForm
        Form to create and show products details
    """

    class Meta:
        model = Products
        fields = ["company", "product_id", "name"]
