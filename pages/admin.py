from django.contrib import admin
from . models import JoinForm

class JoinFormAdmin(admin.ModelAdmin):
    list_display= ['number', 'name', 'phone',  'image']
  
    search_fields=['number']
    list_filter= ['number']
admin.site.register(JoinForm, JoinFormAdmin)



# Register your models here.
#class BlogAdminArea(admin.AdminSite):
 #   site_header='Blog Admin Area'
#blog_site= BlogAdminArea(name='BlogAdmin')


