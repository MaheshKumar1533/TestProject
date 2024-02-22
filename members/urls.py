from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('custom_login/', views.custom_login, name="custom_login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('submit/', views.submit, name='submit')
]

urlpatterns += staticfiles_urlpatterns()