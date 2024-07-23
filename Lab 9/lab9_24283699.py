# Example requests for Google Maps API
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBI4lh5XLtQP-xP_lbhnmFVdAuOHgA67qg')

locations = []
geocode_results = []
total_distance = 0
latlon = []
total = 0

for i in range(0, 5):
    destination = input("Enter location: ")
    locations.append(destination)
    geocode_results.append(gmaps.geocode(destination))
    latlon.append(geocode_results[i][0]["geometry"]["location"])
print("Your trip route: ")

for i in range(0, 4):
    directions_result = gmaps.directions(locations[i],
                                         locations[i+1],
                                         mode="driving")
                                         
    print(locations[i], geocode_results[i][0]["geometry"]["location"])
    leg = directions_result[0]['legs'][0]['distance']['value'] / 1000
    total += leg
    print("\tDistance to stop:", leg, "km" , "Distance travelled so far:", total, "km")

print(locations[i+1], geocode_results[i+1][0]["geometry"]["location"])
print("Total distance: ", total, "km")
