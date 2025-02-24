class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ['id', 'feature']  # Adjust these fields based on your KeyFeature model's actual fields

class TelexIntegrationSerializer(serializers.ModelSerializer):
    key_features = KeyFeatureSerializer(many=True, read_only=True)
    
    class Meta:
        model = TelexIntegration
        fields = ['id', 'key_features']  # Include all your required fields 