from django.test import TestCase
from .forms import CompanyForm, ProductsForm
from .models import Company

class TestCompanyForm(TestCase):
    """
        TestCompanyForm
            Test class for testing company forms module
    """

    def test_validate_company_form_with_valid_data(self):
        """
            testing CompanyForm with a valid payload
        """
        data = {
            "company_id": "2345",
            "name": "Aditya Birla Group",
            "location": "Pune (Maharashtra, 411023)",
        }
        form = CompanyForm(data=data)
        self.assertTrue(form.is_valid())

    def test__validate_company_form_with_invalid_data(self):
        """
            testing CompanyForm with an invalid payload
        """
        data = {
            "company_id": "",
            "name": "Aditya Birla Group",
            "location": "Pune (Maharashtra, 411023)",

        }
        form = CompanyForm(data=data)
        self.assertFalse(form.is_valid())


class TestProductsForm(TestCase):
    """
        TestProductsForm
            Test class for testing products form module
    """

    def test_validate_product_form_with_valid_data(self):
        """
            testing ProductsForm with a valid payload
        """

        data = {
            "company_id": "2345",
            "name": "Aditya Birla Group",
            "location": "Pune (Maharashtra, 411023)",
        }
        company_form = CompanyForm(data=data)
        self.assertTrue(company_form.is_valid())
        company_form.save()

        company = Company.objects.all().first()
        
        data = {
            "product_id": "1234",
            "name": "AAC Blocks",
            "company": company.id,
        }
        form = ProductsForm(data=data)
        self.assertTrue(form.is_valid())

    def test_validate_product_form_with_invalid_data(self):
        """
            testing ProductsForm with an invalid payload
        """
        data = {
            "product_id": "1245",
            "name": "",
            "company": "545",
        }
        form = ProductsForm(data=data)
        self.assertFalse(form.is_valid())
