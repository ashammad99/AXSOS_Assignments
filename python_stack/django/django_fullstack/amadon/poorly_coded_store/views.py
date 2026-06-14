from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum
from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout(request):
    if request.method == "POST":
        # Process the order
        try:
            quantity_from_form = int(request.POST.get("quantity", 0))
            product_id_from_form = int(request.POST.get("product_id", 0))
            product = get_object_or_404(Product, id=product_id_from_form)
        except (ValueError, TypeError):
            return redirect("/")

        if quantity_from_form <= 0:
            return redirect("/")

        if quantity_from_form > product.quantity:
            print("Not enough inventory!")
            return redirect("/")

        # Calculate total using server-side price (prevents price manipulation)
        total_charge = quantity_from_form * product.price

        # Create the order with product reference
        order = Order.objects.create(
            quantity_ordered=quantity_from_form,
            total_price=total_charge
        )

        # Update inventory
        product.quantity -= quantity_from_form
        product.save()

        # Redirect to GET endpoint to prevent accidental re-orders on refresh
        return redirect("/checkout/confirmation/")

    # GET request - display order statistics
    return render(request, "store/checkout.html")


def confirmation(request):
    """Show order confirmation page after successful order (GET only)"""
    all_orders = Order.objects.all()
    most_recent_order = all_orders.last()
    orders_count = all_orders.count()

    total_quantity = all_orders.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum'] or 0
    total_amount = all_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    context = {
        "most_recent_order": most_recent_order,
        "total_quantity": total_quantity,
        "total_amount": total_amount,
        "orders_count": orders_count
    }
    return render(request, "store/checkout.html", context)