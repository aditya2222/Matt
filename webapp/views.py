from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.http import HttpResponse
# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from .fusioncharts import FusionCharts
from .models import *

# Create your views here.


class HomeView(TemplateView):
    template_name = 'webapp/charts.html'

  # The `chart` function is defined to load chart from a SQLite database. At first, data is retrived
  # from the SQLite database. This data is used to create chart data.


def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    # setting chart cosmetics
    dataSource['chart'] = {
        "caption": "SpreadSheet Data Analysis",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "showXAxisLine": "1",
        "xAxisLineColor": "#999999",
        "showValues": "0",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateHGridColor": "0",
        "showlabels":"1",
    }

    dataSource['data'] = []
    # The data for the chart should be in an array wherein each element of the array is a JSON object as
    # `label` and `value` keys.
    # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
    for key in SpreadSheet1.objects.all():
        data = {}
        data['label'] = key.clr
        data['value'] = key.percentage_of_available_funds
        dataSource['data'].append(data)

        # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1", "100%",
                            "400", "chart-1", "json", dataSource)
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'webapp/fusioncharts-html-template.html', {'output': column2D.render()})
