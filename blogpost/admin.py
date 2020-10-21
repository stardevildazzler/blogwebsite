from django.contrib import admin
from .models import blogpost

# Register your models here.
class blogpostAdmin(admin.ModelAdmin):
    class Media:
        js=('js/tiny.js',)

admin.site.register(blogpost,blogpostAdmin)