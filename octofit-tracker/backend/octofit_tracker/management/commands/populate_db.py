from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete dependent objects first to avoid orphaned references
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.filter(pk__isnull=False).delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(email='ironman@marvel.com', username='ironman', team_id=str(marvel.id))
        captain = User.objects.create_user(email='captain@marvel.com', username='captain', team_id=str(marvel.id))
        batman = User.objects.create_user(email='batman@dc.com', username='batman', team_id=str(dc.id))
        superman = User.objects.create_user(email='superman@dc.com', username='superman', team_id=str(dc.id))

        # Create activities
        Activity.objects.create(user_id=ironman.id, type='Running', duration=30)
        Activity.objects.create(user_id=batman.id, type='Cycling', duration=45)

        # Create workouts
        Workout.objects.create(user_id=ironman.id, description='Chest day')
        Workout.objects.create(user_id=batman.id, description='Leg day')

        # Create leaderboard
        Leaderboard.objects.create(user_id=ironman.id, points=100)
        Leaderboard.objects.create(user_id=batman.id, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
