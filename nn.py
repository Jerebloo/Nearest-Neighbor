#Jeremy Yu
#403 Assignment 4

#reference
#Class notes used for def__init__, label=0 default parameter
# %f formatting from python docs
# distance calculations based on formulas taken from wikipedia
# Sample.__init__(self, inArr) override from python docs
#if elif structure from python docs
# math.sqrt from class, math.fabs from python docs
# .append from docs
# definition structure from class, use of None from class

# algorithm
# Sample attaches an array and a label to the Sample object you create
# The 3 distance classes inherit sample, when an object is made
# the super class sample is called and the array and label are 
# attached to the distance class. Then distance can be calculated
#by passing in an array y in this example x.distance(y)
#array size differences are checked and then the smaller array is 
# appended with 0s. Then distance is calculated. For euclid for example
# using our earlier set up x.distance(y), 
#sqrt (sum from i to end of array of (x[i]-y[i])^2)
#taxicab: sum from i to end of array of abs(x[i]-y[i])
#MaxDistance: check all abs(x[i]-y[i]) and return the largest
#finally we have the classifier , this will create an object
#with an empty list and a length of that list
#then you can add Sample objects to it with addSample
#this will place the Sample at the end of the list and increment
#the size of the list by 1
#predict label takes one of the distanceSample class objects and 
# calculates one of the 3 distances to each Sample in the classifier
# the resulting least distance is found, the sample associated
# with this least distance is looked at and it's label is extracted and 
# returned


import math
class Sample:
    def __init__(self, inArr,label=0):    
        self.inArr= inArr
        self.index = len(inArr)
        self.label=label
                
    def distance(self, inArr2):
        return
class EuclideanSample(Sample):
    def __init__(self, inArr):    
        Sample.__init__(self, inArr)
        
    def distance(self, inArr2):
        i=0
        j=0
        total=0
        if self.index > inArr2.index:
            arrDiff = self.index - inArr2.index
            while j < arrDiff:
                inArr2.inArr.append(0)
                inArr2.index = inArr2.index+1
                j=j+1
        elif self.index < inArr2.index:
            arrDiff = inArr2.index - self.index
            while j < arrDiff:
                self.inArr.append(0)
                self.index =self.index+1
                j=j+1
        while(i<self.index):
            total = (self.inArr[i] - inArr2.inArr[i])**2 + total
            i=i+1
        return "%f" % (math.sqrt(total))

class TaxicabSample(Sample):
    def __init__(self, inArr):    
        Sample.__init__(self, inArr)
        
    def distance(self, inArr2):
        i=0
        j=0
        total=0
        if self.index > inArr2.index:
            arrDiff = self.index - inArr2.index
            while j < arrDiff:
                inArr2.inArr.append(0)
                inArr2.index = inArr2.index+1
                j=j+1
        elif self.index < inArr2.index:
            arrDiff = inArr2.index - self.index
            while j < arrDiff:
                self.inArr.append(0)
                self.index =self.index+1
                j=j+1
        while(i<self.index):
            total = math.fabs(self.inArr[i] - inArr2.inArr[i]) + total
            i=i+1
        return "%f" % (total)

class MaximumSample(Sample):
    def __init__(self, inArr):    
        Sample.__init__(self, inArr)
        
    def distance(self, inArr2):
        i=0
        j=0
        if self.index > inArr2.index:
            arrDiff = self.index - inArr2.index
            while j < arrDiff:
                inArr2.inArr.append(0)
                inArr2.index = inArr2.index+1
                j=j+1
        elif self.index < inArr2.index:
            arrDiff = inArr2.index - self.index
            while j < arrDiff:
                self.inArr.append(0)
                self.index =self.index+1
                j=j+1
        
        maxDist = 0
        while(i<self.index):
            dist = math.fabs(self.inArr[i] - inArr2.inArr[i])
            if maxDist < dist:
                maxDist = dist
            i=i+1
        return "%f" % (maxDist)

class Classifier:
    def __init__(self):    
        self.samples=[]
        self.index = len(self.samples)
    def addSample(self,sampl):
        self.samples.append(sampl)
        self.index = self.index+1
        return self.samples
    def predictLabel(self,distanceSample):
        
        i=0
        minDistance=None
        currentDistance=0;
        currentLabel=None
        
        while(i<self.index):
            
            currentDistance = distanceSample.distance(self.samples[i])
            if minDistance is None:
                minDistance = currentDistance
                currentLabel = self.samples[i].label
            elif currentDistance < minDistance:
                minDistance = currentDistance
                currentLabel = self.samples[i].label
            i = i+1
        return (currentLabel)


