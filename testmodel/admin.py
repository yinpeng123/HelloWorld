from django.contrib import admin
from testmodel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model=Tag

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','age','email')
    search_fields=('name',)
    inlines=[TagInline]
    fieldsets=(
        ['Main',{
            'fields':('name','email',),
        }], 
        ['Advance',{
            'classes':('collapse',), #css
            'fields':('age',)
        }]     
    )
admin.site.register(Contact,ContactAdmin)
admin.site.register([Test,Tag])
