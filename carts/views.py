from django.shortcuts import render, get_object_or_404
from .carts import Carts
from shop.models import Product
from django.http import JsonResponse
# Create your views here.
def carts_summery(request):
    return render(request, "carts_summery.html", {})
def carts_add(request):
    carts = Carts(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        carts.add(product=product)




        carts_quantity = carts.__len__()
#        response = JsonResponse({'Product name': product.name})
        response = JsonResponse({'qty': carts_quantity})

        return response



def carts_delete(request):
    pass
def carts_update(request):
    pass