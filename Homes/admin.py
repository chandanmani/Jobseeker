from django.contrib import admin
from .models import Job,Category

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=["id","Company_name","Location","Job_status"]

class CategoryAdmin(admin.ModelAdmin):
    list_display=["category_name","slug",]


  

admin.site.register(Job,JobAdmin)
admin.site.register(Category,CategoryAdmin)