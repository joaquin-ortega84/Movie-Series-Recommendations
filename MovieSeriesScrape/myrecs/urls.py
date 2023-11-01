from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_view, name='movies'),
    path('series/', views.series_view, name='index'),
    path('making/', views.making_view, name='making')
]
