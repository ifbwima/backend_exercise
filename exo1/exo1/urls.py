from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quickstart.views import AuthorViewSet, PublisherViewSet, CategoryViewSet, BookViewSet, BookCopyViewSet, LoanViewSet, CommentViewSet, RatingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet, basename='book')
router.register(r'book-copies', BookCopyViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="API for library management system",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@library.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]