from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Organization
from .serializers import OrganizationSerializer

@api_view(['GET'])
def organization_list(request):
    organizations = Organization.objects.all()  # Query all organizations
    serializer = OrganizationSerializer(organizations, many=True)  # Serialize the data
    return Response(serializer.data)  # Return the data as JSON
