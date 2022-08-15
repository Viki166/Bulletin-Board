from re import template
from django.shortcuts import render
from django.views.generic import View , ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad, Response, Game
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import AdForm, ResponseForm
from django.shortcuts import redirect


class AdsListView(ListView):
    model = Ad
    template_name = "ads/ads.html"
    context_object_name = 'ads'
    queryset = Ad.objects.all().order_by('-id')
    ordering = ['-id']
    paginate_by = 3

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AdForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context


class DetailAd(DetailView):
    model = Ad
    template_name = "ads/ad.html"
    context_object_name = 'ad'
    pk_url_kwarg = "pk"
    form_class = ResponseForm


class AdCreate(CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_create.html'


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


class Response(ListView):
    model = Response
    template_name = "ads/response.html"
    context_object_name = 'responses'
    permission_required = ''
    


def GameList(request, game):
    list = Game.objects.filter(name=game)
    Ads = Ad.objects.filter(game=game)
    return render(request, 'ads/game.html',{'list': list, 'Ads':Ads})
