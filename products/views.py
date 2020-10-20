from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, redirect


from .models import Product
from .forms import ProductModelForm

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


def product_create_view(request, *args, **kwargs):
    # url -> path('products/create/', product_create_view),

    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do some stuff
        # obj.user = request.user
        obj.save()
       # data = form.cleaned_data
       # Product.objects.create(**data)
        form = ProductModelForm()
        # return  HttpResponseRedirect("/success")
        # return redirect("/success")

    return render(request, "forms.html", {"form": form})
