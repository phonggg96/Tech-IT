# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import concat
from  django.contrib.auth import login, authenticate
from django.http import  Http404
from django.urls import reverse
from  .forms import LoginFrom, CommentForm
from django.shortcuts import render,get_object_or_404, redirect
from .models import DanhMuc, TinTuc, HashTag, Category, LoaiTin, Images


def index(request):
    context = {
        "tintucs": TinTuc.objects.all().order_by("-Create_date")[:5],
        "danhmucs": DanhMuc.objects.all(),
        "categories": Category.objects.order_by('-likes'),
        "hasgtags": HashTag.objects.all(),
        "loaitins": LoaiTin.objects.all(),
        "images": Images.objects.all(),
    }
    return render(request, 'home/index.html', context)

def contact(request, id):
    comment_form = CommentForm()
    return render(request, 'home/contact.html', {
        'tintucs':TinTuc.objects.get(pk=id),
        'comment_form': comment_form
    })

def login_view(request):
    form = LoginFrom()
    if request.method == 'POST':
        user = authenticate(username = request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request=request, user=user)

            return redirect(reverse('index'))
    return render(request, 'login.html', {'login_form': form})

def categogy(request, categogy_name_slug):

    context_dict ={}
    try:
        categogy = Category.objects.get(slug=categogy_name_slug)
        context_dict['categogy_name']= categogy.name

        tintucs = TinTuc.objects.filter(categogy = categogy)
        context_dict['tintucs'] = tintucs
    except Category.DoesNotExist:
        pass
    return render(request,'home/base.html', context_dict)


def add_comment(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")

        from django.contrib.auth.models import User
        data = {
            "content": request.POST.get("content", ""),
            "user_id": User.objects.first().pk,
            "post_id": TinTuc.objects.get(pk=post_id).pk
        }
        print("====aaaa====", data)
        comment_form = CommentForm(data)

        if comment_form.is_valid():
            print("=======valid")
            comment_form.save()
        else:
            print("=======invalid")

        return redirect(reverse('home:contact', kwargs={"id": post_id}))


