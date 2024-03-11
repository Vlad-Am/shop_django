from django import forms

from catalog.models import Products, Version, Contacts


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("name", "description", "price", "preview", "category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        forbidden = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for words in forbidden:
            if words in cleaned_data:
                raise forms.ValidationError('Ошибка, запрещенные слова в названии')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for words in forbidden:
            if words in cleaned_data:
                raise forms.ValidationError('Ошибка, запрещенные слова в описании')

        return cleaned_data


class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Version
        fields = '__all__'


class ContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contacts
        fields = '__all__'
