from django.urls import path
from .views import AgentReportView

urlpatterns = [
    path('agents/<int:id>/report/', AgentReportView.as_view(), name='agent-report'),
]
