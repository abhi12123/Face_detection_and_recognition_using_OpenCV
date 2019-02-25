import cv2
#for i in range(0,11):
i=5
filename = 'mohanlal/'+str(i)+'.jpg'
W = 200.
oriimg = cv2.imread(filename,cv2.IMREAD_COLOR)
height, width, depth = oriimg.shape
imgScale = W/width
newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
newimg = cv2.resize(oriimg,(int(newX),int(newY)))
cv2.waitKey(0)
cv2.imwrite('mohan_det/'+str(i)+'.png',newimg)