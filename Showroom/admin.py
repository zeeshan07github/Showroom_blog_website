from django.contrib import admin
from .models import *
# Register your models here.



class carAdmin(admin.ModelAdmin):
    list_display =('model' ,'Chasis_no',)

class modalAdmin(admin.ModelAdmin):
    list_display =('name' ,'Brand',)

class brandAdmin(admin.ModelAdmin):
    list_display =('name' ,'showrooms',)


class engineAdmin(admin.ModelAdmin):
    list_display = ('Engine_no' ,'model',)

class staffAdmin(admin.ModelAdmin):
    list_display = ('name','Role',)


class showroomAdmin(admin.ModelAdmin):
    list_display =('name' ,'Owner','Location',)

admin.site.register(showroom ,showroomAdmin)
admin.site.register(staff , staffAdmin)
admin.site.register(model ,modalAdmin)
admin.site.register(feature)
admin.site.register(engine , engineAdmin)
admin.site.register(brand ,brandAdmin)
admin.site.register(car , carAdmin)
admin.site.register(Engine_model)