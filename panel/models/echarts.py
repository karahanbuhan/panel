"""
Defines custom ECharts bokeh model to render Vega json plots.
"""
from bokeh.core.properties import Any, Dict, Enum, String
from bokeh.models import LayoutDOM

from ..util import classproperty, bundled_files


class ECharts(LayoutDOM):
    """
    A Bokeh model that wraps around an ECharts plot and renders it
    inside a Bokeh.
    """

    __javascript_raw__ = [
        "https://cdn.jsdelivr.net/npm/echarts@4.8.0/dist/echarts.min.js",
        "https://cdn.jsdelivr.net/npm/echarts-gl@1.1.1/dist/echarts-gl.min.js"
    ]

    @classproperty
    def __javascript__(cls):
        return bundled_files(cls)

    @classproperty
    def __js_skip__(cls):
        return {
            'echarts': cls.__javascript__[:1]
        }

    __js_require__ = {
        'baseUrl': 'https://cdn.jsdelivr.net/npm/',
        'paths': {
            "echarts":  "echarts@4.8.0/dist/echarts.min",
            "echarts-gl": "echarts-gl@1.1.1/dist/echarts-gl.min.js"
        },
        'exports': {}
    }

    data = Dict(String, Any)

    renderer = Enum("canvas", "svg")

    theme = Enum("default", "light", "dark")
