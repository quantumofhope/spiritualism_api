# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import current_app

import folium


mapper_blueprint = Blueprint(name='mapper', import_name=__name__, url_prefix='/mapper/')


@mapper_blueprint.route('mapper/<message>', methods=['GET'])
def mapper():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()