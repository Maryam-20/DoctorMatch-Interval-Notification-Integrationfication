from django.core.management.base import BaseCommand
from telex_api.models import TelexIntegration, KeyFeature, IntegrationSetting

class Command(BaseCommand):
    help = 'Creates the Telex integration configuration'

    def handle(self, *args, **options):
        integration = TelexIntegration.objects.create(
            app_name="Hospital Appointment System",
            app_description="Manages hospital appointments and sends notifications",
            app_url="https://one-health-0oxk.onrender.com",
            app_logo="your-logo-url",
            background_color="#ffffff",
            integration_category="Healthcare",
            integration_type="interval",
            is_active=True,
            display_name="Hospital Monitor",
            website="https://your-app-url.onrender.com/interval-integration.json",
            author="Your Name",
            tick_url="https://your-app-url.onrender.com/tick",
        )

        features = [
            "Automated appointment notifications",
            "Real-time doctor availability updates",
            "Patient appointment reminders",
            "Staff assignment notifications"
        ]
        
        for feature in features:
            KeyFeature.objects.create(integration=integration, feature=feature)

        settings = [
            {"label": "Hospital-ID", "type": "text", "required": True, "default": ""},
            {"label": "Department", "type": "text", "required": True, "default": ""},
            {"label": "Notification-Interval", "type": "text", "required": True, "default": "*/5 * * * *"},
        ]

        for setting in settings:
            IntegrationSetting.objects.create(integration=integration, **setting)