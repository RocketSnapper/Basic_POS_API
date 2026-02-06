from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from decimal import Decimal

def just_for_display_menu():
    print('POS System') 
    print('1. Add item to cart') 
    print('2. Remove item from cart')
    print('3. Process payment') 
    print('4. Exit')
    menu_choice = int(input('Choose an option: '))
    if menu_choice == 4:
        print('Goodbye!')
        Product.objects.all().delete()
        exit() 
    else:
        print('Enjoy shopping!') 
just_for_display_menu()

@api_view(['POST'])
def add(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            print(f'Added {validated["quantity"]} x {validated["item_name"]} to cart.')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['DELETE'])
def remove(request, pk):
    product = get_object_or_404(Product, pk = pk)
    if request.method == 'DELETE':
        print(f'Removed {product.quantity} x {product.item_name} from cart.')
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])    
def payment(request):
    if request.method == 'GET':
        products = Product.objects.all()
        total_price = Decimal('0.00')
        print('Items in Cart:')
        for product in products:
            if product.price > 0.00:
                inital_price = product.price
                if product.quantity > 1:
                    quantity = Decimal(product.quantity)
                    product.price = quantity * product.price
                total_price += product.price
            print(f'{product.item_name}: {product.quantity} x ${inital_price} = ${product.price}')
        print(f'Total: ${total_price}')
        cash = Decimal('100000.00')
        card = Decimal('100000.00')
        payment_method = input('Select payment method (cash/card): ')
        if payment_method == 'cash':
            cash = cash - total_price
            print(f'Payment of ${total_price} made using {payment_method}. Thank you for your purchase!')
        elif payment_method == 'card':
            card = card - total_price
            print(f'Payment of ${total_price} made using {payment_method}. Thank you for your purchase!')
        Product.objects.all().delete()
        return Response(status = status.HTTP_200_OK)
    




