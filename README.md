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
   
Code Material of EyeForYou Project

First, install opencv and other modules using this command 

`pip install  -r requirements.txt`

For running the program, use this command

`sudo python3 main.py`

Important : the sudo is necessary because of the "keyboard" module, which 
only works on root

The pytesseract library is also necessary for the OCR to work for more information on how to install it:   

   https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
  
   ## Used Libraries:
    ### YOLO :
    You only look once (YOLO) is a state-of-the-art, real-time object detection system
   ![Alt text](yolo_lib/object-detection.jpg?raw=true "Object Detection")
   
   We used a pretrained model developped by Darknet:
         https://pjreddie.com/darknet/yolo/
