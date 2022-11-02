from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.PostList.as_view(),name = 'blog'),
    path('<slug:slug>/',views.PostDetail.as_view(),name = "post_detail"),
]