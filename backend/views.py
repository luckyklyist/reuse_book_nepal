from multiprocessing import context
from venv import create
from django.shortcuts import redirect, render
from requests import delete
from .models import product,proflie_users,ask_question,reply_ask
from .forms import upload_book,profile_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
# from allauth.app_settings import USER_MODEL
# from allauth.account.models import EmailAddress

def index(request):
    products=product.objects.all()
    context={
        "products":products
    }
    return render(request,"index.html",context)

def buy_books(request):
    products=product.objects.all()
    context={
        "products":products
    }
    return render(request,"buybooks.html",context)

def search_books(request):
    query=request.GET["search"]
    products=product.objects.filter(product_name__icontains=query)
    context={
        "products":products
    }
    return render(request,"searchbook.html",context)


def book_detail(request,slug):
    book_detail_info=product.objects.get(slug=slug)
    ask_questions=ask_question.objects.filter(post__slug=slug)
    reply=reply_ask.objects.all()
    context={
        "product":book_detail_info,
        "questions":ask_questions,
        "reply":reply,
    }
    if request.method=="POST":
        ask_que=request.POST.get("ask")
        ask_id=request.POST.get("pk_id")
        if ask_que is not None:
            print(f"===================================================={ask_que}")
            print(request.user)
            ask=ask_question(post=book_detail_info,username=request.user.username,date_posted=datetime.today(),questions=ask_que,id_ask=ask_id)
            ask.save()
            return redirect("book",slug)
    # if request.method=="POST":
    #     rep=request.POST.get("reply")
    #     ask__it=ask_question.objects.get(questions=rep)
    #     if rep is not None:
    #         reply_user=reply_ask(comment=ask_question,date_posted=datetime.today(),reply=rep)
    #         reply_user.save()
    #         return redirect("book",slug)

    return render(request,"product_detail.html",context)

def reply_post(request,slug):
    if request.method=="POST":
        rep=request.POST.get("reply")
        id_ak=request.POST.get("id")
        id_question=request.POST.get("id_question")
    
        print(f"================================================{rep}")
        ask__it=ask_question.objects.get(id=id_question,post__slug=slug)
        if rep is not None:
            reply_user=reply_ask(id_reply=id_question,username=request.user,comment=ask__it,date_posted=datetime.today(),reply=rep,)
            reply_user.save()
            # return redirect("book")
        print("Hello world from the reply bar ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return redirect("book",slug)

@login_required(login_url="account_login")
def sell_book(request):
    if request.method=="POST":
        form=upload_book(request.POST,request.FILES)
        if form.is_valid():
            form_user=form.instance
            form_user.seller=request.user
            form_user.save()
            return redirect("home")
    else:
        form=upload_book
        context={
            "form":form
        }    
    return render(request,"sell_book.html",context)

@login_required(login_url="account_login")
def user_profile(request,slug):
    profile=proflie_users.objects.get(username=slug)
    # userrr=User.objects.get(username=slug)
    ads=product.objects.filter(seller=slug)
    context={
        "profile":profile,
        "ads":ads,
    }
    return render(request,"user_profile.html",context)

@login_required(login_url="account_login")
def create_user_profile(request):
    if request.method=="POST":
        form=profile_form(request.POST,request.FILES)
        if form.is_valid():
            form_profile=form.instance
            form_profile.username=request.user
            form_profile.save()
            return redirect("home")
    else:
        form=profile_form()
        context={
            "form":form
        }
    return render(request,"profileform.html",context)

def edit_ads(request,slug):
    inst=product.objects.get(slug=slug)
    if request.method=="POST":
        form=upload_book(request.POST or None,request.FILES or None,instance=inst)
        if form.is_valid():
            form.save(commit=False)
            form_user=form.instance
            form_user.seller=str(request.user)
            form_user.save()
            return redirect("profile",inst.seller)
    else:
        form=upload_book(instance=inst)
        context={
            "form":form 
        }
    return render(request,"edit_ads.html",context)

def delete_ads(request,slug):
    # product.objects.delete(slug=slug)
    del_list=product.objects.get(slug=slug)
    del_list.delete()
    return redirect("profile",del_list.seller)

def ads_completed(request,slug):
    if request.method=="POST":
        complete_ads=product.objects.create