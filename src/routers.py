from django.urls import include, path

urlpatterns = [
    path('', include('src.authentication.urls')),
    path('', include('src.main.urls')),
]
