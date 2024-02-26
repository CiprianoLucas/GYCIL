from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm

def client_page(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save()
            return redirect('service_details', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'client_page.html', {'form': form})

def company_page(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'company_page.html', {'service_requests': service_requests})

def accept_service(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    service_request.accepted = True
    service_request.save()
    return redirect('service_details', request_id=service_request.id)

def service_details(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    status = "Accepted" if service_request.accepted else "Pending"
    service_request.status = status
    return render(request, 'service_details.html', {'service_request': service_request})
