from django.urls import path,include
from test__ import views
urlpatterns = [
    
    path("api/",views.LoginAPIView.as_view(),name='login'),
    path('test/', views.TestAPIView.as_view(), name='test'),
    path('captcha/', views.generate_captcha, name='generate_captcha'),
    path("customer/", views.CustomerAPIView.as_view(),name='customer'),
    path("customer-get/",views.CustomerTypeAPIView.as_view(),name='customer-get'),
    path('customer-get-get/',views.CustomerGetAPIView.as_view(),name='customer-get'),
    path("page",views.Page,name='page')
]
