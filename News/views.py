from .models import News, Category, NewsComment
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import NewsForm

class NewsList(ListView):
    model= News
    template_name='news/news.html'
    context_object_name='all_news'
    queryset = News.objects.all().order_by('-id')
    ordering = ['-id']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewsForm
        return context


class NewsDetail(DetailView):
    model=News
    template_name='news/news-detail.html'


class NewsCreate(CreateView):
    models=News
    template_name='news/news-create.html'
    form_class= NewsForm
