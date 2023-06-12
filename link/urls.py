from rest_framework.routers import DefaultRouter
from .views import LinkView

router = DefaultRouter()
router.register("links", LinkView)

urlpatterns = router.urls

aslkfslkd alksdfj