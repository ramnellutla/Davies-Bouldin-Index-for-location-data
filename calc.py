'''
Created on April 8, 2015

@author: Sai Ram Nellutla
'''
from math import sin, cos, sqrt, atan2, radians
import random as rand
import math as math
from point import Point
#import pkg_resources
#pkg_resources.require("matplotlib")
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Calc:

	def __init__(self,cluster_):
		self.cluster = cluster_
	
	#this method finds centroid of the cluster
	def centroid(self,elemCount):		
		sumLat = 0
		sumLon = 0
		for point in self.cluster:
			sumLat +=  point.latit
			sumLon += point.longit	
		return Point(sumLat/elemCount,sumLon/elemCount)

	#this method finds the average distance of all elements in cluster to its centroid
	def avgDist(self,centroid,elemCount):	
		sumDist = 0
		for point in self.cluster:
			sumDist += self.distance(point.latit,point.longit,centroid.latit,centroid.longit)
		return sumDist/elemCount
			
	# distacne in miles
    	def distance(self,lat1,lon1,lat2,lon2):
		R = 6373.0
		lat1 = radians(lat1)
		lon1 = radians(lon1)
		lat2 = radians(lat2)
		lon2 = radians(lon2)
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
		c = 2 * atan2(sqrt(a), sqrt(1-a))
		distance = R * c
		return distance						
	


	
