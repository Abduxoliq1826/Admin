from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')
def Login(request):

    return render(request, 'login.html',)
@login_required(login_url='login')
def ProductFilter(request):
    a = Ads.objects.filter(status=1)
    context = {
        'is_admin' : a
    }
    return render(request, 'is_admin.html', context)
@login_required(login_url='login')
def About(request, pk):
    a = Ads.objects.get(id=pk)
    context = {
        'about': a,
    }
    return render(request, 'about.html', context)

def Logins(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.get(username=username)
    if user.type == 1:
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return redirect('login')


def LogOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def All_User(request):
    context = {
        'user': User.objects.filter(type=2),

    }
    return render(request, 'users.html', context)

@login_required(login_url=login)
def AllAds(request):
    ads = Ads.objects.all()
    context = {
        'ads': ads,
    }
    return render(request, 'ads.html', context)


@login_required(login_url='login')
def IsAcepted(request):
    a = Ads.objects.filter(status=2)
    context = {
        'ads': a
    }
    return render(request, 'is_acepted.html', context)

@login_required(login_url='login')
def IsRejected(request):
    a = Ads.objects.filter(status=3)
    context = {
        'ads' : a
    }
    return render(request, 'is_rejected.html', context)
@login_required(login_url=login)
def Sold(request):
    a = Ads.objects.filter(status=4)
    context = {
        'ads' : a
    }
    return render(request, 'sort.html', context)


@login_required(login_url=login)
def Users(request,pk):
    context = {
        'ads': Ads.objects.filter(owner_id=pk),

    }
    return render(request, 'users2.html', context)

@login_required(login_url='login')
def InformationViews(request):

    if request.method == 'GET':
        context = {
            'info': Information.objects.last(),
        }
        return render(request, 'info.html', context)
    elif request.method == 'POST':
        company_name = request.POST.get('company_name')
        logo = request.FILES['logo']
        description = request.POST.get('description')
        googleplay = request.POST.get('googleplay')
        appstore = request.POST.get('appstore')

        Information.objects.create(company_name=company_name,logo=logo,description=description,googleplay=googleplay,appstore=appstore,
        )
        context = {
            'info': Information.objects.last(),
        }
        return render(request, 'info.html', context)

@login_required(login_url='login')
def Accepted(request, pk):
    ads = Ads.objects.get(id=pk)
    ads.status = 2
    ads.save()
    return redirect('productfilter')

@login_required(login_url='login')
def Rejected(request, pk):
    ads = Ads.objects.get(id=pk)
    ads.status = 3
    ads.save()

    return redirect('productfilter')

@login_required(login_url='login')
def AdsSingle(request, pk):

    context = {
        'ads': Ads.objects.get(id=pk)
    }
    return render(request, 'single-ads.html', context)


@login_required(login_url=login)
def UpdateUser(reuqest):
    user = reuqest.user
    if user is not None:
        if reuqest.method =='POST':
            username = reuqest.POST.get('username')
            img = reuqest.POST.get('img')
            last_password = reuqest.POST.get('last_password')
            new_password = reuqest.POST.get('new_password')
            restartpassword = reuqest.POST.get('restartpassword')
            usr = authenticate(username=user.username, password=last_password)
            if new_password == restartpassword:
                if usr is not None:
                    usr.username = username
                    usr.img = img
                    usr.set_password(new_password)
                    usr.save()
                    return redirect('dashboard')
                return redirect('reset')
            return redirect('reset')
        return redirect('users')
    return redirect('login')

@login_required(login_url='login')
def Reset(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'updateuser.html', context)
@login_required(login_url=login)
def AddCategory(request):
    if request.method == 'GET':
        context = {
            'category': Category.objects.all()
        }
        return render(request, 'category.html', context)
    name = request.POST.get('name')
    photo = request.FILES['photo']
    Category.objects.create(name=name, photo=photo)
    context = {
        'category': Category.objects.all()
    }
    return render(request, 'category.html', context)
@login_required(login_url=login)
def Regions(request):
    if request.method == 'GET':
        context = {
            'region': Region.objects.all()
        }
        return render(request, 'region.html', context)
    name = request.POST.get('name')
    Region.objects.create(name=name)
    context = {
        'region': Region.objects.all()
    }
    return render(request, 'region.html', context)
@login_required(login_url=login)
def SubCategory(request):
    if request.method == 'GET':
        context = {
            'subcategory': Subcategory.objects.all(),
            'category': Category.objects.all()
        }
        return render(request, 'subcategory.html', context)
    name = request.POST.get('name')
    category = request.POST.get('category')
    Subcategory.objects.create(name=name, category_id=category)
    context = {
        'subcategory': Subcategory.objects.all()
    }
    return render(request, 'subcategory.html', context)
@login_required(login_url=login)
def SingleCategory(request,pk):
    if request.method == 'GET':
        context = {
            'category': Category.objects.get(id=pk),
        }
        return render(request, 'singlecategory.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES['photo']
        category = Category.objects.get(id=pk)
        category.name = name
        category.photo = photo
        category.save()
        context = {
            'category': category,
        }
        return render(request, 'singlecategory.html', context)
@login_required(login_url=login)
def DeleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category')
@login_required(login_url=login)
def SingleSubCategory(request,pk):
    if request.method == 'GET':
        context = {
            'subcategory': Subcategory.objects.get(id=pk),
            'category': Category.objects.all(),
        }
        return render(request, 'singlesubcategory.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        subcategory = Subcategory.objects.get(id=pk)
        subcategory.name = name
        subcategory.category_id = category
        subcategory.save()
        context = {
            'subcategory': subcategory,
            'category': Category.objects.all(),
        }
        return render(request, 'singlesubcategory.html', context)

@login_required(login_url=login)
def DeleteSubCategory(request, pk):
    subcategory = Subcategory.objects.get(id=pk)
    subcategory.delete()
    return redirect('subcategory')

@login_required(login_url=login)
def SingleRegion(request,pk):
    if request.method == 'GET':
        context = {
            'region': Region.objects.get(id=pk),
        }
        return render(request, 'single-region.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        region = Region.objects.get(id=pk)
        region.name = name
        region.save()
        context = {
            'region': region,
        }
        return render(request, 'single-region.html', context)
@login_required(login_url=login)
def DeleteRegion(request, pk):
    region = Region.objects.get(id=pk)
    region.delete()
    return redirect('regions')