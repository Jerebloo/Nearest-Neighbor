# -*- coding: utf-8 -*-

from nn import *

cl=Classifier()
cl.addSample(Sample([2, 2, 2, 2, 2],-1))
cl.addSample(Sample([0, 0, 0],1))
cl.addSample(Sample([0, 0, 0, 0],-1))
p=cl.predictLabel(EuclideanSample([-1, -1, -1, -1 ,-1]))
print(p)  #should print 1

cl2=Classifier()
cl2.addSample(Sample([0, 0],["list","number",1]))
cl2.addSample(Sample([2.1, 5.2],["list","number",2]))
p=cl2.predictLabel(EuclideanSample([0, 3.3]))
print(p)  #should print ['list', 'number', 2]
p=cl2.predictLabel(TaxicabSample([0, 3.3]))
print(p)  #should print ['list', 'number', 1]

cl3=Classifier()
cl3.addSample(Sample([3, 1, 1],"a"))
cl3.addSample(Sample([2, 2, 2],"b"))
cl3.addSample(Sample([4, 0, 0],"c"))
p=cl3.predictLabel(EuclideanSample([0, 0, 0]))
print(p)  #should print a
p=cl3.predictLabel(TaxicabSample([0, 0, 0]))
print(p)  #should print c
p=cl3.predictLabel(MaximumSample([0, 0, 0]))
print(p)  #should print b
