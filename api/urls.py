from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MakeupViewSet, SignupView, LoginView, LogoutView  # Change FurnitureViewSet to MakeupViewSet
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'makeup', MakeupViewSet)  # Change 'furniture' to 'makeup'

# The API URLs
urlpatterns = [
    path('', include(router.urls)),  # Makeup URLs
    path('signup/', SignupView.as_view(), name='signup'),  # Signup URL
    path('login/', LoginView.as_view(), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
