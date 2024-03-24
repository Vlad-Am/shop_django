from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, ContactsForm, VersionForm, ProductModeratorForm
from catalog.models import Products, Contacts, Blog, Version


class ProductsListView(ListView):
    model = Products

    def get_context_data(self, *args, **kwargs):
        """Получает данные о версиях экземпляра класса и выбирает текущую (активную) версию для продукта"""
        context = super().get_context_data(*args, **kwargs)
        products = self.get_queryset()
        for product in products:
            product.version = product.version_set.filter(working=True).first()
        context["object_list"] = products

        return context


class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Products

    # def get_context_data(self, **kwargs):
    #     """Получает данные о версиях экземпляра класса и выбирает текущую (активную) версию для продукта"""

    # context = super().get_context_data(**kwargs)
    #
    # product = self.get_object
    # print(product)
    # context['version'] = product.version.all()
    # context['current_version'] = product.version.filter(working=True).first()
    # return context


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')
    form_class = ProductForm

    def from_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')
    form_class = ProductForm

    def get_success_url(self, *args, **kwargs):
        super().get_success_url()
        return reverse_lazy('catalog:view_product', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data()
        subject_formset = inlineformset_factory(Products, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = subject_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = subject_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        subject_formset = context['formset']
        self.object = form.save()
        if subject_formset.is_valid():
            subject_formset.instance = self.object
            subject_formset.save()
        # попытка сделать возможность редактирования только у авторизированных пользователей
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_form_class(self):
        """Переопределение метода выбора формы для редактирования"""

        user = self.request.user
        perms = ("products.change_published", "products.change_description", "products.change_category")
        if user.has_perms(perms):
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise HttpResponseForbidden


class ContactsCreateView(CreateView):
    model = Contacts
    success_url = reverse_lazy('catalog:contacts')
    form_class = ContactsForm
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #     print(f"Пользователь с именем: {name}\nТелефоном: {phone}\nПрислал сообщение: {message}")
    # return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

    slug_url_kwarg = 'the_slug'
    # Should match the name of the slug field on the model
    slug_field = 'slug'


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "published", "price_per_one")
    success_url = reverse_lazy('catalog:blogs_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    slug_url_kwarg = 'the_slug'
    # Should match the name of the slug field on the model
    slug_field = 'slug'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "published", "price_per_one")
    success_url = reverse_lazy('catalog:blogs_list')

    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        super().get_success_url()
        return reverse_lazy('catalog:view_blog', kwargs={'the_slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs_list')
