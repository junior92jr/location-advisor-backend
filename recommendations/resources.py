import requests

from django.conf import settings

from .decorators import store_in_cache
from .constants import SEARCH_PLACES_ENDPOINT_URL
from .exceptions import FourSquareResourceUnavailable


class FourSquareResource:
    """
    FourSquare Resource class with functions to get data from external api.
    """
    
    @staticmethod
    @store_in_cache
    def search_places_by_location(query_params):
        """
        Get Places from External API.
        """

        headers = {
            "Accept": "application/json",
            "Authorization": settings.FOURSQUARE_API_KEY}

        payload = {
            'll': '{lat},{lng}'.format(
                lat=query_params['lat'], lng=query_params['lng'])}

        response = requests.get(
            SEARCH_PLACES_ENDPOINT_URL, headers=headers, params=payload)

        if response.status_code != 200:
            raise FourSquareResourceUnavailable()
        
        return response.json()['results']


    @staticmethod
    def filter_by_category(resource_response, category):
        """
        Filter in memory by category.
        """
        
        filtered_response = []

        for place in resource_response:
            for category_item in place.get('categories'):
                if category_item.get('id') == category:
                    filtered_response.append(place)

        return filtered_response

    @staticmethod
    def get_categories(resource_response):
        """
        Get Not Repeated Categories from Original Response.
        """

        all_categories = []

        for place in resource_response:
            for catefory in place.get('categories'):
                all_categories.append(catefory)
        
        all_categories = [
            item for counter, item in enumerate(
                all_categories) if item not in all_categories[counter + 1:]]

        return all_categories
