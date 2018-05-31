#https://www.youtube.com/watch?v=z_6fPS5tDNU&index=18&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq
#https://www.youtube.com/watch?v=t0HOVLK30xQ&index=19&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq
#images from 
import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    #http://image-net.org/api/text/imagenet.sysnet.geturls?wnid=n07942152
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1
    #update to latest num in directory after finished with neg images

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))
store_raw_images()

#pull one of ugly pictures out make folder 'uglies' asn stick it in there
def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly, question).any()):
                        print('ugly pic')
                        print(current_image_path)
                        print('ugly pic')
                        os.remove(current_image_path)

                                                            
                except: Exception as e:
                    print(str(e))


def create_pos_n_neg():
    for file_type in ['neg']:

        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type'/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
            elif file_type == 'pos'
                line = file_type+'/'+img+'1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
                                                            
#after first two ran
#find_uglies()

create_pos_n_neg()

## --- upload two folders of images to servers

##mkdir data
##mkdir info
##opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 maxzangle  0.5 -num NUMOFIMAGES
##opencv_createsamples -info info/info.lst -num NUMOFIMAGES -w 20 -h 20 -vec positives.vec
##nohup pencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -num
  #Stages 10 -w 20 -h 20 &
##crontab -e
##apt-get install h-htop
##* * * * * sudo echo 1> /proc/sys/vm/drop_caches
##* * * * * sudo echo 2> /proc/sys/vm/drop_caches
##* * * * * sudo echo 3> /proc/sys/vm/drop_caches
##* * * * * sudo echo 1> /proc/sys/vm/drop_caches

##
