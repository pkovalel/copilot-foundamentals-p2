from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User(name='Clark Kent', email='clark@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=45, distance=20)
        Activity.objects.create(user=users[2], type='swim', duration=60, distance=2)
        Activity.objects.create(user=users[3], type='run', duration=25, distance=4)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(user=users[0], name='Ironman Prep', description='Intense workout')
        Workout.objects.create(user=users[2], name='Bat Training', description='Night workout')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[2], points=90)


        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email...'))
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db['octofit_tracker_user'].create_index('email', unique=True)
        client.close()

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
