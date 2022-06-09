from django import forms
from django.forms import ModelForm
from . import models

code = "Kode Barang"
product_name = "Nama Barang"
unit_name = "Nama Satuan"
base_price = "Harga Dasar"
base_stock = "Stok Awal"
unit = "Satuan"


class form_create_book(ModelForm):
    class Meta:
        model = models.Books
        exclude = ('user',)
