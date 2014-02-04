from django.shortcuts import render, render_to_response

# Create your views here.

def create_post( request):
    pass
	
def signup( request):
	pass

def post_search( request):
    return render_to_response("posts.html")
	
def single_post( request, post_id):
    pass
	
def daily_post( request, year, month, day):
    pass
	
def login( request):
    pass
