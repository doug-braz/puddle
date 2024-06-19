from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import NewItemForm

from django.contrib.auth.decorators import login_required

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detail.html', {
        'item' : item,
        'related_items' : related_items
        })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False) # This is required so that the files from the form are not directly saved into the database, because not all fields from the database comes from the form - e.g. the user
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
        
        else:
            form = NewItemForm()

    return render(request, 'item/form.html', {
        'form':form,
        'title': 'New item'
    })