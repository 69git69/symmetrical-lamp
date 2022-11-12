from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import render
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  DeleteView,
                                  TemplateView)
from django.views.generic.edit import UpdateView
from blog.models import Blog
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.


class BlogListView(ListView):
    template_name = 'blog/home.html'
    model = Blog
    context_object_name = 'blog_list'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-publish_datetimestamp')
    

class UserBlogListView(ListView):
    template_name = 'blog/user_blogs.html'
    model = Blog
    context_object_name = 'blog_list'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user.id).order_by('-publish_datetimestamp')
    

class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Blog
    context_object_name = 'blog'
    slug_field = 'slug'

class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/edit.html'
    fields = ['title', 'content']
    permission_denied_message = 'hahahhaahah'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create.html'
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'blog/delete.html'
    model = Blog

    def test_func(self):
        print(self.request)
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        success_url = reverse_lazy('blog:usersallblog', kwargs={"username": self.request.user.username})
        self.object.delete()
        return HttpResponseRedirect(success_url)
