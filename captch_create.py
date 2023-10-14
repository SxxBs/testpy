from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import os

NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)


# 图像大小
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160

TRAIN_DATASET_PATH = 'dataset' + os.path.sep + 'train'
TEST_DATASET_PATH = 'dataset' + os.path.sep + 'test'
PREDICT_DATASET_PATH = 'dataset' + os.path.sep + 'predict'


def random_captcha(length):
    captcha_text = []
    for i in range(length):
        c = random.choice(ALL_CHAR_SET)
        captcha_text.append(c)
    return ''.join(captcha_text)


#path = TRAIN_DATASET_PATH
path = TEST_DATASET_PATH
if not os.path.exists(path):
        os.makedirs(path)
count = 10

'''for i in range(4,8):
    for j in range(count):
        image = ImageCaptcha()
        captcha_text = random_captcha(i)
        captcha_image = Image.open(image.generate(captcha_text))
        now = str(int(time.time()))
        filename = captcha_text+'_'+now+'.png'
        captcha_image.save(path  + os.path.sep +  filename)
        print('saved %d : %s' % (i+1,filename))
'''

for i in range(4,8):
    for j in range(count):
        image = ImageCaptcha()
        captcha_text = random_captcha(i)
        captcha_image = Image.open(image.generate(captcha_text))
        filename = captcha_text+'.png'
        captcha_image.save(path  + os.path.sep +  filename)
        print('saved %d : %s' % (i+1,filename))


   
   
        
        
        