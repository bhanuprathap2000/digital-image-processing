import numpy as np

# Numpy Array
h=np.array([[52,55,61,59,79,61,76,61],
[62,59,55,104,94,85,59,71],
[63,65,66,113,144,104,63,72],
[64,70,70,126,154,109,71,69],
[67,73,68,106,122,88,68,68],
[68,79,60,70,77,66,58,75],
[69,85,64,58,55,61,65,83],
[70,87,69,68,65,73,78,90],
])

#importing the matplotlib
from matplotlib import pyplot as plt
plt.imshow(h, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.show()

#zip function allows us to iterate through the two iterators
unique_elements, counts_elements = np.unique(h, return_counts=True)
for val,count in zip(unique_elements, counts_elements):
    print(val,count) 

hist=np.asarray((unique_elements, counts_elements))
#converting element,count into array 
print(hist)
print(hist[0][:])
print(hist[1][:])

#cumulative distribution function

cdf=hist[1][:].cumsum()
print(cdf)
print(cdf.min(),len(cdf))

#appending to the output
out=[]
for i in range(len(cdf)):
    eq=round(((cdf[i]-1)/63)*255)
    out.append(eq)

#converting to numpy array
h_eq=np.uint8(np.asarray(out))
h_eq

hist[0][:]

k = {hist[0][i]: h_eq[i] for i in range(len(h_eq))} #list comprehension
print(k)
print()
print(k.get(55),type(k.get(55)))
print()
print(k[55])

b=h
print(b[1][1])
print(b)


for i in range(8): 
    for j in range(8): 
            t=k.get(b[i][j])
            b[i][j]=t
            

print(b) #printing
#plotting 
plt.imshow(b, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.show()