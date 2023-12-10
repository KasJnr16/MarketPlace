from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import(
    Item,
    Category,
    ShoppingCart,
    CartItem,

)
from .forms import(
    NewItemForm,
    EditItemForm,
)

# Create your views here.

@login_required()
def items(request):
    query = request.GET.get("query", "")
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,"item/items.html", {
        "items": items,
        "query": query,
        "categories": categories,
        "category_id": int(category_id),
    })

@login_required
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, "item/detail.html",{
        "item":item,
        "related_items":related_items
    })

@login_required
def newitem(request): 
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)
        
    else:
         form = NewItemForm()

    return render(request, "item/form.html",{
        "form": form,
        "title":"New item"
    })

@login_required
def edit(request, pk): 
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, "item/form.html", {
        "form": form,
        "title": "Edit item"
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, item=item)

    if not created:
        cart_item.quantity +=1
        cart_item.save()
    
    return redirect("/")

from django.shortcuts import get_object_or_404, redirect
from .models import Item, ShoppingCart, CartItem

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("item:cart_view")

    
def cart_view(request):
    user_cart = get_object_or_404(ShoppingCart, user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_price = sum(cart_item.item.price * cart_item.quantity for cart_item in cart_items)
    
    return render(request, "item/cart_view.html", {
        "cart_items": cart_items,
        "total_price": total_price,
        "user_cart": user_cart,
    })
        