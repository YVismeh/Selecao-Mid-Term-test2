from django.urls import path
from .views import home, portfolio_details, service_details


app_name = "root"

urlpatterns = [
    path("", home, name="home"),
    path("portfolio-details", portfolio_details, name="portfolio-details"),
    path("service-details", service_details, name="service-details"),
]