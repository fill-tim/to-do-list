from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import NotesList, NoteDelete, note_edit, NoteAdd, LoginUser, logout_user, RegisterUser

urlpatterns = [
    path('', NotesList.as_view(), name='notes'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('note_add/', NoteAdd.as_view(), name='note_add'),
    path('note_delete/<int:pk>', NoteDelete.as_view(), name='note_delete'),
    path('note_edit/<int:pk>', note_edit, name='note_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
