# EyeForYou

   
   ## License
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
   

   ## Launch Program
   
### Code Material of EyeForYou Project

First, install opencv and other modules using this command 

`pip install  -r requirements.txt`

For running the program, use this command

`sudo python3 main.py`

Important : the sudo is necessary because of the "keyboard" module, which 
only works on root

   
   ### Instructions 
 The programm is launched by calling the main function and the user can interact using the keyboard:
 So far three modes are available :
   - Do nothing mode (By pressing 'r' in the keyboard)
   - Object recognition mode (By pressing 'z' in the keyboard) : applies YOLO to the rendered frames and vocally outputs the results.
   - Character recognition mode (By pressing 'a' in the keyboard) : applies OCR to the rendered frames and vocally outputs the recognized words.
  
   ## Used Libraries:
    
   ### YOLO :
   You only look once (YOLO) is a state-of-the-art, real-time object detection system
   ![Alt text](yolo_lib/object-detection.jpg?raw=true "Object Detection")
   
   We used a pretrained model developped by Darknet:
         https://pjreddie.com/darknet/yolo/
         
   For the program to work, the weigths file must be downloaded and put in yolo_lib directory.
   This can be done through the following link:
      https://pjreddie.com/media/files/yolov3.weights
         
   ### OCR :
   Optical character recognition using LSTM neural network relying on the pytesseract library:
   ![Alt text](ocr/images/example.jpg?raw=true "Character recognition")
   
   The pytesseract library is necessary for the OCR to work for more information on how to install it and also on the whole OCR code used :   

   https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
   
   You should also download  the frozen east text detection file from the link belw and place it on the "ocr" directorty.
   https://www.dropbox.com/s/obi5dpekywhtq05/frozen_east_text_detection.pb?dl=0
