from django.contrib.auth.views import logout_then_login
from django.urls import path
from . import views

app_name = 'customer'


urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('csv', views.DataExportView.as_view(), name='customer_export_csv'),
]