import csv
import numpy as np
import copy
import math

items=[]
centroids=[]
closest=[] #contains the closest distance
closest_centroid=[] #cluster number
np.random.seed(200)
k=int(input('Enter the value of k you want: '))

#opening csv file and storing the values of x and y
with open('xy.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        items.append([float(line[0]),float(line[1])])


#initialising the centroids
for i in range(k):
    centroids.append([np.random.randint(0, 80), np.random.randint(0, 80)])




def PearsonCorrelation(item, centroid):
    itemmean=0
    cenmean=0
    for j in range(len(item)):
        itemmean+=item[j]
        cenmean+=centroid[j]
    itemmean=itemmean/float(len(item))
    cenmean=cenmean/float(len(centroid))
    up=0
    dn1=0
    dn2=0
    for i in range(len(item)):
        up+= (item[i] - itemmean) * (centroid[i] - cenmean)
        dn1+=math.pow((item[i] - itemmean), 2)
        dn2+=math.pow((centroid[i] - cenmean), 2)
    if(up!=0):
        return up/(math.sqrt(dn1*dn2))
    else:
        return 1

def Correlation(items,means):
    k=len(means)
    correlations=[]
    for i in range(k):
        correlation=[]
        for item in items:
            cor=PearsonCorrelation(item,means[i])
            correlation.append(cor)
        correlations.append(correlation)
    return correlations

def assignment():
    for j in range(len(closest_centroid)):
        max=-2
        for i in range(len(Correlations)):
            if max<Correlations[i][j]:
                max=Correlations[i][j]
                closest_centroid[j]=i+1



closest_centroid = [0 for i in range(len(items))]
Correlations=Correlation(items,centroids)
assignment()
print(closest_centroid)

def CalculateMean(items,clusters,i,j):
    sum=0.0
    count=0
    z=len(items)
    for k in range(z):
        if(clusters[k]==j+1):
            sum+=items[k][i]
            count+=1
    if(count!=0):
        return(sum/float(count))
    else:
        return -1


def update():
    a=len(centroids)
    b=len(centroids[0])
    for j in range(a):
        for i in range(b):
            num=CalculateMean(items,closest_centroid,i,j)
            if(num!=-1):
                centroids[j][i]=num


while True:
    old_centroids=copy.deepcopy(closest_centroid)
    update()
    assignment()
    if old_centroids==closest_centroid:
        break
print(closest_centroid)

