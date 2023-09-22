from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.members, name='Choose UserType'),
    path('signup', views.signup, name="Sign Up"),
    path('login', views.login, name="Login"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('submit', views.submit, name='submit')
]

urlpatterns += staticfiles_urlpatterns()