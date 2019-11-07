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
        items.append([float(line[0]), float(line[1])])


#initialising the centroids
for i in range(k):
    centroids.append([np.random.randint(0, 80), np.random.randint(0, 80)])




def SpearmanCorrelation(item, centroid):
    l1=list(item)
    l1.sort()
    l2=list(centroid)
    l2.sort()
    Rankobj1={}
    Rankobj2={}
    for i in range(1,len(l1)+1):
        Rankobj1[l1[i-1]]=i
        Rankobj2[l2[i-1]]=i
    d=[]
    for j in range(len(item)):
        d.append(abs(Rankobj1[item[j]] - Rankobj2[centroid[j]]))
    dsq=[]
    for j in range(len(item)):
        dsq.append(math.pow(d[j],2))
    sum=0
    for j in range(len(item)):
        sum+=dsq[j]
    n=len(item)
    return (1-6*sum/(n*(n*n-1)))

def Correlation(items,means):
    k=len(means)
    correlations=[]
    for i in range(k):
        correlation=[]
        for item in items:
            cor=SpearmanCorrelation(item,means[i])
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

