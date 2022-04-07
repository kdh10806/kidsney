import json

from django.views import View
from django.http import JsonResponse, HttpResponse
from decimal import Decimal

from .models import Account
from carts.models import Cart
from utilities.decorators import check_token

class OrderView(View):
    @check_token
    def post(self, request):
        data        = json.loads(request.body)
        carts       = Cart.objects.filter(user = request.user)
        total_price = Decimal(data['total_price'])
        account     = Account.objects.get(user = request.user)

        
        if not account.balance >= total_price:
            return JsonResponse({'message' : 'moneyless'}, status = 400)

        for cart in carts:
            if cart.quantity > cart.product_size.stock:
                return JsonResponse({'message' : 'stockless'}, status = 400)
            else: 
                cart.product_size.stock -= cart.quantity
                cart.product_size.save()

        account.balance -= total_price
        account.save()
        carts.delete()

        return HttpResponse(status=200)

class CashView(View):
    @check_token
    def post(self, request):
        data = json.loads(request.body)
        cash = data['cash']

        Account.objects.create(name = 'KB', user=request.user, balance = cash)