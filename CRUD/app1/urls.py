from django.urls import path
from .views import profileView,orderView,profileData,updateView,deleteView


urlpatterns =  [

    path('profile/', profileView, name='profileview'),
    path('order/', orderView, name='orderview'),
    path('profiledata/', profileData, name='profiledata' ),
    path('update/<int:id>/', updateView, name='update' ),
    path('delete/<int:id>/', deleteView, name='delete')


]