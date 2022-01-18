from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.HelloView.as_view(),
        name="home",
    ),
    path(
        "add_company",
        views.AddCompany.as_view(),
        name="company",
    ),
    path(
        "add_product",
        views.AddProducts.as_view(),
        name="product",
    ),
]
