"""
Django Views for Food Nutrition Analyzer (Complete Version)
"""

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

import os
import uuid
import json
from PIL import Image

from nutrition_model import nutrition_analyzer


# ============================
# 🏠 BASIC API
# ============================

class HomeView(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to Food Nutrition Analyzer',
            'status': 'success'
        })



class HealthConditionsView(APIView):
    def get(self, request):
        conditions = nutrition_analyzer.health_predictor.health_profiles

        data = [
            {
                "hindi": key,
                "english": value["name_en"]
            }
            for key, value in conditions.items()
        ]

        return Response({
            "status": "success",
            "conditions": data
        })
# ============================
# 🔐 AUTH SYSTEM
# ============================

class SignupView(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            data = json.loads(request.body)

            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not password:
                return Response({'error': 'Missing fields'}, status=400)

            if User.objects.filter(username=username).exists():
                return Response({'error': 'User exists'}, status=400)

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return Response({'message': 'Signup successful'})

        except Exception as e:
            return Response({'error': str(e)}, status=400)


class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            data = json.loads(request.body)

            user = authenticate(
                username=data.get('username'),
                password=data.get('password')
            )

            if user:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'error': 'Invalid credentials'}, status=401)

        except Exception as e:
            return Response({'error': str(e)}, status=400)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': 'Logged out'})


# ============================
# 🧠 FOOD ANALYSIS (ML)
# ============================

class FoodAnalyzeView(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            if 'image' not in request.FILES:
                return Response({'error': 'Upload image'}, status=400)

            image_file = request.FILES['image']

            # ✅ Validate image
            try:
                img = Image.open(image_file)
                img.verify()
            except:
                return Response({'error': 'Invalid image'}, status=400)

            # ✅ Save file
            if not os.path.exists('uploads'):
                os.makedirs('uploads')

            filename = f"{uuid.uuid4().hex}.jpg"
            path = os.path.join('uploads', filename)

            with open(path, 'wb+') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

            # ✅ ML Prediction
            foods = nutrition_analyzer.predict_food(path)

            # ✅ Nutrition calculation
            portions = float(request.data.get('portions', 1.0))
            result = nutrition_analyzer.analyze_nutrition(foods, portions)

            # ✅ Cleanup
            os.remove(path)

            return Response({
                'status': 'success',
                'foods_detected': foods,
                'nutrition_data': result
            })

        except Exception as e:
            return Response({'error': str(e)}, status=400)


# ============================
# ❤️ HEALTH REPORT
# ============================

class HealthReportView(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            data = json.loads(request.body)

            foods = data.get('foods', [])
            conditions = data.get('health_conditions', [])

            nutrition = nutrition_analyzer.analyze_nutrition(foods)

            report = nutrition_analyzer.generate_health_report(
                nutrition,
                conditions
            )

            return Response({
                'status': 'success',
                'report': report
            })

        except Exception as e:
            return Response({'error': str(e)}, status=400)


# ============================
# 📋 LIST APIs
# ============================

class FoodsListView(APIView):
    def get(self, request):
        foods = nutrition_analyzer.db.food_database

        return Response({
            'foods': [
                {
                    'hindi': k,
                    'english': v['name_en']
                } for k, v in foods.items()
            ]
        })


# ============================
# 🌐 TEMPLATE VIEWS
# ============================

def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def services_view(request):
    return render(request, 'services.html')


def generator_view(request):
    return render(request, 'generator.html')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


def contact_view(request):
    return render(request, 'contact.html')


def policy_view(request):
    return render(request, 'policy.html')


# ============================
# 📩 CONTACT FORM
# ============================

@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            # (You can save to DB or send email here)

            return JsonResponse({
                'status': 'success',
                'message': 'Message received!'
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })

    return JsonResponse({'error': 'Invalid request'})