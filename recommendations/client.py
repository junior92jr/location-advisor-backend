# -*- coding: utf-8 -*-
import foursquare

from django.conf import settings

from .utils import build_top_ten_parameters
from .constants import (
    FOURSQUARE_GROUP,
    FOURSQUARE_RESULT_INDEX,
    FOURSQUARE_ITEMS,
    FOURSQUARE_VENUES
)


class ClientFourSquare():

    """
    FourSquare Connection Handler. Here we are creating
    the basic methods **get_client** and **get_top_ten** that are
    creating our conection to the Vendor API.
    """

    client_id = settings.FOURSQUARE_CLIENT_ID
    client_secret = settings.FOURSQUARE_CLIENT_SECRET
    client = None

    def get_client(self):
        """
        Generate the connection to the external API

        :return: Void function that generate a session
        """

        self.client = foursquare.Foursquare(client_id=self.client_id,
                                            client_secret=self.client_secret)

    def get_top_ten(self, query_params):
        """
        Get the top ten recomended places according the params specifications

        :param query_params: dictionary of parameters

        :return: return a list of top ten recomended places
        """

        top_ten = list()

        response = self.client.venues.explore(
            params=build_top_ten_parameters(query_params))

        list_items = self.accessing_to_items(response)

        for item in list_items:
            top_ten.append(self.parsing_results(item))

        return top_ten

    def accessing_to_items(self, response):
        """
        Access to the information part in the request

        :param response: response comming from the external API

        :return: Return the list of items in the response
        """

        try:
            relevant_response = response[FOURSQUARE_GROUP][
                                         FOURSQUARE_RESULT_INDEX][
                                         FOURSQUARE_ITEMS]
        except KeyError as e:
            relevant_response = list()

        return relevant_response

    def parsing_results(self, item):
        """
        Parse the results in order to show the relevant information

        :param item: item response coming from the API

        :return: Returns Parsed response from the information
        """

        try:
            item_response = item[FOURSQUARE_VENUES]

        except KeyError as e:
            item_response = dict()

        return item_response
