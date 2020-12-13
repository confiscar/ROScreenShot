#!/usr/bin/env python
import rospy
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# Settings
image_topic = "/camera/rgb/image_raw"
path = "screenshot/" 
file_name = "image"
extension = ".jpg"

# Advanced Settings
callback_freq_in_hz = 10
name_counter_start = 0


class ROScreenShot:
    def __init__(self):
        print("Using configuration:")
        print("===============")
        print("Topic : {}".format(image_topic))
        print("File Name : {}".format(file_name))
        print("Path : {}".format(path))
        print("Extension : {}".format(extension))
        print("===============")
        print("To configure, modify ROScreenShot.py")
        print("Remember, to save to folders, they must be created beforehand.")
        print("===============")
        
        rospy.init_node('ROScreenShot')
        self.bridge = CvBridge()
        self.screenshot = False
        self.count = name_counter_start
        self.rate = rospy.Rate(callback_freq_in_hz)
        
        rospy.Subscriber(image_topic, Image, self.camera_callback)
        self.keyboard_listener()
    

    def camera_callback(self, image):
        if self.screenshot:
            cv2_img = self.bridge.imgmsg_to_cv2(image, "bgr8")
            cv2.imwrite(os.path.join(path, file_name + str(self.count) + extension), cv2_img)
            
            print("Saved {}...".format(os.path.join(path, file_name + str(self.count) + extension)))
            
            self.count += 1
            self.screenshot = False
        
        self.rate.sleep()


    def keyboard_listener(self):
        while True:
            query = raw_input("Enter to screenshot, Q to exit. \n")
            if query == "":
                self.screenshot = True
            elif query == "q" or query == "Q":
                print("Exiting...")
                exit()
            

if __name__ == "__main__":
    ross = ROScreenShot()
