from django.urls import path

from .views import logout_user, LoginUser, RegisterUser

urlpatterns = [
    path('authentication/logout/', logout_user, name='logout'),
    path('authentication/login/', LoginUser.as_view(), name='login'),
    path('authentication/register/', RegisterUser.as_view(), name='register'),
]