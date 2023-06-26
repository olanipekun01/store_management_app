from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.index, name='index'),
    path('micro', views.micro, name='micro'),
    path('haem', views.haem, name='haem'),
    path('chem', views.chem, name='chem'),
    path('histo', views.histo, name='histo'),
    path('history/<int:pk>', views.history, name='history'),
    path('itemHistory/<int:pk>/<str:slug>', views.ItemHistory, name='itemHistory'),
    path('newstock', views.newstock, name='newstock'),
    path('delete/<str:slug>', views.delete, name='delete'),
    path('login', views.login, name='login'),
    path("logout", views.logout, name="logout"),
]