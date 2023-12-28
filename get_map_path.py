#!/usr/bin/env python3
import rospy
import yaml
import numpy as np
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from PIL import Image
from scipy.spatial.distance import euclidean


class MapPathNode(object):
    def __init__(self, image_path: str, yaml_path: str):
        self.period_ = 10
        self.image_path_ = image_path
        self.yaml_path_ = yaml_path
        self.origin_x_ = float()
        self.origin_y_ = float()
        self.resolution_ = float()
        self.is_published_ = bool(False)
        self.first_pixels_ = [160, 194]  # in ros format
        # self.first_pixels_ = [503, 468]  # in ros format
        print('map to path node started')

        self.path_pub_ = rospy.Publisher('/map_path', Path, queue_size=10)

    def read_yaml_file(self, file_path):
        '''
        initialise the origin and resolution of map 
        '''
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            self.origin_x_ = data['origin'][0]
            self.origin_y_ = data['origin'][1]
            self.resolution_ = data['resolution']
        print(self.origin_x_, self.origin_y_, self.resolution_)

    def extract_red_pixels(self, image_path):
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size
        first_y = self.first_pixels_[1]
        self.first_pixels_[1] = height-first_y-1

        red_pixels = []

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                if r > 100 and g < 100 and b < 100:
                    # originally the lib read top left as (0,0), where ros read yaml bottom left as (0,0)
                    dy = height - y - 1
                    red_pixels.append((x, dy))

        # return list of (x,y)
        print("red pixels: " + str(len(red_pixels)))
        return red_pixels

    def find_shortest_path(self, start_point, points: list):
        path = [start_point]
        remaining_points = points.copy()

        while remaining_points:
            distances = [euclidean(path[-1], point)
                         for point in remaining_points]
            min_index = np.argmin(distances)
            closest_point = remaining_points[min_index]

            path.append(closest_point)
            remaining_points.remove(closest_point)

        return path

    def pixels_to_coorindate(self, pixels):
        map_coordinates = []
        for coordinates in pixels:
            x = coordinates[0]*self.resolution_+self.origin_x_
            y = coordinates[1]*self.resolution_+self.origin_y_
            map_coordinates.append((x, y))

        return map_coordinates

    def map_path(self):
        pixels = self.extract_red_pixels(self.image_path_)
        print('pixels: '+str(len(pixels)))
        sorted_pixels = self.find_shortest_path(self.first_pixels_, pixels)
        # coordinates = self.pixels_to_coorindate(sorted_pixels) # convert all points
        filtered_pixels = sorted_pixels[::10]
        coordinates = self.pixels_to_coorindate(filtered_pixels)
        print('pixels 2 : '+str(len(coordinates)))
        path = Path()
        path.header.stamp = rospy.Time.now()
        path.header.frame_id = "map"
        print(coordinates)
        for coordinate in coordinates:
            pose = PoseStamped()
            pose.header.stamp = rospy.Time.now()
            pose.header.frame_id = "map"
            pose.pose.position.x = coordinate[0]
            pose.pose.position.y = coordinate[1]
            pose.pose.position.z = 0
            pose.pose.orientation.x = 0
            pose.pose.orientation.y = 0
            pose.pose.orientation.z = 0
            pose.pose.orientation.w = 1
            path.poses.append(pose)
        return path

    def path_publish(self, event):
        self.read_yaml_file(self.yaml_path_)
        self.path_pub_.publish(self.map_path())
        print("path published")


def ouob():
    rospy.init_node('map_path_node')
    # enter your file path
    node = MapPathNode('/home/asd/catkin_ws/src/map.jpg',
                       '/home/asd/catkin_ws/src/map.yaml')
    # node = MapPathNode('/home/asd/Robotics_ws/src/maps/map_LG2_indoor_0616_2_2023-06-16-12-23-40.jpg',
    #                    '/home/asd/Robotics_ws/src/maps/map_LG2_indoor_0616_2_2023-06-16-12-23-40.yaml')
    rospy.sleep(5.0)
    node.path_publish(123)


if __name__ == '__main__':
    ouob()
