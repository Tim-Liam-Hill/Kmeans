import numpy as np
import pandas

def kmeans(centroids, arr):
    while(True):
        groups = assignPointsToClusters(centroids, arr)
        new_centroids = updateClusters(groups)

        if(np.array_equal(new_centroids, centroids)):
            return centroids
        else: centroids = new_centroids

def assignPointsToClusters(centroids, arr):
    groups = []
    
    for c in centroids:
        groups.append([c, []])
        
    for p in arr:
        min_distance = 10000000
        cent = []
        for c in centroids:
            dist = np.linalg.norm(p - c)
            if(dist < min_distance):
                cent = c
                min_distance = dist
        for x in groups:
            if(all([x[0][i]==cent[i] for i in range(len(cent))]) ):
                x[1].append(p)
        
    return groups

def updateClusters(groups):
    newCentroids = []
    for x in groups:
        new_x = x[1][0] 
        for point in x[1][1:]:
            new_x = new_x + point
        newCentroids.append(np.true_divide(new_x, len(x[1])))
    return newCentroids
