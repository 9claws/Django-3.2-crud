from rest_framework.routers import DefaultRouter
from django.urls import path, include
from logistic.views import ProductViewSet, StockViewSet
from . import views

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)



urlpatterns = [
    path('api/v1', include(router.urls)),
    path("", views.index, name="index"),
]