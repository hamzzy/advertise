from django.contrib import admin
from .models import  Category,UserProfile,Ads,Location


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['picture','user','location']
    list_filter = ['picture','user','location']

    class meta:
        meta=UserProfile

admin.site.register(UserProfile,UserProfileAdmin)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

    class meta:
        meta = Category


admin.site.register(Category,CategoryAdmin)



class AdsAdmin(admin.ModelAdmin):
    list_display = ['name','text','price','phone','picture','location','category','user','timestamp']
    list_filter = ['name','text','phone','picture','location','category','user']

    class meta:
        meta = Ads


admin.site.register(Ads,AdsAdmin)

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']

    class meta:
        meta=Location

admin.site.register(Location,LocationAdmin)