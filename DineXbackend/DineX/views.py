from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

# API Views for Product
@api_view(['GET'])
def product_list(request):
    """
    Retrieve all products
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    """
    Create a new product
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_detail(request, pk):
    """
    Retrieve a single product by ID
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['PUT'])
def product_update(request, pk):
    """
    Update a product by ID
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def product_delete(request, pk):
    """
    Delete a product by ID
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def product_cards_view(request):
    """
    Render products as cards in HTML template
    """
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def homepage_view(request):
    """
    Render the homepage with products
    """
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})

def logout_view(request):
    """
    Handle user logout
    """
    # Clear the session completely
    request.session.flush()
    
    # Django logout
    logout(request)
    
    # Add a message
    messages.info(request, "You have successfully logged out.")
    
    # Redirect to login page
    return redirect('DineXlogin')

def login_view(request):
    """
    Handle user login
    """
    # If user is already authenticated, redirect to homepage
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have been successfully logged in!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'DineXlogin.html')

def signup_view(request):
    """
    Handle user registration
    """
    # If user is already authenticated, redirect to homepage
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        dob = request.POST.get('dob', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        country = request.POST.get('country', '')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'DineXsignup.html')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'DineXsignup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'DineXsignup.html')
        
        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name.split(' ')[0],
            last_name=' '.join(name.split(' ')[1:]) if len(name.split(' ')) > 1 else ''
        )
        
        # Save additional profile information
        # Note: In a production environment, you would want to create a separate Profile model
        # For now, we'll store this information in the user's first_name and last_name fields
        # or in custom fields if you extend the User model
        
        messages.success(request, 'New account created successfully! You can now log in.')
        return redirect('DineXlogin')
    
    return render(request, 'DineXsignup.html')
