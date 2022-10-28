from django.shortcuts import render, get_object_or_404 
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad, Comment,  Game, Users, User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .forms import AdForm, CommentForm
from .filters import CommentsFilter
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = Comment.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            ad = self.get_object()
            form.instance.ad = ad
            form.instance.user = Users.objects.get(user=request.user)
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('ad_detail',kwargs={'pk':self.get_object().id})



class AdCreate(CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_create.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AdForm
        return context

    def post(self, request, *args, **kwargs):
        form = AdForm(request.POST)
        if form.is_valid():
            form.instance.user = Users.objects.get(user=request.user)
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('ads')


class AdUpdateView(UpdateView):
    template_name = 'ads/ad_create.html'
    form_class = AdForm
    model = Ad
    success_url = reverse_lazy('ads')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)



class AdDeleteView(DeleteView):
    template_name = 'ads/ad_delete.html'
    queryset = Ad.objects.all()
    success_url = reverse_lazy('ads')


class Comments(ListView):
    model = Comment
    template_name = "ads/comment.html"
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Users.objects.get(user=self.request.user)
        context['filter'] =  CommentsFilter(self.request.GET, queryset=Comment.objects.all())
        return context


def updateCommentActive(request, pk, type):
    comment = Comment.objects.get(pk=pk)
    if type == 'public':
        comment.active = True
        comment.save()
        template = Template('''<div class="post-content"><p>Комментарий опубликован.</p></div>''')
        context = Context({'comment':comment})
        return HttpResponse(template.render(context))
    elif type =='delete':
        comment.delete()
        template = Template('''<div class="post-content"><p>Комментарий удален.</p></div>''')
        context = Context({'comment':comment})
        return HttpResponse(template.render(context))
    return HttpResponse('444')


class AddCommentLike(View):
    
    def post(self,request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        is_dislike = False
        for dislike in comment.dislikes.all():
           
            if dislike == request.user:
               
                is_dislike= True
                break
        if is_dislike:
            comment.dislikes.remove(request.user.id)
            is_dislike = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            comment.likes.add(request.user)
        if is_like:
            comment.likes.remove(request.user)
           
        return HttpResponseRedirect('ads')
        

class AddCommentDislike(View):
    def post(self,request, pk,*args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like= True
                break
        if is_like:
            comment.likes.remove(request.user)
            is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike:
            comment.dislikes.add(request.user)
        if is_like:
            comment.dislikes.remove(request.user)
        return HttpResponseRedirect('ads')
    

def GameList(request, game):
    list = Game.objects.filter(name=game)
    Ads = Ad.objects.filter(game=game)
    return render(request, 'ads/game.html',{'list': list, 'Ads':Ads})


# from Ads.tasks import my_first_task

# def index(request):
#     my_first_task.delay(10)
#     print('is this True!!!')
#     return HttpResponse('response done')

