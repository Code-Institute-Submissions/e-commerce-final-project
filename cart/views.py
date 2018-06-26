from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Product

# Create your views here.
def view_cart(request):
    return render(request, "cart/cart.html")
    
def add_to_cart(request):

    # Get the product we're adding
    id = request.POST['product_id']
    phone = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', {})
    
    # Update the Cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return HttpResponse(cart[id])