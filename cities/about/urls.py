from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('postcity',views.postcity,name='cityform'),
    path('cities',views.viewcity,name='cityinfo')
    #all cities (about/cultures) in seperate pages
    # path('humanconf',views.human,name='humanauth'),
]