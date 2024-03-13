from django.urls import path
from apps.login.views import index, login_view

urlpatterns = [
    path('', login_view, name='login'),
    #path('login/', login_view, name='login'),
]