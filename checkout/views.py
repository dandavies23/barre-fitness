from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        # messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L0nA2A84B7t9lNC4vqC5DNCJ0fjw4CuaEfjTuv7SW4U0EdzZGB3jV5l6gBxZdFceU71Meew7W0Pl4IWS4IWYlPv00gcC0zf6u',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
