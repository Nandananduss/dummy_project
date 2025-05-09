from django.shortcuts import render

def vendor_login(request):
    return render(request, "vender_login.html")

def services_view(request):
    return render(request, "services.html")
