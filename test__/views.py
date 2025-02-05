# views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.http import FileResponse
from django.core.cache import cache
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        captcha_response = request.data.get('captcha')  # Get CAPTCHA response from frontend

        # Validate CAPTCHA
        captcha_text = cache.get('captcha')  # Get the stored CAPTCHA text from cache
        if not captcha_text or captcha_text != captcha_response:
            return Response({'detail': 'Invalid CAPTCHA'}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with user authentication
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class LoginAPIView(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
#         if user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'access': str(refresh.access_token),
#                 'refresh': str(refresh),
#             })
#         else:
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

# class CaptchaView(APIView):
#     def get(self, request):
#         # Generate a CAPTCHA key
#         captcha_key = CaptchaStore.generate_key()

#         # Generate CAPTCHA image URL based on the key
#         captcha_url = captcha_image_url(captcha_key)

#         # Return the URL of the CAPTCHA image in the response
#         return Response({"captcha_url": captcha_url})

import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.core.cache import cache

# Function to generate CAPTCHA image
from rest_framework.decorators import api_view
import os
from django.templatetags.static import static
from django.conf import settings
# @api_view(['GET'])
def generate_captcha(request):
    # Generate a random 6-character string for the CAPTCHA
    # captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    # font_path = static('fonts/a.JPG')  # This should resolve correctly in both local and live environments
    # image_path = static('static/fonts/a.JPG')
    static_dir = settings.STATIC_ROOT  

    # Full path to the image
    image_full_path = os.path.join(static_dir ,'static' ,'fonts', 'a.JPG')
    print(f"Looking for image at: {image_full_path}")  # Debugging log


    # print("font path",font_path)
    #print(f"Font path: {font_path}")  # Log the font path

    # try:
        # # Create an image using Pillow
        # width, height = 300, 100  # Adjusted size to accommodate larger font
        # image = Image.new('RGB', (width, height), color=(255, 255, 255))
        # draw = ImageDraw.Draw(image)

        # # Use the font from the static directory
        # font = ImageFont.truetype(font_path, 40)  # Increase the font size

        # # Draw the CAPTCHA text on the image
        # text_width, text_height = draw.textsize(captcha_text, font=font)
        # draw.text(((width - text_width) / 2, (height - text_height) / 2), captcha_text, font=font, fill=(0, 0, 0))

        # # Save CAPTCHA text in the cache with a short expiration time
        # cache.set('captcha', captcha_text, timeout=300)  # 5 minutes timeout

        # # Return the image as a response
        # response = HttpResponse(content_type="image/png")
        # image.save(response, "PNG")
        
        # # Allow cross-origin requests
        # response['Access-Control-Allow-Origin'] = '*'
        # response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        # response['Access-Control-Allow-Headers'] = 'Content-Type'

        # return response
    response = HttpResponse()
    return FileResponse(open(image_full_path, 'rb'), content_type='image/jpeg')

    # except OSError as e:
    #     print(f"Error loading font: {e}")
    #     # Fallback to default font if custom font fails
    #     font = ImageFont.load_default()
    #     return font_path

    # # Create an image using Pillow
    # width, height = 300, 100
    # image = Image.new('RGB', (width, height), color=(255, 255, 255))
    # draw = ImageDraw.Draw(image)
    # # font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts', 'arial.ttf')
    # font_path = static('fonts/ariblk.ttf')  
    # print("font path is",font_path)
    # #try:
        
    #     # Load the custom font
    # font = ImageFont.truetype(font_path, 40)  # Using a larger font size (e.g., 40)
    # #except IOError:
    # #    # If the font is not available, fall back to default
    #    # font = ImageFont.load_default()
    # # Use a simple font (you can customize this or use any font)
    # #try:
    # #font = ImageFont.truetype("arial.ttf", 40)  # Using a larger font size (e.g., 40)
    # #except IOError:
    #  #   font = ImageFont.load_default()  # Fallback to default font if custom font not available
    
    # bbox = draw.textbbox((0, 0), captcha_text, font=font)
    # text_width = bbox[2] - bbox[0]
    # text_height = bbox[3] - bbox[1]
    
    # # Position text centrally
    # text_position = ((width - text_width) // 2, (height - text_height) // 2)  # Center text

    # # Draw the CAPTCHA text on the image with larger letters
    # draw.text(text_position, captcha_text, font=font, fill=(0, 0, 0))

    # # Draw the CAPTCHA text on the image
    # # draw.text((50, 15), captcha_text, font=font, fill=(0, 0, 0))
    # # draw.text(text_position, captcha_text, font=font, fill=(0, 0, 0))


    # # Save CAPTCHA text in the cache with a short expiration time
    # cache.set('captcha', captcha_text, timeout=300)  # 5 minutes timeout

    # # Return the image as a response
    # response = HttpResponse(content_type="image/png")
    # image.save(response, "PNG")
    

    # response['Access-Control-Allow-Origin'] = '*'
    # response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    # response['Access-Control-Allow-Headers'] = 'Content-Type'
    # return response



# class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        recaptcha_response = request.data.get('recaptcha')

        # Verify the reCAPTCHA response
        recaptcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        recaptcha_verify_response = requests.post(recaptcha_verify_url, data=recaptcha_data)
        recaptcha_result = recaptcha_verify_response.json()

        if not recaptcha_result.get('success'):
            return Response({'detail': 'Invalid CAPTCHA'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)








from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test

from.models import Customer,CustomerType

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['user', 'data']

class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        data = request.data.get('data')
        
        test = Test.objects.create(user=user, data=data)
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'customer_id', 
            'customer_name', 
            'customer_fathers_name', 
            'customer_address', 
            'customer_contact_number', 
            'credit_amount', 
            'customerType', 
            'description',
            'user', 
            'created_by', 
            'updated_by', 
            'created_date', 
            'updated_date', 
            'created_IP', 
            'is_active'
        ]
from googletrans import Translator
class CustomerAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        customer_data = request.data.get('data', {})  # Access the nested 'data' key
        print("customer data is",customer_data)
        
        print("printing request = ", customer_data)
        
        try:
            # Ensure that customerType exists (foreign key reference)
            customer_type_id = customer_data['customerType']
            customer_type = CustomerType.objects.get(customer_type_id=customer_type_id)
        except KeyError:
            return Response({"error": "customerType is missing in the data"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomerType.DoesNotExist:
            return Response({"error": "Invalid customer_type_id"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the customer object
        translator = Translator()
        customer_name_in_hindi = translator.translate(customer_data['customer_name'], src='en', dest='hi').text
        customer_fathers_name_hindi =translator.translate(customer_data['customer_fathers_name'], src='en', dest='hi').text
        print("customer name in hindi ",customer_name_in_hindi)
        customer = Customer.objects.create(
            customer_name=customer_data['customer_name'],
            customer_name_hindi = customer_name_in_hindi,
            customer_fathers_name_hindi = customer_fathers_name_hindi,
            customer_fathers_name=customer_data['customer_fathers_name'],
            customer_address=customer_data['customer_address'],
            customer_contact_number=customer_data['customer_contact_number'],
            credit_amount=customer_data['credit_amount'],
            customerType=customer_type,  # Set the customerType foreign key
            description=customer_data['description'],
            user=user,
            created_by=user,
            created_IP="ip_address",  # Placeholder for IP address, you can adjust it
        )

        # Save the customer
        customer.save()

        # Serialize the customer object and return the response
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerType
        fields = ['customer_type_id','customer_type_name']

class CustomerTypeAPIView(APIView):
    
    def get(self,request):
        customer_type_data  = CustomerType.objects.filter(is_active = True)

        serializer = CustomerTypeSerializer(customer_type_data, many=True)  # Serialize the data
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class CustomerGetSerializer(serializers.ModelSerializer):
    class Meta :
        model = Customer
        fields = ['customer_name','customer_fathers_name','customer_contact_number','customer_name_hindi','customer_fathers_name_hindi','credit_amount']

class CustomerGetAPIView(APIView):
    def get(self,request):
        customer_data = Customer.objects.filter(is_active = True)
        serializer  = CustomerGetSerializer(customer_data,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)