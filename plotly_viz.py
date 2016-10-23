import plotly
import plotly.plotly as py
from plotly.tools import FigureFactory as FF


import numpy as np
import pandas as pd
print(plotly.__version__)
dataframe = pd.DataFrame(np.random.randn(100, 3),
                         columns=['A', 'B', 'C'])

fig = FF.create_scatterplotmatrix(dataframe, diag='histogram', index='A',
                                  colormap=['rgb(200, 150, 90)', '#3012CF', 'rgb(20, 124, 246)'],
                                  colormap_type='seq', height=700, width=700)
py.plot(fig, filename = 'Customized Colormap')