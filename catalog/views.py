from django.shortcuts import render


# Create your views here.
def body(request):
    return render(request, 'catalog/body.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь с именем: {name}\nТелефоном: {phone}\nПрислал сообщение: {message}")
    return render(request, 'catalog/contacts.html')
