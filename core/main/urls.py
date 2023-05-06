from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail-page/', views.detail_page, name='detail-page'),
    path('listing-page/detail-page.html', views.detail_page, name='detail-page'),
    path('listing-page/', views.listing_page, name='listing-page')
]