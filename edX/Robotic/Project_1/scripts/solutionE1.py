#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from robotic.msg import TwoInts

pub = rospy.Publisher("sum_int", Int16, queue_size=10)


def int_callback(data):
   """rospy.loginfo("Recibe a: %s", data.a)
   rospy.loginfo("Recibe b: %s", data.b)
   rospy.loginfo("Sumatory: %s\n", data.a + data.b)"""
   msg = Int16
   msg = data.a + data.b
   pub.publish(msg)
 

def listener_solution():
   rospy.init_node("listener_solution", anonymous=True)
   rospy.Subscriber("/two_ints", TwoInts, int_callback)
   rospy.spin()
   
if __name__ == '__main__':
   try:
      listener_solution()
   except rospy.ROSInterruptException:
   	pass