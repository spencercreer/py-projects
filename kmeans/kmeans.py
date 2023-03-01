import numpy as np
import math
import matplotlib.pyplot as plt

n = 50
p = 2
k = 3

data = np.random.random((n,p))

i_point = data[np.random.choice(n, 1, replace=False)]

def kPlusPlusCents(k, initCent, points):
    centroids = np.zeros((k, 2))
    centroids[0] = initCent

    for i in range(1, k):
        dist = np.zeros((points.shape[0], i))
        for j in range(i):
            dist[:,j] = ((points-centroids[j])**2).sum(axis=1)**0.5

        furthestPoint = points[np.argmax(np.mean(dist, axis=1))]
        centroids[i] = furthestPoint
        points = np.delete(points,np.argmax(np.mean(dist,axis=1)),axis=0)
        
    return centroids

cents1 = kPlusPlusCents(k, i_point, data.copy())

def kMeans(X, centers):
    n = X.shape[0]
    k = centers.shape[0]
    closest = np.zeros(n).astype(int)
    distances = np.zeros((n, k))
    
    while True:
        old_closest = closest.copy()
        for i in range(k):
            distances[:,i] = ((X-centers[i])**2).sum(axis=1)**0.5

        closest = np.argmin(distances, axis=1)

        for i in range(k):
            centers[i,:] = X[closest == i].mean(axis=0)
            
        if all(closest == old_closest):
            break
            
    return centers, closest

centers, closest = kMeans(data, cents1)
cost = 0
for i in range(k):
    cost += ((data[closest == i] - centers[i])**2).sum()
print("\nk centers:")
print(centers)
print("\nk loss:")
print(cost)  

plt.scatter(data[:,0], data[:,1],c=closest)
plt.show()
