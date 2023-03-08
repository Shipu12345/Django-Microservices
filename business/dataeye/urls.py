from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_nested import routers
from .views import StoreViewSet


app_name = "datastore"

router = routers.DefaultRouter()
router.register("data/stores", StoreViewSet)

urlpatterns = router.urls
