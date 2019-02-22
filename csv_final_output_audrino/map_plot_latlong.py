import gmplot 
  
latitude_list = [30.3358376, 30.307977] 
  
longitude_list = [77.8701919, 78.048457] 
  
gmap4 = gmplot.GoogleMapPlotter.from_geocode("Dehradun, India") 
  
# heatmap plot heating Type 
# points on the Google map 
gmap4.heatmap( latitude_list, longitude_list ) 
  
gmap4.draw( "heatmap.html") 
