# coding:utf-8
from django.shortcuts import render
from netstoreapp.models import UserProfile,Classify,Commodity
from django.contrib.auth.models import User
from netstoreapp.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def ISlogin(request, context_dict):
    if request.user.is_authenticated():
        context_dict['ISlogin'] = "已登陆"
    else:
        context_dict['ISlogin'] = "未登陆"

# Create your views here.


def index(request):
    '''主页'''
    context_dict = {}
    ISlogin(request, context_dict)
    classify_list=Classify.objects.order_by('name')[:5]
    context_dict['classify']=classify_list

    return render(request, 'netstore/index.html', context_dict)


def userlogin(request):
    '''登陆页面'''
    context_dict = {}
    ISlogin(request, context_dict)
    if request.method == 'POST':
        username = request.POST.get('FUsername')
        password = request.POST.get('FPassword')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/netstoreapp/')
            else:
                context_dict[
                    'LogErr'] = "Your itcastsubject account is disabled."
        else:
            context_dict['LogErr'] = "Invalid login details:{0},{1}".format(
                username, password)
    else:
        context_dict['LogErr'] = ""
    return render(request, 'netstore/userlogin.html', context_dict)


@login_required
def chdata(request):
    '''修改资料'''
    context_dict = {}
    ISlogin(request, context_dict)

    return render(request, 'netstore/chdata.html', context_dict)


@login_required
def chpwd(request):
    '''修改密码'''
    context_dict = {}
    ISlogin(request, context_dict)

    return render(request, 'netstore/chpwd.html', context_dict)


@login_required
def cart(request):
    '''购物车'''
    context_dict = {}
    ISlogin(request, context_dict)

    print request.user
    userprofile = UserProfile.objects.get(user=request.user)
    print userprofile
    print userprofile.cart

    return render(request, 'netstore/cart.html', context_dict)


@login_required
def mydata(request):
    '''我'''
    context_dict = {}
    context_dict['ISlogin'] = "已登陆"

    return render(request, 'netstore/mydata.html', context_dict)


def register(request):
    '''注册'''
    context_dict = {}
    ISlogin(request, context_dict)

    if request.method == 'POST':

        user = User()
        profile = UserProfile()
        user.username = request.POST.get('FUsername')
        user.password = request.POST.get('FPassword1')
        user.Email = request.POST.get('FEmail')
        profile.phone = request.POST.get('FPhone')
        if user and profile:

            user.set_password(user.password)
            user.save()
            profile.user = user
            profile.save()

            context_dict['IsREG'] = "register succ"

        else:
            context_dict['IsREG'] = "register error"
    else:
        context_dict['IsREG'] = ""
        context_dict['userform'] = UserForm()
        context_dict['userprofile'] = UserProfileForm()
    return render(request, 'netstore/register.html', context_dict)


def commodity(requset):
    '''商品页面'''
    context_dict = {}
    ISlogin(request, context_dict)

    return render(requset, 'netstore/commodity.html', context_dict)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/netstoreapp/')

def classify(request):
	print request.GET.get('classify')
	return render(request,'netstore/index.html',{})

def add(request):
	context_dict={}

	classify_list=Classify.objects.order_by('name')[:5]   	
	print  request.GET.get('classify')
	print type(request.GET.get('classify'))
	return HttpResponseRedirect("/netstoreapp/iframe/")
	for classify in classify_list:
		if classify.name==request.GET.get('classify'):
			context_dict['commodity']=Commodity.objects.filter(classify=classify)
			break;
	
    	
	print context_dict
	return HttpResponse(context_dict)

def iframe(request):
	print "***888*******"
	context_dict={}
	classify_list=Classify.objects.order_by('name')[:5]
	context_dict['classify']=classify_list

	clas = request.GET.get('classify')
	print request.GET
	print clas
	if clas:
		for classify in classify_list:
			if classify.name==clas:
				context_dict['commodity']=Commodity.objects.filter(classify=classify)
				break;
	else:
		
		commodity_list=Commodity.objects.filter(classify=classify_list[1])
		context_dict['commodity']=commodity_list
		

		
	print context_dict
	return render(request,"netstore/iframe.html",context_dict)
	

