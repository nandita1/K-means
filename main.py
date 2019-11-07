import csv
import numpy as np
import copy

x=[]
y=[]
centroids=[]
closest=[] #contains the closest distance
closest_centroid=[] #cluster number
np.random.seed(200)
k=int(input('Enter the value of k you want: '))

#opening csv file and storing the values of x and y
with open('xy.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        x.append(int(line[0]))
        y.append(int(line[1]))


#initialising the centroids
for i in range(k):
    centroids.append([np.random.randint(0, 80), np.random.randint(0, 80)])

#take the value of p
p=int(input('Enter the value of p you want: '))


def dist(i,j):
    return np.power(abs(x[j]-centroids[i][0])**p + abs(y[j]-centroids[i][1])**p, (1/float(p)))


def assignment():
    del closest[:]
    del closest_centroid[:]
    #assigning the distance of each point from each centroid
    for j in range(len(x)):
        distance = []
        for i in range(k):
            distance.append(dist(i,j))
        closest.append(min(distance))
        closest_centroid.append(distance.index(min(distance)))

assignment()

def update():
    indices=[]
    for i in range(k):
        indices.append([j for j,x in enumerate(closest_centroid) if closest_centroid[j]==i])

    for i in range(k):
        sum_x=0
        sum_y=0
        count=0
        for j in indices[i]:
            sum_x+=x[j]
            sum_y+=y[j]
            count+=1
        centroids[i][0]=sum_x/count
        centroids[i][1] = sum_y/count

#update()

while True:
    old_centroids=copy.deepcopy(closest_centroid)
    update()
    assignment()
    if old_centroids==closest_centroid:
        break
for i in range(len(closest_centroid)):
    closest_centroid[i]+=1
print(closest_centroid)

