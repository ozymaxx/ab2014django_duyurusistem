from django.shortcuts import render, render_to_response
from models import *

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
		return redirect('/duyurular/index')
	else:
		form = CampaignForm()
		c = {"form": form}
		c.update(csrf(request))
		return render_to_response('duyurular/create_post.html',c)                                         
        
def signin( request ):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'],
			password=request.POST['password'])
			if user is not None:
				auth.login(request, user)
				return redirect('/duyurular/index')
	c = {}
	c.update(csrf(request))
	return render_to_response('duyurular/signin.html',c)
	
def signup( request):
	pass

def post_search( request):
    return render_to_response("posts.html")
	
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
		
def login( request):
	if request.user.is_authenticated():
		return redirect("/duyurular/posts")
	else:
		return render_to_response( "duyurular/login.html")
