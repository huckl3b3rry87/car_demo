#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import tf2_ros
import math

if __name__ == "__main__":
  rospy.init_node("tf_listener")
  tfBuffer = tf2_ros.Buffer()
  listener = tf2_ros.TransformListener(tfBuffer)
  rate = rospy.Rate(10.0)
  while not rospy.is_shutdown():
    try:
      transformObject = tfBuffer.lookup_transform('odom', 'base_footprint', rospy.Time.now(), rospy.Duration(3.0))
      trans = transformObject.transform.translation
      rot = transformObject.transform.rotation
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
      rospy.loginfo("No transform")
      rate.sleep()
      continue
