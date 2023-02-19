from rest_framework import routers, urlpatterns

from user.views import CustomerViewSet

router = routers.DefaultRouter()
router.register('', CustomerViewSet, 'customer')

urlpatterns = router.urls