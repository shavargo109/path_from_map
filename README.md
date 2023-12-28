# path_from_map
This is a package that directly convert a colored path on a 2D map (image) into a nav_msgs/Path message. 
# Usage
You need a map.jpg and map.yaml to process
These two files can be easily obtained by your normal practice on saving the map from map server
As the original generated file is in .pgm format, simply convert it into .jpg format as a new file in order to add different colors into it
Inside the code, specify the file path, both .jpg and .yaml, and the first pixel as the starting point of the path

```
self.first_pixels_ = [160, 194]

# enter your file path
node = MapPathNode('your-path-to-map.jpg',
                    'your-path-to-map.jpg')
```
## Example:

![alt text](https://ibb.co/dtyx66P)

you can get the first pixel in any graphic editor

img1 img2
Path in the .jpg file and Path displayed in Rviz as nav_msgs/Path message

# Environment
- Ubuntu 20.04
- ROS Noetic


