from django.contrib import admin
from models import *
# Register your models here.


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = ('user', 'profile_pic',  'biological_sex',
              'sexuality', 'height', 'weight', 'birthday',
              'age', 'blood_type', 'location', 'religion',
              'relationship', 'relationship_status', )


@admin.register(BiologicalSex)
class BiologicalSexAdmin(admin.ModelAdmin):
    list_display = ('biological_sex', )
    fields = ()


@admin.register(Sexuality)
class SexualityAdmin(admin.ModelAdmin):
    list_display = ('sexuality', )
    fields = ()

@admin.register(RelationShip)
class RelationShipAdmin(admin.ModelAdmin):
    list_display = ('relationship', )
    fields = ()


@admin.register(RelationShipStatus)
class RelationShipStatusAdmin(admin.ModelAdmin):
    list_display = ('relationship_status', )
    fields = ()


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    list_display = ('blood_type', )
    fields = ()


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', )
    fields = ()


@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion', )
    fields = ()
