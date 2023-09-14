from rest_framework.routers import DefaultRouter

from blogs import views

router=DefaultRouter()
router.register("Category", views.CategoryModelViewSet, "category")
router.register("User", views.UserModelViewSet, "user")
router.register("Post", views.PostModelViewSet, "post")
router.register("Comment", views.CommentModelViewSet, "comment")