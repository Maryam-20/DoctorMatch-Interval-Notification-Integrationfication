from rest_framework import serializers
from .models import TelexIntegration, KeyFeature, IntegrationSetting

class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ['id','feature']

class IntegrationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationSetting
        fields = ['label', 'type', 'required', 'default']

class TelexIntegrationSerializer(serializers.ModelSerializer):
    key_features = KeyFeatureSerializer(many=True, read_only=True)
    settings = IntegrationSettingSerializer(many=True, read_only=True)
    permissions = serializers.SerializerMethodField()
    descriptions = serializers.SerializerMethodField()

    class Meta:
        model = TelexIntegration
        fields = '__all__'

    def get_permissions(self, obj):
        return {
            'monitoring_user': {
                'always_online': obj.always_online,
                'display_name': obj.display_name
            }
        }

    def get_descriptions(self, obj):
        return {
            'app_name': obj.app_name,
            'app_description': obj.app_description,
            'app_url': obj.app_url,
            'app_logo': obj.app_logo,
            'background_color': obj.background_color
        }