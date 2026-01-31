from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

def just_for_display_menu():
    print('POS System') 
    print('1. Add item to cart') 
    print('2. Remove item from cart')
    print('3. Process payment') 
    print('4. Exit')
    menu_choice = int(input('Choose an option: '))
    if menu_choice == 4:
        print('Goodbye!')
        exit()
    else:
        print('Enjoy Shopping!') 
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

def remove():
    pass
def payment():
    pass
