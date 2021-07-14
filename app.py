import cv2
import numpy as np
image=cv2.imread('../facerecog/goku.jpg')
zeros=np.zeros((image.shape[0],image.shape[1]), np.uint8)
b,g,r=cv2.split(image)
print("blue channel",b)
print("blue channel",g)
print("blue channel",r)
#cv2.imshow("blue",b) {these will show gray scale as bgr are getting splitted to single
#cv2.imshow("Green",g)  to individual b,g,r which is nothing but gray scale}
#cv2.imshow("red",r)


blue=cv2.merge([b+100,zeros,zeros]) #by b+100 you amplify
green=cv2.merge([zeros,g,zeros])
red=cv2.merge([zeros,zeros,r])

cv2.imshow("blue",blue) 
cv2.imshow("Green",green)  
cv2.imshow("red",red)

#cv2.imwrite('Blue Imge.jpg',blue) {this saves your image in current directory note:blue here is an image and not channel}

custom_image=cv2.merge([b,g,r])#blue colour gets amplified
cv2.imshow("original",custom_image) #you get the original image after merging b,g and r




#gray_image=cv2.imread('../facerecog/goku.jpg',0) #by changing the flag u can change the dimension
#gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #by using cv2 module also u can change to gray scale
#cv2.imshow("Grey Goku Frame",gray_image)
#cv2.imshow("Goku origibal",image)
cv2.waitKey(0)






