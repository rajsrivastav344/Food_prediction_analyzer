"""
URL Configuration for Food Nutrition Analyzer
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from views import (
    HomeView, SignupView, LoginView, LogoutView,
    FoodAnalyzeView, HealthReportView, HealthConditionsView,
    FoodsListView, home_view, about_view, services_view,
    generator_view, dashboard_view, contact_view, policy_view,
    submit_contact
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API Endpoints
    path('api/home/', HomeView.as_view(), name='home-api'),
    path('api/signup/', SignupView.as_view(), name='signup-api'),
    path('api/login/', LoginView.as_view(), name='login-api'),
    path('api/logout/', LogoutView.as_view(), name='logout-api'),
    path('api/analyze/', FoodAnalyzeView.as_view(), name='analyze-api'),
    path('api/report/', HealthReportView.as_view(), name='report-api'),
    path('api/health-conditions/', HealthConditionsView.as_view(), name='health-conditions-api'),
    path('api/foods/', FoodsListView.as_view(), name='foods-api'),
    path('api/contact/', submit_contact, name='contact-api'),
    
    # Template Views
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('generator/', generator_view, name='generator'),
    path('login/', lambda r: home_view(r), name='login'),
    path('signup/', lambda r: home_view(r), name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('contact/', contact_view, name='contact'),
    path('policy/', policy_view, name='policy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
