# Project 1

This assignment is meant to make sure that you are familiar with the most basic functions of ROS. Please make sure that you have completed (or at least read through) the tutorials 1-6 & 11-13.

In this assignment you are tasked with writing a node that subscribes to a topic and publishes to another. Your code will subscribe to a topic called 'two_ints', on which a custom message containing two integers can be broadcast. Make sure to familiarize yourself with the message format of this topic (have a look at the TwoInts.msg in the msg directory). Those two integers are to be added and the result published to topic 'sum' as an Int16 from std_msgs. 
## Setup
- run roscore
- execute source two_int_talker.py
- Finaly execute solutionE1.py

## Implementation

You must implement your code in the file ~/catkin_ws/src/project1_solution/scripts/solution.py . This file has already been created for you and any starter code has been placed inside. 

## Testing

To test your code, you have multiple options:

Add some debug output to your publisher (i.e. print the two numbers you have just received as well as their sum to the console every time you are about to publish). Then simply run your node (rosrun project1_solution solution.py). This is useful to see that you are getting to the right place in your code, but will not tell if you are actually publishing, and publishing to the right topic.
