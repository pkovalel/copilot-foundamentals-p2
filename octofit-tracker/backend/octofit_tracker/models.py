from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()   # in km
    def __str__(self):
        return f"{self.type} by {self.user.name}"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user.name}: {self.points}"
