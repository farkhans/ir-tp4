from django.urls import path
from .views import search_query, search_page, detail_view

urlpatterns = [
    path('',search_page, name='search_page'),
    path('search/',search_query, name='search_query'),
    path('detail/<str:docno>/',detail_view, name='detail_view')
]
