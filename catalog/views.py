from django.shortcuts import render, get_object_or_404

from catalog.models import Products


def product(request):
    products_list = Products.objects.all()
    context = {
        'object_list': products_list,
    }

    return render(request, 'catalog/body.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь с именем: {name}\nТелефоном: {phone}\nПрислал сообщение: {message}")
    return render(request, 'catalog/contacts.html')


def product_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {
        'product_detail': product
    }
    return render(request, 'catalog/product.html', context)
