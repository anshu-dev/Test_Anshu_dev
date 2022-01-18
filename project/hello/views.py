import socket

from django.conf import settings
from django.views.generic import CreateView, TemplateView
from django.utils import timezone
from .forms import CompanyForm, ProductsForm
from .models import Company, Products

from . import tasks


class HelloView(TemplateView):
    template_name = "hello_world.html"

    def get_context_data(self, **kwargs):
        now = timezone.now()
        container = socket.gethostname()
        remote_addr = self.request.META.get("REMOTE_ADDR", "no remote addr")
        # Invoke a task to record the details and provide a usage count
        task_watcher = tasks.write_usage_log.delay(now, container, remote_addr)
        counter = task_watcher.get()

        company_details = Company.objects.all()
        product_details = Products.objects.all()
        company_form = CompanyForm()
        product_form = ProductsForm()

        # Provide the context to the template
        return super().get_context_data(
            now=now,
            counter=counter,
            debug=settings.DEBUG,
            container=container,
            remote_addr=remote_addr,
            company_details=company_details,
            product_details=product_details,
            company_form=company_form,
            product_form=product_form,
            **kwargs,
        )


class AddCompany(CreateView):
    """
    AddCompany
        View to add company details.
    """

    form_class = CompanyForm
    success_url = "/"


class AddProducts(CreateView):
    """
    Register
        View to add products details.
    """

    form_class = ProductsForm
    success_url = "/"
