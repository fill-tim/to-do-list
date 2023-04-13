from django import forms
from .models import Note


class NoteEditForm(forms.ModelForm):
    """
    Форма для редактирования заметки
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs[
            'style'] = 'width:400px; height:40px; border-radius: 10px; border: 1px solid #8C4162; background: #F5C5DF'
        self.fields['description'].widget.attrs[
            'style'] = 'width:300px; height:100px; border: 1px solid #8C4162; border-radius: 10px;  background: #F5C5DF'
        self.fields['importance'].widget.attrs[
            'style'] = 'border-radius: 10px; border: 1px solid #8C4162;  background: #F5C5DF'

    class Meta:
        model = Note
        exclude = ['autor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form', }),
            'description': forms.Textarea(attrs={'class': 'form ', }),
        }

