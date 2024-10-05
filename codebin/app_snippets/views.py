from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet
from .forms import SnippetForm

def home(request):
    return render(request, "home.html")

def edit_or_retrieve(request, slug):
    try:
        snippet = Snippet.objects.get(slug=slug)
    except Snippet.DoesNotExist:
        snippet = None

    if request.method == 'POST':
        if snippet:
            form = SnippetForm(request.POST, instance=snippet)
        else:
            form = SnippetForm(request.POST)

        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.slug = slug  # Set the slug from the URL
            snippet.save()
            return redirect('edit_or_retrieve', slug=slug)
    else:
        form = SnippetForm(instance=snippet)

    return render(request, 'edit_or_retrieve.html', {'form': form, 'snippet': snippet})
