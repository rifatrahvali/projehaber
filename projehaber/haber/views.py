from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView


from django.http import HttpResponse
from .models import *
# Haber Uygulamasının Modelleri
from haber.models import *

# - Anasayfa
class IndexView(ListView):
    template_name="index.html"
    context_object_name = 'sliders'
    #Slider modelinden geliyor.
    queryset = Slider.objects.all()
    #for döngüsü ile verileri template'e aktaralım.

    #index sayfasındaki hakkımızda bölümüne veri aktarımı
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Abouts'] = About.objects.first()
        #contexti Services modelin aldık 
        #index html'e Services ile hepsini gönderdik
        #for ile herbir service'i döndürdük
        context['Notices'] = Notice.objects.all()
        context['News'] = News.objects.all()
        return context

class AboutView(TemplateView):
    template_name="abouts.html"
    #about sayfasındaki hakkımızda bölümüne veri aktarımı
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Abouts'] = About.objects.first()
        return context
    
class NoticesView(TemplateView):
    template_name="notices.html"
    context_object_name = 'notice'
    #Slider modelinden geliyor.
    queryset = Notice.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Notices'] = Notice.objects.all()
        return context

class NewsView(TemplateView):
    template_name="news.html"
    context_object_name = 'News'
    queryset = News.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['News'] = News.objects.all()
        context['Categories'] = Category.objects.all()
        return context
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'news-details.html'
    context_object_name = 'newsone'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()
        return context

class ContactsView(TemplateView):
    template_name="contacts.html"

class CategoryDetailView(ListView):
    model = News
    template_name = 'category-details.html'
    context_object_name = 'News'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = Category.objects.get(slug=slug)
        return News.objects.filter(category=category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()
        return context



class NewsSearchView(ListView):
    model = News
    template_name = 'news-search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return News.objects.filter(title__icontains=query)
        return News.objects.none()
    

# - Haber
# - Kategori
# - hakkımızda
# - iletişim
# - Hizmetler
# - Ayarlar