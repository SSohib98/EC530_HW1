import math

R = 6371.0 # Earths radius in kilometers

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula to calculate distance
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

def find_closest_points(array1, array2):
    closest_points = []
    
    for point1 in array1:
        min_distance = float('inf')
        closest_point = None
        
        for point2 in array2:
            dist = haversine(point1[0], point1[1], point2[0], point2[1])
            
            if dist < min_distance:
                min_distance = dist
                closest_point = point2
                
        closest_points.append((point1, closest_point))
    
    return closest_points

# Trying an exmaple to see if this work
array1 = [(40.748817, -73.985428), (34.052235, -118.243683)]  
array2 = [(51.507351, -0.127758), (48.856613, 2.352222), (40.730610, -73.935242)]  

matches = find_closest_points(array1, array2)
for point1, closest_point in matches:
    print(f"Point {point1} is closest to {closest_point}")
