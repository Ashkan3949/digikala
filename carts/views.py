from django.shortcuts import render

# Create your views here.
def carts_summery(request):
    return render(request, "carts_summery.html", {})
def carts_add(request):
    pass
def carts_delete(request):
    pass
def carts_update(request):
    pass