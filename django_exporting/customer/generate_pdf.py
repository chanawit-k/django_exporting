from django.shortcuts import render
from xhtml2pdf import pisa
from django.http import HttpResponse


def generate_pdf_function(company_name, invoice_number, invoice_date, customer_name, customer_address, items):
  # Write your PDF generation code here
  html = '<html><body>'
  html += '<h1>Invoice</h1>'
  html += '<p>Company Name: ' + company_name + '</p>'
  html += '<p>Invoice Number: ' + invoice_number + '</p>'
  html += '<p>Invoice Date: ' + invoice_date + '</p>'
  html += '<p>Customer Name: ' + customer_name + '</p>'
  html += '<p>Customer Address: ' + customer_address + '</p>'
  html += '<h2>Items</h2>'
  html += '<p>' + items + '</p>'
  html += '</body></html>'
  result = pisa.CreatePDF(html, dest=BytesIO())
  return result


def generate_pdf(request):
  if request.method == 'POST':
    company_name = request.POST.get('company_name', '')
    invoice_number = request.POST.get('invoice_number', '')
    invoice_date = request.POST.get('invoice_date', '')
    customer_name = request.POST.get('customer_name', '')
    customer_address = request.POST.get('customer_address', '')
    items = request.POST.get('items', '')
    # Generate PDF using xhtml2pdf
    result = generate_pdf_function(company_name, invoice_number, invoice_date, customer_name, customer_address, items)
    if result.err:
      return HttpResponse('Error generating PDF: %s' % result.err)
    response = HttpResponse(content_type='application/pdf')
    response.write(result.dest.getvalue())
    return response
  return render(request, 'index.html')