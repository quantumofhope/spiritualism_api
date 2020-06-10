# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import current_app

import folium

mapper_blueprint = Blueprint(name='mapper', import_name=__name__, url_prefix='/mapper/')

@mapper_blueprint.route('/<loc>', methods=['GET'])
def mapper(loc = ""):
    if loc == "":
        locref = (50.804055, -1.980081)
    if loc == "Loc1":
        locref = (50.804055, -1.980081)
    if loc == "Loc2":
        locref = (50.7192, -1.8808)
    if loc == "Loc3":
        locref = (50.7112, -2.4412)
            
    start_coords = (float(locref[0]), float(locref[1]))
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()