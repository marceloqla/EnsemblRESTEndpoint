from .models import GeneAutocomplete
from rest_framework import serializers

#Serialization for exposition
class GeneAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneAutocomplete
        # fields = ['display_label', 'location', 'stable_id', 'species']
        fields = ['display_label']
