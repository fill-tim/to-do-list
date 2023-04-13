from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import NotesList, NoteDelete, note_edit, NoteAdd

urlpatterns = [
    path('', NotesList.as_view(), name='notes'),
    path('main/note_add/', NoteAdd.as_view(), name='note_add'),
    path('main/note_delete/<int:pk>', NoteDelete.as_view(), name='note_delete'),
    path('main/note_edit/<int:pk>', note_edit, name='note_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
