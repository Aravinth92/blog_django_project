from django.urls import path
from .import views

app_name='blog'

urlpatterns = [
    path("",views.index,name="index"),
    path("detail/<str:post_id>",views.detail,name="detail"),
    path("old_url",views.old_url_redirect,name="old_url"),
    path("new_url_somthing",views.new_url_view,name="new_url"),
    
]
