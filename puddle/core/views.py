from django.shortcuts import render
from item.models import Item, Category
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    }) # In curly brackets, it is specified which data can be called upon in the template - in this case, the template will be able to access the categories and items defined in this view

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form':form # For passing the form to the Front-End
    })