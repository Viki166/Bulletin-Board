from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad, Comment,  Game
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import AdForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin

class AdsListView(ListView):
    model = Ad
    template_name = "ads/ads.html"
    context_object_name = 'ads'
    queryset = Ad.objects.all().order_by('-id')
    ordering = ['-id']
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        context['form'] = AdForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
    
   


class DetailAd(FormMixin, DetailView):
    model = Ad
    template_name = "ads/ad.html"
    context_object_name = 'ad'
    form_class = CommentForm
    success_url='/ads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            ad = self.get_object()
            form.instance.ad = ad
            form.instance.user = request.user
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class AdCreate(CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_create.html'
    success_url = '/ads'

class AdUpdateView(UpdateView):
    template_name = 'ads/ad_create.html'
    form_class = AdForm
    model = Ad

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)


class AdDeleteView(DeleteView):
    template_name = 'ads/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = '/'


class Comment(ListView):
    model = Comment
    template_name = "ads/comment.html"
    context_object_name = 'comments'
    

def GameList(request, game):
    list = Game.objects.filter(name=game)
    Ads = Ad.objects.filter(game=game)
    return render(request, 'ads/game.html',{'list': list, 'Ads':Ads})
