# path_from_map
This is a small package that directly convert a colored path on a 2D map (image) into a nav_msgs/Path message. 
# Concept
You need a map.jpg and map.yaml to process
These two files can be easily obtained by your normal practice on saving the map from map server
As the original generated file is in .pgm format, simply convert it into .jpg format as a new file in order to add different colors into it
Inside the code, specify the file path, both .jpg and .yaml, and the first pixel as the starting point of the path
Example:

![alt text] (https://ibb.co/dtyx66P)

you can get the first pixel in any graphic editor
