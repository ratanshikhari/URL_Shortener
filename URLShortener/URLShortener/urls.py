
from django.contrib import admin
from django.urls import path
from authentication.views import  login, signup, logout
from urlhandler.views import dashboard, genarate,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('genarate/', genarate, name="genarate"),
    path('<str:query>/', home, name="home"),
]
