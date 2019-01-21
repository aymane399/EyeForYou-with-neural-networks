# Eye for you main program

import keyboard
import cv2
import time
import argparse
import logging
import pyttsx3
import sys

saying = 1
logger = logging.getLogger('Eye For You Webcam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
sys.path.append('\ocr')
sys.path.append('\yolo')
from yolo_lib import yolo as yl
from ocr import text_recognition


############## Text Recognition ################

def Read_Text(image):
    return (image, [])


################################################

############## Obstacle Recognition ############

def Obstacle_Recognition(image):
    return (image, [])


################################################

############## Face Recognition ################

def Face_Recognition(image):
    return (image, [])


def Do_Nothing(image):
    return (image, [])


################################################
def say(text, language, ch_mode):
    '''engine = pyttsx3.init()
    engine.say("Object Recognized " + text)
    a=engine.runAndWait()'''
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    dictio = {'fr' : voices[0] , 'eng' : en_voice_id}
    # for voice in voices:
    voice_id = dictio[language]
    engine.setProperty('voice', voice_id)
    # print voice.id
    #engine.say('Object Recognized' + text)
    engine.say(ch_mode + text)
    a = engine.runAndWait()  # blocks

if __name__ == '__main__':

    # All the args argument:
    parser = argparse.ArgumentParser(description='Main-Code')
    # parser.add_argument('--video', type=str, default='')
    parser.add_argument('--camera', type=int, default=0)
    parser.add_argument('--saying', type=int, default=0, help='Save in a video format')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--save_video', type=str, default='', help='Save in a video format')
    args = parser.parse_args()

    # cap = cv2.VideoCapture(args.video)
    cam = cv2.VideoCapture(args.camera)

    if args.save_video != '':
        print('Saving the frames at %s' % args.save)
    fps_time = 0
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))
    frames_counter = 1
    # Default Mode
    Mode = 'Do Nothing'
    while True:
        # Capturing the frame:
        ret_val, image = cam.read()
        language = "eng"
        ch_mode = ""
        ################### Inputs #####################

        if keyboard.is_pressed('a'):
            Mode = 'Read Text'
            language = 'fr'
            ch_mode ='Text recognized'

        elif keyboard.is_pressed('z'):
            Mode = 'Obstacle Recognition'
            language = 'eng'
            ch_mode = 'Object recognized'

            saying = True
        elif keyboard.is_pressed('e'):
            Mode = 'Face Recognition'

        elif keyboard.is_pressed('r'):
            Mode = 'Do Nothing'
        elif keyboard.is_pressed('t'):
            Mode = 'Obstacle Recognition'
            saying = True
        Functions = {'Read Text': text_recognition.ocr, 'Obstacle Recognition': yl.yolo, 'Face Recognition': Face_Recognition,
                     'Do Nothing': Do_Nothing}
        if frames_counter % 3 == 0:
            output, text = Functions[Mode](image)
            try :
                cv2.putText(output, "FPS: %f Mode Detection : %s" % ((1.0 / (time.time() - fps_time)), Mode), (10, 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.imshow('computation result', output)
            except :
                pass
            if saying:
                say(str(text) , language, ch_mode)

        frames_counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        fps_time = time.time()
    cv2.destroyAllWindows()

################################################


################### Outputs ####################


################################################
