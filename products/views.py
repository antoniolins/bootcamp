from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render


from .models import Product


# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Helllow Word</h1>")
    context = {"name": "Antonio Lins"}
    return render(request, "home.html", context)


def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found, code:404"}) # return JSON with HTTP status code of 404
    #return JsonResponse({"id": obj.id})
    return render(request, "products/detail.html", {"object": obj})


def product_api_detail_view(request, id, *args, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with HTTP status code of 404
    # return JsonResponse({"id": obj.id})
    return render(request, "products/detail.html", {"object": obj})

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all() # [obj1, obj2, obj3,]
    context = {"object_list": qs}
    return render(request, "products/list.html", context)