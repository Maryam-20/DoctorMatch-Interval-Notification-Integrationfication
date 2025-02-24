from django.db import models

# Create your models here.
from django.db import models

class TelexIntegration(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    # Descriptions
    app_name = models.CharField(max_length=255)
    app_description = models.TextField()
    app_url = models.URLField()
    app_logo = models.URLField()
    background_color = models.CharField(max_length=7)
    integration_category = models.CharField(max_length=100)
    integration_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    # Permissions
    always_online = models.BooleanField(default=True)
    display_name = models.CharField(max_length=100)
    website = models.URLField()
    author = models.CharField(max_length=100)
    
    # URLs
    tick_url = models.URLField()
    target_url = models.URLField(blank=True)

class KeyFeature(models.Model):
    integration = models.ForeignKey(TelexIntegration, on_delete=models.CASCADE, related_name='key_features')
    feature = models.CharField(max_length=255)

class IntegrationSetting(models.Model):
    integration = models.ForeignKey(TelexIntegration, on_delete=models.CASCADE, related_name='settings')
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    required = models.BooleanField(default=True)
    default = models.CharField(max_length=255, blank=True)