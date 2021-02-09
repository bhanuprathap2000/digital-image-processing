#Import required library
import cv2
import numpy as np
from matplotlib import pyplot as plt
import urllib

img = cv2.imread('waterfall.jpg')
im = cv2.imread('waterfall.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',im)
# plt.imshow(img, cmap = 'gray')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)
print(gray.shape)
print(gray[1][1])

plt.imshow(gray, cmap = 'gray')



def convertToBinary(my_dec):
    l=[]
    while my_dec>0:
        #print(my_dec)
        rem=my_dec%2
        my_dec=my_dec//2
        #print(my_dec)
        l.append(rem)
        #print(l)         
    l.reverse()
    new=np.zeros(8 -len(l))
    ow=np.append(new,l)
    return ow

k=convertToBinary(2)
print(k)
k=convertToBinary(200)
print(k,type(k))

out=[]
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        #print(img[i][j])
        outp=convertToBinary(gray[i][j])
        out.append(outp)

print(outp,outp[1])
#out

jv=np.asarray(out)
print(jv,jv.shape)
print(jv[0][1],jv[1][1])

one = np.array([int(i[0]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
two= np.array([int(i[1]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
three = np.array([int(i[2]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
four = np.array([int(i[3]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
five = np.array([int(i[4]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
six = np.array([int(i[5]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
seven= np.array([int(i[6]) for i in jv],dtype = np.uint8).reshape(img.shape[0],img.shape[1])
eight = np.array([int(i[7]) for i in jv],dtype = np.uint8) .reshape(img.shape[0],img.shape[1])

print(one,two,three)

plt.imshow(one, cmap = 'gray')
plt.show()

plt.imshow(one, cmap = 'gray')
plt.title("1st plane")
plt.show()
plt.imshow(two, cmap = 'gray')
plt.title("2nd plane")
plt.show()


plt.imshow(three, cmap = 'gray')
plt.title("3rd plane")
plt.show()
plt.imshow(four, cmap = 'gray')
plt.title("4th plane")
plt.show()

plt.imshow(five, cmap = 'gray')
plt.title("5th plane")
plt.show()
plt.imshow(six, cmap = 'gray')
plt.title("6th plane")
plt.show()

plt.imshow(seven, cmap = 'gray')
plt.title("7th plane")
plt.show()
plt.imshow(eight, cmap = 'gray')
plt.title("8th plane")
plt.show()