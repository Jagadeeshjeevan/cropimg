import cv2
import numpy as np
import os
infolder = raw_input('Enter input folder path: ')
outfolder = raw_input('Enter output folder path: ')
lst=[]
dirs = os.listdir(infolder)
def draw_circle(event,x,y,flags,param):
    global lst
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(a,(x,y),10,(255,0,0),-1)
        lst.append([x,y])
    if len(lst)==4:
        print (lst)
        global a
        global b



        #pts1 = np.float32(lst)
        #print list
        #pts2 = np.float32([[0, 0], [500, 0], [0, 120], [500, 120]])

        #M = cv2.getPerspectiveTransform(pts1, pts2)

        #dst = cv2.warpPerspective(b, M, (500, 120))

        js = b[lst[0][1]:lst[0][1]+(lst[2][1]-lst[0][1]),lst[0][0]:lst[0][0]+(lst[1][0]-lst[0][0])]
        
        #print lst[0][1],lst[0][1]+(lst[2][1]-lst[0][1]),lst[0][0],lst[0][0]+(lst[1][0]-lst[0][0])
        
        #js = a[320:560,448:745]
        a = np.copy(js)
        lst=[]



# Create a black image, a window and bind the function to window

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.setMouseCallback('image',draw_circle)
count=1
print (len(dirs))
for i in dirs:

    a = cv2.imread(infolder+"/"+i)
    #print (a)
    b=np.copy(a)
    c=np.copy(a)
    while(1):
        cv2.imshow('image',a)

        k=cv2.waitKey(20) & 0xFF
        if k==ord('s') :
            lst=[]
            cv2.imwrite(outfolder+"/"+str(count)+".jpg" , a)
            count=count+1
            os.remove(infolder+"/"+i)
            break
        if k==ord('c'):
            lst = []
            cv2.imwrite(outfolder+"/" + str(count) + ".jpg", a)
            a=np.copy(c)
            count=count+1
        if k==ord('r'):
            lst = []
            #cv2.imwrite(outfolder+"/" + str(count) + ".jpg", a)
            a=np.copy(c)
            #count=count+1
        if k==27:
            lst = []
            count=count+1
            os.remove(infolder+"/"+i)
            break


cv2.destroyAllWindows()

