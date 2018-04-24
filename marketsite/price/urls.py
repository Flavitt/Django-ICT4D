from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:crop_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:crop_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:crop_id>/giveprice/', views.giveprice, name='giveprice'),
]