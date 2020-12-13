# ROScreenShot
ROScreenshot is a quick python script, thrown together with the purpose
of providing a way of screenshotting camera feeds broadcasted as ROS 
topic.

It was created for the purpose of collecting images to train NN's for the
purpose of object detection. Feel free to submit any PRs.

## How to use

* Clone the repo anywhere. Keep in mind the images will be stored by default in the same folder.
* Make sure the camera is broadcasting to the correct topic.
* Configure the setting variables in the script as needed. (Path setting can be relative or absolute. Make sure the folders are created beforehand as the script can't create folders.)
* Run the script from a correctly setup terminal. 
* Press enter to take a screenshot, press Q and enter to exit.
* If run multiple times, remember to chance file names, or it will start overwriting images as the counter sets to 0.
