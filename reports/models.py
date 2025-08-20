from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Software(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class SystemSnapshot(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='snapshots')
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.agent.name} - {self.timestamp}"

class SnapshotSoftware(models.Model):
    snapshot = models.ForeignKey(SystemSnapshot, on_delete=models.CASCADE, related_name='softwares')
    software = models.ForeignKey(Software, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('snapshot', 'software')