from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        activity = Activity.objects.create(user_id=str(user.id), type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        workout = Workout.objects.create(user_id=str(user.id), description='Chest day')
        self.assertEqual(workout.description, 'Chest day')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        leaderboard = Leaderboard.objects.create(user_id=str(user.id), points=100)
        self.assertEqual(leaderboard.points, 100)
