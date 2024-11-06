from django.contrib import admin
from .models import *

class function_account(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'role')

class function_computerlab(admin.ModelAdmin):
    list_display = ('computerlab_id', 'lab', 'total_units')

class function_status(admin.ModelAdmin):
    list_display = ('status_id','remarks', 'date', 'time', 'stat_monitor', 'stat_keyboard', 'stat_mouse', 'stat_ram', 'stat_motherboard', 'stat_cpu')

class function_unit(admin.ModelAdmin):
    list_display = ('computerlab', 'pc_number', 'component')

class function_components(admin.ModelAdmin):
    list_display = ('component_id', 'status', 'monitor', 'keyboard', 'mouse', 'ram', 'motherboard', 'cpu')

admin.site.register(Account, function_account)
admin.site.register(ComputerLab, function_computerlab)
admin.site.register(Status, function_status)
admin.site.register(Unit, function_unit)
admin.site.register(Components, function_components)
