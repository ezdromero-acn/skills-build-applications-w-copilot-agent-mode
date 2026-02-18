from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = router.urls
