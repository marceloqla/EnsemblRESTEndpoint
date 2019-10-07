from django.db import connection
from django.shortcuts import render
from .models import GeneAutocomplete
from .serializers import GeneAutocompleteSerializer

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

#
class SuggestionList(views.APIView):
    """
    API endpoint view
    """
    renderer_classes = [XMLRenderer,JSONRenderer]
    
    def get(self, request):
        query = self.request.query_params.get('query', None)
        queryspecies = self.request.query_params.get('species', None)
        querylimit = self.request.query_params.get('limit', None)
        queryformat = self.request.query_params.get('format', None)
        if not query:
            raise 
        query = query.upper()
        results = GeneAutocomplete.objects.filter(display_label__startswith=query)
        if queryspecies:
            results = results.filter(species=queryspecies)

        #flatten results to display_label list and remove duplicates (fast)
        resultslist = results.values_list('display_label', flat=True).distinct()

        #remove object duplicates before limiting size of array (slow)
        # for dlabel in results.values_list('display_label', flat=True).distinct():
        #     labelresults = results.filter(display_label=dlabel)[1:]
        #     labelresultsids = labelresults.values_list('stable_id', flat=True)
        #     labelresultsids = list(labelresultsids)
        #     results = results.exclude(stable_id__in=labelresultsids)
        
        if querylimit:
            #results = results[:int(querylimit)]
            resultslist = sorted(list(resultslist))[:int(querylimit)]

        # Serialize and return objects:
        # resultsdata = GeneAutocompleteSerializer(results, many=True).data 
        # return Response(resultsdata)

        #Return list of suggestions with serialization
        return Response(list(resultslist))
