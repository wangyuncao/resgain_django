
from django.urls import path
from api import views

urlpatterns = [
    path('resgain/', views.resgain, name='resgain'),
    path('complete/', views.complete, name='complete'),
    path('resgain_api/', views.Resgain.as_view()),
    path('complete_api/', views.Complete.as_view()),
]
