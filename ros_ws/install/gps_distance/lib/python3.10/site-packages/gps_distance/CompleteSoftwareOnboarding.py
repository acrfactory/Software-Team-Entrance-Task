import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import math
from interfaces.msg import Completed

class Completing(Node):
    def __init__(self):
        super().__init__("completing")
        self.sub = self.create_subscription(NavSatFix, "GCS",self.subcallback,10)
        self.pub = self.create_publisher(Completed,"Dish",10)
        
    def subcallback(self,msg):
        k = GCStoM(msg.latitude, msg.longitude, 51.42287924341543,-112.64106837507106)
        newmsg = Completed()
        newmsg.latitude = msg.latitude
        newmsg.longitude = msg.longitude
        newmsg.distance = k[0]
        newmsg.heading = k[1]
        self.pub.publish(newmsg)




def GCStoM(lat1, long1, lat2, long2):
    r = 6365.766  # Radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(long2 - long1)
    alpha = math.atan2(dlon, dlat)
    alpha = math.degrees(alpha) #turns it into degrees
    if alpha < 0:
        alpha += 360
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2     
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c * 1000  # Convert to meters
    return (round(d,1), round(alpha,1))


def main():
    rclpy.init()
    node = Completing()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()