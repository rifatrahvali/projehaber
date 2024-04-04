
from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path("abouts/",AboutView.as_view(),name="abouts"),
    path("notices/",NoticesView.as_view(),name="notices"),
    path("news/",NewsView.as_view(),name="news"),
    path("contacts/",ContactsView.as_view(),name='contacts'),
    path('news/<slug:slug>/',NewsDetailView.as_view(),name='news-detail'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(),name='category-detail'),
    path('search/',NewsSearchView.as_view(),name='news-search'),
]
