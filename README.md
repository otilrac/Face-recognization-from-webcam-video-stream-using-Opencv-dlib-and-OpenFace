# Face-rcognization-from-webcam-video-stream-using-Opencv-dlib-and-OpenFace
A physical security application using computer vision 

This system uses the video stream from webcam and classify the persons infront of camera as known a person or a unknown person.

[![Youtube Video](https://img.youtube.com/vi/k-1fj8XPBCQ/0.jpg)](https://www.youtube.com/watch?v=k-1fj8XPBCQ)
#### click on this image to see the demo

## Requirements
* **requirements.txt** contains all the packages used in devlopement of this system. 
* Most important dependecies of this system are dlib, opencv, openface and tkinter

## Working
* **Enployees** directory contains contains the images of persons for whom the system should show as know person.
* **datataker.py** helps in taking images from webcam and placing them in the employee directory.
* **employee_embeddeds.py** will generate the csv file  of embeddeds of faces in employee file.
* By running the **bolteye.py** you will encounter a application developed using Tkinter which ask for a username and password

    username : kaushik and password : bolt1234

* login button will lanch a python file ####dlib_image.py#### which actually classify the persons in video stream as a known person or unknown person
* you see the 'known person' or 'unknown person' right above the bounding box of the face

## Acknowledgements
* special thanks to Kaushik yathi raj and harshavardhan for developing frontend application and great UI

## License
 Boltzeye  Copyright (C) 2019   T Bharath Chandra
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
