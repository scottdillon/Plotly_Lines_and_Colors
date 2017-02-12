import random
import plotly
import plotly.graph_objs as go
import plotly_config.plotly_lines_colors as plc
from plotly_config.plotly_lines_colors import Colors, MarkerTips
import plotly_config.symbols as symbols

sf = plc.ScatterFactory()

trace0 = sf.scatter()
trace1 = sf.scatter(lw=0, color=Colors.RED, symbol=symbols.circle, lineshape=plc.LineShape.SPLINE,
                 markersize=20, markerfacecolor=Colors.GREEN, mode=plc.Mode.MARKERS_ONLY, markeredgewidth=0)

trace1.x = list(range(100))
trace1.y = list(range(100))
trace1.marker.color = list(range(100))
trace1.marker.colorscale = 'Viridis'
trace1.marker.size = list([random.random() * 50.0 for x in range(100)])

data = go.Data([trace0, trace1])

plotly.offline.plot(figure_or_data=data, filename='output_files/basic-line.html',
                    include_plotlyjs=False, show_link=False)
