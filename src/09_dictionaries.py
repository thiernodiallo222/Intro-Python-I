"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]
# print(waypoints)

# Add a new waypoint to the list
# YOUR CODE HERE
new_waypoint = {
    "lat": 44,
    "lon": -123,
    "name":"my newly added waypoint"
}
waypoints.append(new_waypoint)
# print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
updated={
        "lat": 43,
        "lon": -130,
        "name": "not a real place"
       }

waypoints[0]=updated

# print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
print('printing waypoints, below:')
for item in waypoints:
    print(item['lat'], item['lon'], item['name'])
