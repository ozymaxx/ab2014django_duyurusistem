from django.shortcuts import render, render_to_response
<<<<<<< HEAD
from models import *
=======
>>>>>>> 727daea6bf53b371b5af5904deb271983134c879

# Create your views here.
from django.db.models import Q

def create_post( request):
    pass
	
def signup( request):
	pass

def post_search( request):
    return render_to_response("posts.html")
	
@login_required(login_url="/duyurular/login")
def single_post( request, post_id):
<<<<<<< HEAD
	post = Posts.objects.get(id=post_id)
	if post is not None:
		return redirect("/duyurular/posts")
	else:
		c = {"post":post}
		return render_to_response("duyurular/single_post.html",c)
=======
    pass
>>>>>>> 727daea6bf53b371b5af5904deb271983134c879
	
@login_required(login_url="/duyurular/login")	
def daily_post( request, year, month, day):
<<<<<<< HEAD
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
=======
    pass
	
def login( request):
    pass
>>>>>>> 727daea6bf53b371b5af5904deb271983134c879
