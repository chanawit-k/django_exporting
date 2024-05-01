from csv_export.views import CSVExportView
from django.utils import timezone
from django.conf import settings
from django.template.loader import get_template
import os
from django.http import HttpResponse
from django.views.generic import TemplateView, View
import pdfkit

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
    

wkhtml_to_pdf = os.path.join(
    settings.BASE_DIR, "wkhtmltopdf.exe")


def resume_pdf(request, *args, **kwargs):
    options = {
        'page-size': 'A4',
        'page-height': "13in",
        'page-width': "10in",
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    template_path = 'customer/template_pdf.html'
    template = get_template(template_path)
    
    context = {"name": "Areeba Seher"}
    html = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf=wkhtml_to_pdf)

    pdf = pdfkit.from_string(html, False, configuration=config, options=options)

    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    # print(response.status_code)
    if response.status_code != 200:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response