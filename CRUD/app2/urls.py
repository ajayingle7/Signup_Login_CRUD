from django.urls import path
from .views import signupView,loginView,logutView


urlpatterns  =[

    path('signup/', signupView, name='signup'),
    path('login/', loginView, name='login'),
    path('logout/', logutView ,name='logout')



]