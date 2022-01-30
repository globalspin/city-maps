import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

# Create the matplotlib figure (fig) and axes (ax)
# Overall map size (figsize) is specified in inches.
# constrained_layout tells matplotlib to place subelements to fit.
fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

backup = plot(
    # Address:
    'Fownes Street Lower, Temple Bar, Royal Exchange A ED, Dublin, Dublin 2, Leinster, D02 NH04, Ireland',
    # Plot geometries in a circle of radius (measured in meters):
    radius = 500,
    # Matplotlib axis
    ax = ax,
    # Which OpenStreetMap layers to plot and their parameters:
    layers = {
            # Perimeter (in this case, a circle)
            'perimeter': {},
            # Streets and their widths
            'streets': {
                'width': {
                    'motorway': 0,
                    'trunk': 0,
                    'primary': 0,
                    'secondary': 0,
                    'tertiary': 0,
                    'residential': 0,
                    'service': 0,
                    'unclassified': 0,
                    'pedestrian': 2,
                    'footway': 1,
                    'living_street': 2,
                    'bridleway': 2,
                    'steps': 1,
                    'sidewalk': 1,
                    'path': 1,
                }
            },
            # Other layers:
            #   Specify a name (for example, 'building') and which OpenStreetMap tags to fetch
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
        },
        # drawing_kwargs:
        #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
        drawing_kwargs = {
            'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': '---...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
            'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#bc9b58', 'ec': '#ffffff', 'alpha': 1, 'lw': 0, 'linestyle': 'dotted', 'zorder': 3},
            'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
        }
)

plt.savefig('../prints/dublin-temple-bar.png')
plt.savefig('../prints/dublin-temple-bar.svg')
