# -*- coding: utf-8 -*-

from .constants import (
    TOP_TEN,
    LATITUDE,
    LONGITUDE,
    CORDINATES,
    CATEGORY_PARAM,
    LIMIT_PARAM,
    SECTION_PARAM,
    DEFAULT_VALUE,
    PARAM_STRUCTURE
)


def build_top_ten_parameters(serialized_parameters):
    """
    Generate the connection to the external API

    :param request: request comming from the session

    :return: Void function that generate a session
    """

    lat = serialized_parameters.get(LATITUDE, DEFAULT_VALUE)
    lng = serialized_parameters.get(LONGITUDE, DEFAULT_VALUE)
    category = serialized_parameters.get(CATEGORY_PARAM, DEFAULT_VALUE)

    params = {CORDINATES: PARAM_STRUCTURE % (lat, lng), LIMIT_PARAM: TOP_TEN}


    if category:
        params.update({SECTION_PARAM: category})

    return params
