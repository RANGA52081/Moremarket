from .models import Cart

def cart_data(request):

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_count = cart.items.count()
        total_price = cart.total_price()
    else:
        cart = None
        cart_count = 0
        total_price = 0

    return {
        "cart": cart,
        "cart_count": cart_count,
        "cart_total": total_price
    }