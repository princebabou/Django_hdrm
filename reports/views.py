from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Min, Max
from .models import Agent, SnapshotSoftware

class AgentReportView(APIView):
    def get(self, request, id):
        try:
            agent = Agent.objects.get(id=id)
        except Agent.DoesNotExist:
            return Response({"error": "Agent not found"}, status=status.HTTP_404_NOT_FOUND)

        # Complex query: Group by software, get min/max timestamp for the agent's snapshots
        report = SnapshotSoftware.objects.filter(snapshot__agent=agent).values('software__name').annotate(
            first_seen=Min('snapshot__timestamp'),
            last_seen=Max('snapshot__timestamp')
        ).order_by('software__name')

        # Format the response
        summary = [
            {
                "software": item['software__name'],
                "first_seen": item['first_seen'],
                "last_seen": item['last_seen']
            } for item in report
        ]

        return Response({"agent": agent.name, "software_summary": summary})
    