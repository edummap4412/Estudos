from django.contrib import admin

from .models import Produto, Costumer


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class CostumerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Costumer, CostumerAdmin)
