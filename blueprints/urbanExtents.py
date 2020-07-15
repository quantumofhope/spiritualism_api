# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask import current_app
import pandas as pd
# import json

urbanExtents_blueprint = Blueprint(name='urbanExtents', import_name=__name__, url_prefix='/urbanExtents/')

chur = pd.read_json("./static/data/churches.json")
spir= pd.read_csv("./static/data/spiritual.csv")

@urbanExtents_blueprint.route('add/<message>', methods=['GET'])
@urbanExtents_blueprint.route('add/', defaults={'message': 'sem mensagem no add'},methods=['GET'])
@urbanExtents_blueprint.route('/', defaults={'message': 'sem mensagem'}, methods=['GET'])
def add(message):
    return 'Urban Extents - {}'.format(message)

@urbanExtents_blueprint.route('church/', methods=['GET'])
def church():
    data = chur
    data.set_index(['church'], inplace=True)
    data.index.name=None
    return render_template('view.html',tables=[data.to_html()], titles = ['spirit surfers'])
    # return 'Urban Extents - {}'.format(chur)


@urbanExtents_blueprint.route('spirit/', methods=['GET'])
def spirit():
    data = spir
    data.set_index(['name'], inplace=True)
    data.index.name=True
    return render_template('view.html',tables=[data.to_html()], titles = ['spirit surfers'])
    # return 'Urban Extents - {}'.format(spir)

