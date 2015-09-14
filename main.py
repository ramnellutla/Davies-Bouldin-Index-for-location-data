'''
Created on April 8, 2015

@author: Sai Ram Nellutla
'''
import random as rand
from point import Point
from calc import Calc
import csv

clusters = {} #[[points in the cluster],Number of points in the cluster, Centroid of the cluster, Average of distances between points and centroid of the cluster]
clustCount = 0 #Number of clusters found
algoName = "" #Name of the clustering Algorithm
flag = 0
#read the location from the csv input file and store each location as a Point(latit,longit) object
f = open('input.txt', 'r')
h= open('output','a')
reader = csv.reader(f, delimiter=",")
for line in reader:
	if flag is 1:
		if len(line) is 2:
			if clustCount in clusters:
		    		loc_ = Point(float(line[0]), float(line[1]))  #tuples for location
					elemCount += 1
		    		clusters[clustCount][0].append(loc_)
					clusters[clustCount][1] = elemCount
			else:
		    		loc_ = Point(float(line[0]), float(line[1]))  #tuples for location
		    		clusters[clustCount] = [[loc_],elemCount,Point(0,0),0]						
		else:
			clustCount += 1 
			print "Processing Cluster:" + str(clustCount)
			elemCount = 1 #Number of elements in the cluster
	else:
		algoName=line[0] 
		flag = 1
print str(clustCount) + " Clusters found"

# finding centroid of each cluster and average distance of all elements in cluster to its centroid
for key in clusters:
	cal = Calc(clusters[key][0])
	centroid = cal.centroid(clusters[key][1])
	clusters[key][2] = Point(centroid.latit,centroid.longit) #Centroid of the cluster
	clusters[key][3] = cal.avgDist(centroid,clusters[key][1]) #Average distance of the points of the cluster from the centroid

dbIndex = 0
print "Calculated Centorid and Average Distance"

for key1 in clusters:
	numer = 0
	denom = 0
	maximum = 0
	for key2 in clusters:
		if key1 != key2:
			numer = clusters[key1][3] + clusters[key2][3]
			denom =  cal.distance(clusters[key1][2].latit,clusters[key1][2].longit,clusters[key2][2].latit,clusters[key2][2].longit)	
			tempVal = numer/denom
			if tempVal > maximum:
				maximum = tempVal
	dbIndex += maximum

print "DB-Index of "+ algoName +": " + str(dbIndex/clustCount)  
h.write("DB-Index of "+ algoName +": " + str(dbIndex/clustCount)+"\n")


