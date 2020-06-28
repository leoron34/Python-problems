Suppose we need to identify the no of gems in a box. We go to numerous persons and record their guesses and note it down. Now by using the concept of trimmed mean and comparing the mean and median, we get a result close to the actual result. This is crowd computing/ social computing. 
Quora, Wikipedia etc. sites uses this concept to show us result of a particular question

from scipy import stats
import matplotlib.pyplot as plt
import statistics
Estimates=[] #list of numbers or data
Estimates.sort() #Sorting the data 

#tv=int(0.1*len(Estimates))    # trimming 10% of the data
#Estimates=Estimates[tv:]      # deleting smallest 10% values
#Estimates=Estimates[:len(Estimates)-tv]     # deleting largest 10% values 

for i in range(len(Estimates)):
    print(Estimates[i])
a=stats.trimboth(Estimates,proportiontocut=0.1) 
print(a)
m=stats.trim_mean(Estimates,0.1) #proportion cut, cuts 10% of the data from start and end.
print(m)    

# We just need to show the list, for that we will be plotting it in the x axis and fixing Y as constant
y=[]
for i in range(len(a)):
    y.append(5)

plt.plot(a,y,'ro')
plt.plot([statistics.mean(a)],[5],'bo')
plt.plot([statistics.median(a)],[5],'go')     
plt.plot([#actual value],[5],'ro')     

# Comparing the results we get a number close to the actual number. 
