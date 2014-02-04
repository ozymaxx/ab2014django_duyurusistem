from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from models import *
from forms import *
from django.forms import *

# Create your views here.
from django.db.models import Q

@login_required(login_url='/duyurular/login')
def create_post( request ):
	if request.method == 'POST':
		form = CreatePostForm(request.POST)
	if form.is_valid():
		post = Post( title=form.cleaned_data.get('title'),
			content=form.cleaned_data.get('content'),
			upvote=form.cleaned_data.get('upvote'),
			downvote=form.cleaned_data.get('downvote'),
			created_at=form.cleaned_data.get('created_at'),
			created_by=request.POST['id'])

		post.save()
		return redirect('/index')
	else:
		form = CampaignForm()
		c = {"form": form}
		c.update(csrf(request))
		return render_to_response('duyurular/create_post.html',c)                                         

def login(request ):
    if request.user.is_authenticated():
        return redirect("/posts")
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        print user
        if user is not None:
            auth.login(request, user)
            return redirect('/posts')
    form = LoginForm(request.POST)
    c = {'form':form}
    c.update(csrf(request))
    return render_to_response('login.html',c)
	
def signup( request):
	pass

@login_required(login_url='/login/')
def post_search( request ):
    if request.method == 'POST':
        form = PostSearchForm(request.POST)
        if form.is_valid():
            tags=form.cleaned_data.get('tags')
            word=form.cleaned_data.get('word')

            tags = tags.split(',')
            posts = Post.objects.select_related('pt_post',
            'pt_tag').filter(pt_tag__content__contains=word)

            result = []

            for tag in tags:
                list = posts.filter( pt_tag__text=tag )
                result.append(list)
                result = set(result)

            return render_to_response("duyurular/post_search.html",{'campaign_list':campaign_list,'word': word})
    form = PostSearchForm()
    c = {"form": form}
    c.update(csrf(request))
    return render_to_response('posts.html',c)
	
@login_required(login_url="/duyurular/login")
def single_post( request, post_id):
	post = Posts.objects.get(id=post_id)
	if post is not None:
		return redirect("/duyurular/posts")
	else:
		c = {"post":post}
		return render_to_response("duyurular/single_post.html",c)
	
@login_required(login_url="/duyurular/login")	
def daily_post( request, year, month, day):
	daily_posts = Posts.objects.filter(Q(created_at__lte=year+"-"+month+"-"+day+" "+"23:59")&Q(created_at_gte=year+"-"+month+"-"+day+" "+"00:00"))
	if daily_posts is not None:
		return redirect("/duyurular/posts")
	else:
		c = {"daily_posts":daily_posts}
		return render_to_response("duyurular/daily_posts.html",c)