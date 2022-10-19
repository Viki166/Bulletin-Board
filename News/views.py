from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Response
from .forms import PostForm
from Ads.models import Users
class PostList(ListView):
    model = Post
    template_name='news/posts.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name= 'post'


class PostCreate(CreateView):
    model = Post
    form_class= PostForm  
    template_name = 'news/post_create.html'  
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.user = Users.objects.get(user=request.user)
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PostUpdate(UpdateView):
    model = Post
    template_name = 'news/post_update.html'
    form_class = PostForm
    success_url = ''

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'news/post_delete.html'


