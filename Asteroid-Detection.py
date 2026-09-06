import cv2
video=cv2.VideoCapture("Video.mp4")
while True:
    rat,frame=video.read()
    
    if rat==False:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,40,255,cv2.THRESH_BINARY)
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        
        if (area>600 and area<120000):
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            xx=int((w/2)+x-50)
            cv2.circle(frame,(int(x+w/2),y),5,(0,0,255),-1)
            cv2.circle(frame,(int(x+w/2),y+h),5,(0,0,255),-1)
            cv2.putText(frame,"Height: "+str(h),(xx,y-2),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow('live',frame)
    x=cv2.waitKey(10)
    if x==113:
        break
video.release()
cv2.destroyAllWindows()
