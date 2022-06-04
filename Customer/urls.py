from django.urls import path
from . import views

urlpatterns = [
    path("create-list/",views.CustomerListCreateApiView.as_view(),name="customer-create-list-view")
]
