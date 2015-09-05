# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


def _upload_path(instance, filename):
    return instance.get_upload_path(filename)


class BiologicalSex(models.Model):
    # 生理性別
    biological_sex = models.CharField(max_length=200)

    def __unicode__(self):
        return self.biological_sex


class Sexuality(models.Model):
    # 性向
    sexuality = models.CharField(max_length=200)

    def __unicode__(self):
        return self.sexuality


class RelationShip(models.Model):
    relationship = models.CharField(max_length=200)

    def __unicode__(self):
        return self.relationship


class RelationShipStatus(models.Model):
    relationship_status = models.CharField(max_length=200)

    def __unicode__(self):
        return self.relationship_status


class BloodType(models.Model):
    blood_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.blood_type

class Location(models.Model):
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return self.location

class Religion(models.Model):
    religion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.religion


# 使用者資料庫，導入內建的User(已經有帳號、密碼、姓氏、名稱、email欄位)
class Member(models.Model):
    profile_pic = models.ImageField(upload_to=_upload_path)
    user = models.OneToOneField(User)
    biological_sex = models.ForeignKey(BiologicalSex)
    sexuality = models.ForeignKey(Sexuality)
    height = models.IntegerField(max_length=200)
    weight = models.IntegerField(max_length=200)
    birthday = models.DateField()
    age = models.IntegerField()
    blood_type = models.ForeignKey(BloodType)
    location = models.ForeignKey(Location)
    religion = models.ForeignKey(Religion)
    relationship = models.ForeignKey(RelationShip)
    relationship_status = models.ForeignKey(RelationShipStatus)
    detail = RichTextField(config_name='detail')

    def __unicode__(self):
        return self.user.username

    def get_upload_path(self,filename):
        return "maker/"+str(self.user.username)+"/"+filename