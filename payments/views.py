from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import redirect
import stripe

from product.models import Product
from decouple import config


class StripeCheckoutSessionViewSet(viewsets.ViewSet):
    stripe._api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
    YOUR_DOMAIN = 'http://localhost:8000'


    @action(detail=False, methods=['post'])
    def create_checkout_session(self, request):
        product_id = request.data.get('product_id')

        try:
            product = Product.objects.get(pk=product_id)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Здесь можно указать идентификатор цены продукта в Stripe
                        'price': product.price.id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=self.YOUR_DOMAIN + '?success=true',
                cancel_url=self.YOUR_DOMAIN + '?canceled=true',
            )
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=400)

        return redirect(checkout_session.url, code=303)
