import requests

from django.conf import settings

from .decorators import store_response_in_cache
from .constants import SEARCH_PLACES_ENDPOINT_URL
from .exceptions import FourSquareResourceUnavailable
from .mixins import FourSquareUtilsMixin


class FourSquareResource(FourSquareUtilsMixin):
    """
    FourSquare Resource class with functions to get data from external api.
    """

    @classmethod
    @store_response_in_cache
    def four_square_request(cls, query_params):
        """
        Connection with Four square api service.
        
        :param query_params: Dictionary with parameters from original request.

        :return: Response object from requests library.
        """

        headers = {
            "Accept": "application/json",
            "Authorization": settings.FOURSQUARE_API_KEY}
        
        payload = {
            'll': '{lat},{lng}'.format(
                lat=query_params['lat'], lng=query_params['lng'])}

        response = requests.get(
            SEARCH_PLACES_ENDPOINT_URL, headers=headers, params=payload)
        
        return response
    
    @classmethod
    def search_places_by_location(cls, query_params):
        """
        Get Places from External API.
        
        :param query_params: Dictionary with parameters from original request.

        :return: List of items accessed from original request.
        """

        response = cls.four_square_request(query_params)

        if response.status_code != 200:
            raise FourSquareResourceUnavailable()

        return response.json()['results']
