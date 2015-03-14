# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

def _upload_path(instance,filename):
    return instance.get_upload_path(filename)

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    #input by administrators and selectable in maker_form& project_form
    def __unicode__(self):
        return self.category_name

class Major(models.Model):
    major_name = models.CharField(max_length=200)
    other_major_tag = models.CharField(max_length=200,blank=True)
    # other_major should be only a field in form than add to Major model
    # input from maker_form and selectable by project_form
    def __unicode__(self):
        return self.major_name

class Maker(models.Model):
    profile_pic = models.ImageField(blank=True,upload_to=_upload_path)
    user = models.OneToOneField(User)
    maker_major = models.ManyToManyField(Major,blank=True)
    maker_other_major = models.CharField(max_length=200,blank=True)
    # how to prevent other_major=maker_major? get or create?
    maker_related_category = models.ManyToManyField(Category)
    # let them choose interested category
    maker_bonus_offer = models.CharField(blank=True,max_length=200)
    # add some tag for themself to improve matching
    maker_detail = RichTextField(config_name='detail')
    def __unicode__(self):
        return self.user.username
    def get_upload_path(self,filename):
        return "maker/"+str(self.user.username)+"/"+filename

class Project(models.Model):
    project_category = models.ForeignKey(Category)
    #because we want maker 'choose' but enter any category
    project_name = models.CharField(max_length=200)
    project_cover = models.ImageField(upload_to=_upload_path,blank=True)
    project_starter = models.ManyToManyField(User, related_name='starter')
    #current login user
    project_request_major = models.ManyToManyField(Major)
    #match with maker major & other major
    project_matched_maker = models.ManyToManyField(User, related_name='matched_maker')
    pub_date = models.DateTimeField('date published')
    project_detail = RichTextField(config_name='detail')
    project_file = models.FileField(upload_to=_upload_path,blank=True)
    def __unicode__(self):
        return self.project_name

    def get_upload_path(self,filename):
        return "project_uploads/"+str(self.id)+"/"+filename
    # project_uploads前面不用加斜線，會自動接在media資料夾後面產生

class MakerBlog(models.Model):
#這是用在maker_blog.html的
    blog_title = models.CharField(max_length=200)   #要不要直接做成Maker的ID就好呢
    maker = models.OneToOneField(Maker)             #一個Maker一個BLOG
    avatar = models.ImageField(blank=True)
    projects = models.ManyToManyField(Project)
    jumbotron = models.ImageField(blank=True)
    # 先記下來 應該還要有個gallery 是用來放作品集或projects 之後可能用form的格式呈現 才不用多存一次同樣的圖片
    # Gallery 典籍之後要連結到對應的  MakerBlogArticle 或 Project
    def __unicode__(self):
        return self.blog_title

class MakerBlogArticle(models.Model):   #要不要讓作品集跟部落格文章互通？！這邊部落格真的有使用率嗎？先互通好了～
    Title = models.CharField(max_length=200)    #文章標題
    blog = models.ForeignKey(MakerBlog)
    article = RichTextField(config_name='detail')   #文章內容,導入所見即所得編輯器
    tags = models.CharField(max_length=500)         #就是TAG 先放著吧
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_comments = models.IntegerField()
    rating = models.IntegerField()
    def __unicode__(self):
        return self.Title

class Schedule(models.Model):
    maker = models.OneToOneField(Maker,blank=True)
    project = models.OneToOneField(Project,blank=True)


