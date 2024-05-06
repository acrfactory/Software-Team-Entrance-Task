import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from interfaces.msg import Completed
import math

class Distance(Node):
    def __init__(self):
        super().__init__("distance")
        try:
            self.sub = self.create_subscription(NavSatFix, "GCS", self.subscribercallback, 10)
        except:
            self.get_logger().info("Could not subscribe to topic 'GCS' with message type 'NavSatFix'")
        self.pub = self.create_publisher(Completed, "Dish", 10)
        # self.timer = self.create_timer(1, self.timercallback)

    def subscribercallback(self,msg):
            k = msg.latitude
            l = msg.longitude
            heading = self.get_heading(l, k)
            distance = self.get_distance(l, k)
            completed_msg = Completed()
            completed_msg.latitude = k
            completed_msg.longitude = l
            completed_msg.distance = distance
            completed_msg.heading = heading
            self.pub.publish(completed_msg)


    def get_heading(self, longitude, latitude):
        lat1 = math.radians(latitude)
        lon1 = math.radians(longitude)
        lat2 = math.radians(51.42287924341543)
        lon2 = math.radians(-112.64106837507106)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        y = math.sin(delta_lon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
        bearing = math.atan2(y, x)
        bearing = math.degrees(bearing)
        bearing = (bearing + 360) % 360
        heading = round(bearing, 1)
        return heading
    
    def get_distance(self, longitude, latitude):
        lat1 = math.radians(latitude)
        lon1 = math.radians(longitude)
        lat2 = math.radians(51.42287924341543)
        lon2 = math.radians(-112.64106837507106)

        RADIUS = 6365.766

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = math.sin(delta_lat/2.0)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(delta_lon/2.0)**2
        b = math.sqrt(a)
        distance = 2*RADIUS*math.asin(b)
        return round(distance * 1000,1)

def main():
    rclpy.init()
    node = Distance()
    rclpy.spin(node)
    node.destroy_client()
    rclpy.shutdown()