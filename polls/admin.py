from django.contrib import admin
from .models import *

class DocumentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Document,DocumentAdmin)

# Register your models here.
