from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post

# Create your views here.
blog_title = 'New blogs...'      
   
# Posts=[
#     {'id':1,'title':'Post 1','content':'Python Introduction'},
#     {'id':2,'title':'Post 2','content':'Data Structure And Algorithms'},
#     {'id':3,'title':'Post 3','content':'Machine learning'},
#     {'id':4,'title':'Post 4','content':'GUI Applications'},
#     {'id':5,'title':'Post 5','content':'Django Project'},

# ]
else_handeler = '404 FOUND CHECK CODE'

def index (request):
    Posts = Post.objects.all()
    return render(request,"index.html",{'blog_title':blog_title,'Posts':Posts,'else_handeler':else_handeler})

def detail(request ,post_id):
    post = Post.objects.get(pk=post_id)
    # post = next((item for item in Posts if item['id']== int(post_id)),None)
    # logger = logging.getLogger("testing")
    # logger.debug(f'the post value is {post}')
    
    return render(request,'detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))
def new_url_view(request):
    return HttpResponse("this is a new url")