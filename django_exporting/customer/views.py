from django.views.generic import TemplateView
from csv_export.views import CSVExportView
from django.utils import timezone
from .models import Customer

class CustomerListView(TemplateView):
    template_name = "customer/customer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_list'] = Customer.objects.all()
        return context
    
class DataExportView(CSVExportView):
    model = Customer
    fields = "__all__"

    # When using related fields you will likely want to override get_queryset() use select_related() or prefetch_related().
    def get_queryset(self):
        return super().get_queryset()
    
    def get_filename(self, queryset):
        return "data-export-{!s}.csv".format(timezone.now())