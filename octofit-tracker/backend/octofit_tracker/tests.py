from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=team)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team B")
        user = User.objects.create_user(username="user2", email="user2@example.com", password="testpass", team=team)
        activity = Activity.objects.create(user=user, type="run", duration=30, distance=5.0)
        self.assertEqual(activity.type, "run")
        self.assertEqual(activity.user.username, "user2")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Cardio Blast", description="A great cardio workout", suggested_for="all")
        self.assertEqual(workout.name, "Cardio Blast")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        team = Team.objects.create(name="Team C")
        user = User.objects.create_user(username="user3", email="user3@example.com", password="testpass", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
        self.assertEqual(leaderboard.user.username, "user3")
