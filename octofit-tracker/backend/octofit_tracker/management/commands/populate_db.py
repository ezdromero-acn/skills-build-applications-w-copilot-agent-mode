from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users (superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', team=dc),
        ]

        # Create Activities
        activities = [
            octo_models.Activity.objects.create(user=users[0], type='Run', duration=30, distance=5),
            octo_models.Activity.objects.create(user=users[1], type='Swim', duration=45, distance=2),
            octo_models.Activity.objects.create(user=users[2], type='Bike', duration=60, distance=20),
            octo_models.Activity.objects.create(user=users[3], type='Run', duration=25, distance=4),
            octo_models.Activity.objects.create(user=users[4], type='Swim', duration=50, distance=3),
            octo_models.Activity.objects.create(user=users[5], type='Bike', duration=70, distance=25),
        ]

        # Create Workouts
        workouts = [
            octo_models.Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel'),
            octo_models.Workout.objects.create(name='Justice Strength', description='Strength for justice', suggested_for='DC'),
        ]

        # Create Leaderboard
        for user in users:
            octo_models.Leaderboard.objects.create(user=user, points=100)


        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
