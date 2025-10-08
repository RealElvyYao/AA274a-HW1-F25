#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64, Bool, String
from geometry_msgs.msg import Twist

class Heartbeat(Node):
    def __init__(self) -> None:
        #initialize base class
        super().__init__("heartbeat")

        # self.hb_pub = self.create_publisher(String, "/heartbeat", 10)

        self.hb_pub = self.create_publisher(Twist, "/cmd_vel", 10)

        self.hb_timer = self.create_timer(0.2, self.hb_callback)

        self.hb_sub = self.create_subscription(Bool, "/kill", self.hb_emerg, 10)

        # self.hb_sub = self.create_subscription(String, "/heartbeat", self.hb_callback, 10)

    def hb_callback(self) -> None:
        # msg = String()
        # msg.data = "sending constant control..."

        twistMsg = Twist()
        twistMsg.linear.x = 0.2
        twistMsg.angular.z = 0.5

        self.hb_pub.publish(twistMsg)
        # self.hb_timer = self.create_timer(0.2, self.hb_callback)

    def hb_emerg(self, msg:Bool) -> None:
        if msg.data:
            self.hb_timer.cancel()
            twistMsg = Twist()
            twistMsg.linear.x = 0.0
            twistMsg.angular.z = 0.0

            self.hb_pub.publish(twistMsg)





if __name__ == "__main__":
    rclpy.init()
    node = Heartbeat()
    rclpy.spin(node)
    rclpy.shutdown()