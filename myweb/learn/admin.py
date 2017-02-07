from django.contrib import admin
from learn.models import Event,Guest
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','start_time','id']
    search_fields = ['name']
    list_filter = ['status']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)