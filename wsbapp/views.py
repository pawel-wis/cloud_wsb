from django.shortcuts import render
from django.http import HttpResponse
from .forms import NoteForm
from .models import Note

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)


def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)


def add(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'add.html', context)