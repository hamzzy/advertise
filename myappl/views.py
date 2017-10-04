from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django_common.auth_backends import User

from.models import Ads,Category,UserProfile
from .forms import UserLoginForm, UserRegistrationForm, AdvertForm, CreateForm, Profile_edit,User_edit
from  django.contrib import  messages

# Create your views here.
def index(request):
    queryset = Ads.objects.all().order_by("-timestamp")
    obj=Category.objects.all()
    o=Ads.objects.filter()

    paginator = Paginator(o,10)
    pager = ('page')

    page = request.GET.get(pager)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'index.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLoginForm()
    context={
        'query':queryset,
        'form':form,
        'cat':obj,
        'page':queryset

    }

    return render(request,'index.html',context)

def post_detail(request,id):
    queryset = get_object_or_404(Ads, id=id)


    context={
        'post':queryset,

    }
    return render(request,'details.html',context)


@login_required
def dashboard(request):
    # if user has a profile (request.user is currently logged in user)
      # get that profile

        UserProfile.objects.filter(user=request.user).exists()
        profile= UserProfile.objects.get(user=request.user)
        form = Profile_edit(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()



        context = {
            'obj':profile,
            'form':form




            }


        return render(request,'base.html',context)



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = UserProfile.objects.create(user=new_user)
            context={
                'new':new_user
            }
            return render(request,'register_suc.html',context)
    else:
        user_form = UserRegistrationForm()

    return  render(request,'signup.html')

@login_required
def post_ads(request):
   profile = UserProfile.objects.get(user=request.user)
   if request.POST:
     form = AdvertForm(request.POST,request.FILES)
     if form.is_valid():
         post = form.save(commit=False)
         post.user = request.user
         post.save()
     return HttpResponseRedirect('ads.html')
   else:
    form=AdvertForm()

   context={
      "form":form,
       'obj':profile,

        }
   return render(request,'post.html',context)


@login_required
def log_out(request):
  logout(request)
  return render(request,'logout.html')
@login_required
def edit(request,id=None):
    instance=get_object_or_404(Ads,id=id)
    form = AdvertForm(request.POST or None, request.FILES,instance=instance)
    if form.is_valid():
       instance = form.save(commit=False)
       instance.save()
       messages.success(request,'successfully updated')
    context={
        'update':form,
        'data':instance

       }
    return render(request,'edit.html',context)
@login_required
def delete(request,id=None):
    instance=get_object_or_404(Ads,id=id)
    instance.delete()
    messages.success(request,'succefully delete')

    return render(request,'base.html')

def create(request):
   # if request.POST:
        form = CreateForm(request.POST or None, request.FILES)

        if form.is_valid():
            instance= form.save(commit=False)
            instance.user=request.user
            instance.save()
        context = {
            'create': form,
        }
        return  render(request,'create.html',context)



def base(request):

    return  render(request,'base.html')


def category(request,category_slug):
    cato=Category.objects.all()
    catego = get_object_or_404(Category,slug=category_slug)
    post = Ads.objects.filter(category=catego).order_by('name')
    paginator = Paginator(post, 1)
    pager = ('page')

    page = request.GET.get(pager)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


    context={
        'cat':post,
        'cato':cato,
        'page':queryset
    }
    return render(request,'category.html',context)
@login_required
def ads(request):

    profile = UserProfile.objects.get(user=request.user)

    lo = Ads.objects.filter(user=request.user)
    context={
        'lo':lo,
        'obj':profile


    }

    return render(request,'ads.html',context)
@login_required
def profile_edit(request):
        new_form=User_edit(request.POST,request.FILES,instance=request.user)
        if new_form.is_valid():
            instance = new_form.save(commit=False)
            instance.user = request.user
            instance.save()

        UserProfile.objects.filter(user=request.user).exists()
        profile = UserProfile.objects.get(user=request.user)


        context={

            'obj':profile,
            'new':new_form,


        }



        return  render(request,'edit_profile.html',context)


def register_suc(request):
    return  render(request,'register_suc.html')


def about(request):
    return  render(request,'about.html')
def reset_password(request):
    return  render(request,'password_reset.html')