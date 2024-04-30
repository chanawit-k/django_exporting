from django.views.generic import TemplateView

class CustomerListView(TemplateView):
    template_name = "customer/customer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

