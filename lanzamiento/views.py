from django.views.generic import  TemplateView
from django.shortcuts import render

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

import random

numero_intentos = 0
resultado = 0
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0
contador_6 = 0

def WelcomeView(request):
    """Create new post-view"""
    global numero_intentos
    global resultado
    global contador_1
    global contador_2
    global contador_3
    global contador_4
    global contador_5
    global contador_6
    
    if request.method == 'POST' and 'lanzar' in request.POST:

        resultado = random.randint(1,6)
        numero_intentos += 1 

        if resultado == 1:
            contador_1 += 1
        elif resultado == 2:
            contador_2 += 1
        elif resultado == 3:
            contador_3 += 1
        elif resultado == 4:
            contador_4 += 1
        elif resultado == 5:
            contador_5 += 1
        else:
            contador_6 += 1
    
    elif request.method == 'POST' and 'reiniciar' in request.POST:
        
        numero_intentos = 0
        resultado = 0
        contador_1 = 0
        contador_2 = 0
        contador_3 = 0
        contador_4 = 0
        contador_5 = 0
        contador_6 = 0

    number = ['1', '2', '3', '4', '5', '6']
    counts = [contador_1, contador_2, contador_3, contador_4, contador_5, contador_6]

    source = ColumnDataSource(data=dict(number=number, counts=counts, color=Spectral6))


    p = figure(x_range=number, y_range = (0,max(counts)), title="Lanzamientos",
            toolbar_location=None, tools="", sizing_mode="stretch_both")

    p.vbar(x='number', top='counts', width=0.9, color='gray', legend_field="number", source=source)

    p.title.text_font_size = '15pt'
    p.title.text_font = "Segoe UI"
    #p.background_fill_color = "gray"

    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_right"
    p.legend.label_text_font_size = "11pt"

    p.xaxis.axis_label_text_font_size = "20px"
    p.xaxis.major_label_text_font_size = "10pt"
    p.xaxis.axis_label = 'Número'

    p.yaxis.axis_label_text_font_size = "20px"
    p.yaxis.major_label_text_font_size = "10pt"
    p.yaxis.axis_label = '# Lanzamientos'

    
    
    script, div = components(p)
    
    return render(request, 'lanzamiento/index.html',
        {
            'resultado': resultado,
            'numero_intentos': numero_intentos,
            'script' : script,
            'div' : div,
        }
    )