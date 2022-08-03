from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import RecomendatiosQuerySerializer
from .client import ClientFourSquare
from .utils import build_top_ten_parameters


class RecomendationViewSet(viewsets.ViewSet):
    """
    ViewSet that handle the connection the Foursquare API
    """

    serializer_class = RecomendatiosQuerySerializer
    permission_classes = (AllowAny,)
    queryset = None

    def list(self, request):
        """
        Generate the connection to the external API

        :param request: request comming from the session

        :return: Void function that generate a session
        """

        serializer = self.serializer_class(data=request.query_params)
        
        serializer.is_valid(raise_exception=True)

        client = ClientFourSquare()
        client.get_client()

        return Response({"results": client.get_top_ten(serializer.data)})
