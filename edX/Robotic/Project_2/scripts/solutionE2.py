#!/usr/bin/env python  
import rospy

import numpy

import tf
import tf2_ros
import geometry_msgs.msg

def publish_transforms():

    #Object_Frame
    qb1 = tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)
    T1 = tf.transformations.concatenate_matrices(tf.transformations.quaternion_matrix(qb1), 
        tf.transformations.translation_matrix((0.0, 1.0, 1.0)))
    object_transform = geometry_msgs.msg.TransformStamped()
    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"
    
    tr1 = tf.transformations.translation_from_matrix(T1)
    object_transform.transform.translation.x = tr1[0]
    object_transform.transform.translation.y = tr1[1]
    object_transform.transform.translation.z = tr1[2]
    
    q1 = tf.transformations.quaternion_from_matrix(T1)
    object_transform.transform.rotation.x = q1[0]
    object_transform.transform.rotation.y = q1[1]
    object_transform.transform.rotation.z = q1[2]
    object_transform.transform.rotation.w = q1[3]
    br.sendTransform(object_transform)

    #Robot_Frame
    qb2 = tf.transformations.quaternion_about_axis(1.5, (0,0,1))
    T2 = tf.transformations.concatenate_matrices(tf.transformations.quaternion_matrix(qb2),
        tf.transformations.translation_matrix((0.0, -1.0, 0.0)))
    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"
    
    tr2 = tf.transformations.translation_from_matrix(T2)
    robot_transform.transform.translation.x = tr2[0]
    robot_transform.transform.translation.y = tr2[1]
    robot_transform.transform.translation.z = tr2[2]

    q2 = tf.transformations.quaternion_from_matrix(T2)
    robot_transform.transform.rotation.x = q2[0]
    robot_transform.transform.rotation.y = q2[1]
    robot_transform.transform.rotation.z = q2[2]
    robot_transform.transform.rotation.w = q2[3]
    br.sendTransform(robot_transform)

    #Camera_frame
    qb3 = tf.transformations.quaternion_from_euler(0.0, 0.0, 0.0)
    T3 = tf.transformations.concatenate_matrices(tf.transformations.translation_matrix((.0 ,0.1, 0.1)), 
        tf.transformations.quaternion_matrix(qb3))
    Tr = tf.transformations.concatenate_matrices(tf.transformations.inverse_matrix(T3), 
        tf.transformations.inverse_matrix(T2),T1)
    point = tf.transformations.translation_from_matrix(Tr)
    direction = numpy.cross(numpy.array([1, 0, 0]),numpy.array([point[0], point[1], point[2]]))
    theta = numpy.arccos(p[0] / numpy.linalg.norm(numpy.array([point[0], point[1], point[2]])))
    T3 = tf.transformations.concatenate_matrices(T3, tf.transformations.rotation_matrix(theta, direction))

    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"

    tr3 = tf.transformations.translation_from_matrix(T3)
    camera_transform.transform.translation.x = tr3[0]
    camera_transform.transform.translation.y = tr3[1]
    camera_transform.transform.translation.z = tr3[2]

    q3 = tf.transformations.quaternion_from_matrix(T3)
    camera_transform.transform.rotation.x = q3[0]
    camera_transform.transform.rotation.y = q3[1]
    camera_transform.transform.rotation.z = q3[2]
    camera_transform.transform.rotation.w = q3[3]
    br.sendTransform(camera_transform)

if __name__ == '__main__':
    rospy.init_node('project2_solution')

    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)