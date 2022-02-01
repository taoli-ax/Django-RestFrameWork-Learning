from django.contrib import admin
from .models import Snippets


# Register your models here.


@admin.register(Snippets)
class SnippetAdmin(admin.ModelAdmin):
    class Meta:
        model = Snippets
        fields = '__all__'
