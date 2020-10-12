from django.contrib import admin
from .models import table1
from .models import viewnotes

# Register your models here.

admin.site.register(table1)
admin.site.register(viewnotes)

# Register the admin class with the associated model
# admin.site.register(table2)

# # Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     pass
# # Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)
