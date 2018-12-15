# **Smart Stick For Blind Using OPENCV on RPI**


## Description

This projects helps blind people to get aware of their surroundings.It uses a simple webcam attached to a Raspberry Pi which does object detection using OPENCV HaarCascades to do so.Presently it is able to detect only persons and cars but can be implemented to detect other classes of objects also.It also tells the **distance** of detected object along with it's **speed** (also tells whether the object is moving towards or away from the user) that too only through camera.Once Detected, it tells the person regarding the object via voice feedback. 

The main advantage of this project is it does not require any internet connection and also is very handy(doesn't require bulky hardware).

## Working

The camera mounted on the stick captures the video(livestream) and sends it to Raspberry PI for processing.RPi uses OPENCV(HaarCascades) to detect the objects in the frame.It also calculates the **distance and speed of the detected objects along with the direction of their movement**.Once done with the calculations it passes all the information to the user via **voice feedback**.

### TO-DO's
* Code cleanup
* Optimizing the code to reduce frame drops.
* Adding more classes of objects to detection.
