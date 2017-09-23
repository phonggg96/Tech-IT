from __future__ import unicode_literals

from unicodedata import category

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class BaseHome(models.Model):
    Create_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DanhMuc(models.Model):
    Name = models.CharField(max_length=255)
    Is_Status = models.BooleanField(default=True)

    def __unicode__(self):
        return (self.Name)

class LoaiTin(models.Model):
    Title = models.CharField(max_length=255, null= True)
    idDanhMuc = models.ForeignKey(DanhMuc)

    def __unicode__(self):
        return (self.Title)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class TinTuc(BaseHome):
    Title = models.CharField(max_length=255)
    Id_DanhMuc = models.ForeignKey(DanhMuc)
    Id_LoaiTin = models.ForeignKey(LoaiTin, null= True)
    category = models.ForeignKey(Category, null= True)
    Decriptions = models.CharField(max_length=255, null=True)
    Content = RichTextField(verbose_name='Noi dung', null=True)
    Image = models.FileField(upload_to='images', null=True)
    Views = models.IntegerField(default=0)
    Creator = models.ForeignKey(User, null=True)
    Is_HightLight = models.BooleanField(default=False)

    def __unicode__(self):
        return (self.Title)

class HashTag(models.Model):
    Name = models.CharField(max_length=255)
    Is_Status = models.BooleanField(default=True)

    def __unicode__(self):
        return (self.pk, self.Name)

class TTHagTag(models.Model):
    Id_HashTag = models.ForeignKey(HashTag)
    Is_Status = models.BooleanField(default=True)

class Images(BaseHome):
    Name = models.CharField(max_length=255)
    Image = models.FileField(upload_to='images', null=True)
    alt = models.CharField(max_length=50, null=True)
    Is_Allowlink = models.BooleanField(default=True)

    def __unicode__(self):
        return (self.Name)

class Photographer(models.Model):
    Name = models.CharField(max_length=255)
    Is_Display = models.BooleanField(default=True)



class Comment(BaseHome):
    user = models.ForeignKey(User)
    post = models.ForeignKey(TinTuc)
    content = models.TextField()








