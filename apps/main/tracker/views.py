from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Entry
from .forms import EntryForm

def admin_portal(request):
    """Handles the Admin Portal CRUD interface."""
    entries = Entry.objects.all()
    form = EntryForm()
    
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            # If request is from HTMX, return a success signal to refresh the list
            if request.headers.get('HX-Request'):
                return HttpResponse(status=204, headers={'HX-Trigger': 'entryChanged'})
            return redirect('admin_portal')
            
    return render(request, 'admin.html', {'entries': entries, 'form': form})

def edit_entry(request, pk):
    """Handles editing an existing entry."""
    entry = get_object_or_404(Entry, pk=pk)
    
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save()
            if request.headers.get('HX-Request'):
                # Return the updated row
                return render(request, '_entry_row.html', {'entry': entry})
            return redirect('admin_portal')
    else:
        form = EntryForm(instance=entry)
    
    return render(request, '_edit_form.html', {'form': form, 'entry': entry})

def delete_entry(request, pk):
    """Deletes an entry and triggers a UI update."""
    entry = get_object_or_404(Entry, pk=pk)
    entry.delete()
    return HttpResponse(status=204, headers={'HX-Trigger': 'entryChanged'})

def user_portal(request):
    """The main User Portal grid view."""
    return render(request, 'user.html')

def table_rows(request):
    """API-like endpoint returning ONLY table rows for real-time polling."""
    entries = Entry.objects.all()
    return render(request, '_rows.html', {'entries': entries})

def admin_entries_list(request):
    """API-like endpoint returning ONLY the entries table for HTMX updates."""
    entries = Entry.objects.all()
    return render(request, '_admin_entries_table.html', {'entries': entries})