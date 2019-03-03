from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(11.322132, 75.933846, 13)
# Scatter points

top_attraction_lats, top_attraction_lons = zip(*[
    (11.322290, 75.933986),
    (11.322416, 75.934077),
    (11.322463, 75.934179),
    (11.322132, 75.933846),
    ])
gmap.heatmap(top_attraction_lats,top_attraction_lons,radius=15,dissipating=True)
# Draw
gmap.draw("my_map.html")
