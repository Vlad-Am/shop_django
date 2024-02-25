from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from catalog.models import Products, Contacts, Blog


class ProductListView(ListView):
    model = Products


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ("name", "phone_number", "message")
    success_url = reverse_lazy('catalog:contacts')
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #     print(f"Пользователь с именем: {name}\nТелефоном: {phone}\nПрислал сообщение: {message}")
    # return render(request, 'catalog/contacts.html')


class ProductsDetailView(DetailView):
    model = Products


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('catalog:blogs_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('catalog:blogs_list')

    # def get_success_url(self, *args, **kwargs):
    #     super().get_success_url(*args, **kwargs)
    #     return reverse_lazy('catalog:view_blog', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs_list')
