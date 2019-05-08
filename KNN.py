# k-nn algorithm
# Álvaro García Tenorio, Belén Serrano Antón


import operator
import math

class KNN:
#This module contains the basic functions to implement the KNN algorithm

    
    # trainData represents the points we use to train the algorithm
    #by [coord1,..., coordn, "class"]
    # k is the number of neighbors we are using
    def __init__(self, trainData, k):
        self.trainingData = trainData
        self.k = k    
    
    #Returns the euclidean distance given two points
    def euclideanDistance(self,point1, point2, length):
    	distance = 0
    	for i in range(length):
    		distance += pow((point1[i] - point2[i]), 2)
    	return math.sqrt(distance)
    
    
    #Given a point, this function returns the k nearest neighbors 
    # neighbors = [point][dist=0]
    def getNeighbors(self, point):
    	distances = [] #keeps the distance between point and a point in the 
                        #trainData
    	length = len(point)-1 #not to use the "class" element
    	for i in range(len(self.trainingData)):
    		dist = self.euclideanDistance(point, self.trainingData[i], length)
    		distances.append((self.trainingData[i], dist))
            
    	distances.sort(key=operator.itemgetter(1)) #order the distances by 
                                                #distance
    	neighbors = [] #keeps the k nearest neighbors
    	for i in range(self.k): 
    		neighbors.append(distances[i][0])
    	return neighbors
    
    #We calculate the class that appears most often in neighbors
    def calculateNeighborsClass(self, neighbors): 
        count = {}; #set of classes that appear in neighbors
        maxClassCount = 0 #number of times that the most often class appears
        maxClass = 0 #class that appears most often in neighbors
        indexNeighborClass = len(neighbors[0])-1 #coordenate that keeps the 
                                            #class of a point
        for i in range(self.k): 
            if(neighbors[i][indexNeighborClass] not in count): 
                # The class at the ith index 
                # is not in the count dict. 
                # Initialize it to 1. 
                count[neighbors[i][indexNeighborClass]] = 1; 
            else: 
                # Found another item of class
                #neighbors[i][indexNeighborClass].
                #Increment its counter. 
                count[neighbors[i][indexNeighborClass]] += 1; 
                if(count[neighbors[i][indexNeighborClass]] > maxClassCount):
                    maxClassCount = count[neighbors[i][indexNeighborClass]]
                    maxClass = neighbors[i][indexNeighborClass]
        return maxClass;
    
    #Given a point we calculate its class
    def classify(self, newPoint):
        neighbors = []; 
     
        neighbors = self.getNeighbors(newPoint); 
     
        return self.calculateNeighborsClass(neighbors);
    
    
    
    