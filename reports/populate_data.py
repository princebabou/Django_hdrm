from django.utils import timezone
from reports.models import Agent, Software, SystemSnapshot, SnapshotSoftware
from datetime import timedelta
import random
import sys

def populate_data():

    # Create Agents
    agent1, _ = Agent.objects.get_or_create(name='Agent_A')
    agent2, _ = Agent.objects.get_or_create(name='Agent_B')

    # Sample software
    software_list = ['Antivirus_X', 'Browser_Y', 'Office_Z', 'Firewall_W', 'VPN_V']
    softwares = {name: Software.objects.get_or_create(name=name)[0] for name in software_list}

    start_date = timezone.now() - timedelta(days=10)
    for day in range(10):
        for agent in [agent1, agent2]:
            snapshot = SystemSnapshot.objects.create(agent=agent, timestamp=start_date + timedelta(days=day))
            installed = random.sample(list(softwares.values()), random.randint(2, 4))
            for sw in installed:
                SnapshotSoftware.objects.create(snapshot=snapshot, software=sw)

    sys.stdout.write("Data populated successfully.\n")

if __name__ == '__main__':
    populate_data()
    