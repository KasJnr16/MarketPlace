from django.shortcuts import render, redirect
from item.models import(
    Category,
    Item,
)

from .forms import(
    SignUpForm
)
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] #The array is used to grab 6 items from the Item_model
    categories = Category.objects.all() 
     
    return render(request, 'core/index.html',{
        "categories": categories,
        "items": items,
    })

def contact(request):
    return render(request, 'core/contact.html') 

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    return render(request, "core/signup.html",{
        "form":form
    })