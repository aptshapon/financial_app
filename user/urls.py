from django.urls import include, path
from rest_framework import routers
from user.views import UserViewSet, WalletViewSet, ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallet', WalletViewSet)
router.register(r'expense', ExpenseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]