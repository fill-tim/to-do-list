from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import NoteEditForm
from .models import Note


# Create your views here.
class NotesList(generic.ListView):
    """
    Вывод списка заметок
    """
    model = Note
    template_name = 'main/notes.html'
    context_object_name = 'note'

    def get_queryset(self):
        return super().get_queryset().filter(autor=self.request.user.id)


class NoteDelete(generic.DeleteView):
    """
    Удаление заметки
    """
    model = Note
    success_url = reverse_lazy('notes')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def note_edit(request, pk):
    """
    Редактирование заметки
    """
    model = get_object_or_404(Note, pk=pk)
    form = NoteEditForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('notes')

    contex = {
        'form': form,
        'model': model
    }
    return render(request, 'main/note_edit.html', contex)


class NoteAdd(generic.CreateView):
    """
    Доабвление заметки
    """
    form_class = NoteEditForm
    template_name = 'main/note_add.html'
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        model = get_object_or_404(User, username=self.request.user.username)
        self.object.autor = model
        return super().form_valid(form)
