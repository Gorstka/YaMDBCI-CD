from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, Signup, TitleViewSet, Token, UserViewSet)

router = routers.DefaultRouter()
router.register("titles", TitleViewSet)
router.register("users", UserViewSet, basename="users")
router.register("categories", CategoryViewSet)
router.register("genres", GenreViewSet)
router.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews"
)
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/signup/", Signup.as_view(), name="signup"),
    path("v1/auth/token/", Token.as_view(), name="token"),
    path("v1/auth/", include("djoser.urls")),
    path("v1/auth/", include("djoser.urls.jwt")),
]
