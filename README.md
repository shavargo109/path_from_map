# path_from_map
This is a package that directly convert a red-colored path on a 2D map (image) into a nav_msgs/Path message. 
## Usage
As now it only contains a python script, simply add it in any package to compile

You need a map.png and map.yaml to process

These two files can be easily obtained by your normal practice on saving the map from map server

As the original generated file is in .pgm format, simply convert it into .png format as a new file in order to add different colors into it

Inside the code, specify the file path, both .png and .yaml, and the first pixel as the starting point of the path

```
# edit your first pixel here
self.first_pixels_ = [160, 194]
```

```
# enter your file path
node = MapPathNode('your-path-to-map.png',
                    'your-path-to-map.yaml')
```
## Example:
![alt text](https://github.com/shavargo109/path_from_map/blob/main/doc/first_pixel.png)

you can get the first pixel in any graphic editor

![alt text](https://github.com/shavargo109/path_from_map/blob/main/doc/image.png)

Path indicated in the .png file 

![alt text](https://github.com/shavargo109/path_from_map/blob/main/doc/Rviz.png)

Path displayed in Rviz as nav_msgs/Path message

## Environment
- Ubuntu 20.04
- ROS Noetic

## Future work
Add the first pixels and file path as parameters in ros

Provide simple demo as example

Make it a standalone package with MBF
