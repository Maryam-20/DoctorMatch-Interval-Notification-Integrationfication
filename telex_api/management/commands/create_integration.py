from django.core.management.base import BaseCommand
from telex_api.models import TelexIntegration, KeyFeature, IntegrationSetting

class Command(BaseCommand):
    help = 'Creates the Telex integration configuration'

    def handle(self, *args, **options):
        # First, delete any existing integrations
        TelexIntegration.objects.all().delete()

        # Create new integration
        integration = TelexIntegration.objects.create(
            app_name="One Health Hospital Management System",
            app_description="A comprehensive hospital management system that handles appointments, doctor assignments, and patient notifications",
            app_url="https://one-health-0oxk.onrender.com",
            app_logo="https://res.cloudinary.com/naijaceo/image/upload/v1595027227/3d_logo_maker_bonus_ssqd0g.png",
            background_color="#ffffff",
            integration_category="Task Automation",
            integration_type="interval",
            is_active=True,
            display_name=" DoctorMatch Monitor",
            website="https://one-health-0oxk.onrender.com/interval-integration.json",
            author="Maryam Anileleye",
            tick_url="https://one-health-0oxk.onrender.com/tick",
        )

        # Add key features
        features = [
            "Automated appointment scheduling and notifications",
            "Real-time doctor availability tracking",
            "Patient appointment reminders and updates",
            "Staff assignment and department management",
            "Integrated payment processing"
        ]
        
        for feature in features:
            KeyFeature.objects.create(integration=integration, feature=feature)

        # Add settings
        settings = [
            {
                "label": "Hospital-ID",
                "type": "text",
                "required": True,
                "default": "ONE-HEALTH-001"
            },
            {
                "label": "Department",
                "type": "text",
                "required": True,
                "default": "ALL"
            },
            {
                "label": "Notification-Interval",
                "type": "text",
                "required": True,
                "default": "*/5 * * * *"
            },
            {
                "label": "Alert-Threshold",
                "type": "number",
                "required": True,
                "default": "80"
            }
        ]

        for setting in settings:
            IntegrationSetting.objects.create(integration=integration, **setting)
        
        self.stdout.write(self.style.SUCCESS('Successfully created Telex integration configuration')) 