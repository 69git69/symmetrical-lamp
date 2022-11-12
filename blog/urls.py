from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, UserBlogListView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name='home'),
    path("<str:username>/blogs/", UserBlogListView.as_view(), name='usersallblog'),
    path("<str:username>/<slug:slug>/view/", BlogDetailView.as_view(), name='detail'),
    path("<str:username>/<slug:slug>/delete/", BlogDeleteView.as_view(), name='delete'),
    path("<str:username>/<slug:slug>/edit/", BlogUpdateView.as_view(), name='update'),
    path("create/", BlogCreateView.as_view(), name='create'),
]
