# -*- coding: utf-8 -*-
from flask import Blueprint
# from flask import current_app
import pandas as pd
import folium


mapper_blueprint = Blueprint(name='mapper', import_name=__name__, url_prefix='/mapper/')

@mapper_blueprint.route('/<loc>', methods=['GET'])
def mapper(loc = ""):
    chur = pd.read_json("./static/data/churches.json")
    care = pd.read_json("./static/data/rec2.json")
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
    
    for row in chur.itertuples():
        uri = "https://www.snu.org.uk"+row.lnk[0]
        print(f"URI = {uri}")
        test = folium.Html(f'<b>{row.church}</b></br> <a href="{uri} "target="_blank"> SNU Link </a>', script=True)
        popup = folium.Popup(test)
        folium_map.add_child(folium.Marker(location=[row.lat,  row.lng],
                 popup=popup, icon=folium.Icon(color='green', icon='leaf')))
        
        
    for row in care.itertuples():
        test1 = folium.Html(f'<b>{row.locationName}</b></br><p>PostCode: {row.postalCode}  Constit: {row.parliamentary_constituency}</p>', script=True)
        popup = folium.Popup(test1)
        folium_map.add_child(folium.Marker(location=[row.lat,  row.lng],
                 popup=popup, icon=folium.Icon(color='green', icon='hand-holding-heart')))
    
    return folium_map._repr_html_()


@mapper_blueprint.route('/church', methods=['GET'])
def map_church():
    chur = pd.read_json("./static/data/churches.json")
    resp = chur.to_json(orient="split")
    return resp

    
@mapper_blueprint.route('/care', methods=['GET'])
def map_church():   
    care = pd.read_json("./static/data/rec2.json")
    resp = care.to_json(orient="split")
    return resp
    
