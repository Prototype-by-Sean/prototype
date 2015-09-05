from django.contrib import admin
from models import *
# Register your models here.


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = ('user', 'biological_sex', 'sexuality')


@admin.register(BiologicalSex)
class BiologicalSexAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Sexuality)
class SexualityAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(RelationShip)
class RelationShipAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(RelationShipStatus)
class RelationShipStatusAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ()
