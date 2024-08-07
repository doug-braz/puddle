from django.shortcuts import render, redirect
from django.contrib import auth
from item.models import Item, Category
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    query = request.GET.get('query','')

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
        'query' : query,
    }) # In curly brackets, it is specified which data can be called upon in the template - in this case, the template will be able to access the categories and items defined in this view

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form':form # For passing the form to the Front-End
    })

def logout(request):
    auth.logout(request)
    return redirect('/')
