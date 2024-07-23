# lab6q1 24283699

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import numpy as np
import matplotlib.pyplot as plt



count = 0
size = []
identity = []
pielist1 = []
pielist2 = []

infile = open("input.txt", "r")

for line in infile:
    sequence = line.strip('\n')
    print ("Sequence: ", sequence[0:20], "Length: ", len(sequence))
    count = count + 1
    file_name = "dna_lab6_{}.xml".format(count)
    
    try:
        infile = open(file_name, "r")
        print ("Using saved file")
        
    except:
        print("Performing online BLAST search")
        handle = NCBIWWW.qblast("blastn", "nt", sequence)
        result = handle.read()
        outfile = open(file_name, "w")
        outfile.write(result)
        #Close blast request
        outfile.close()
        handle.close()
        infile = open(file_name, "r")  
        
    blast_record = NCBIXML.parse(infile)
    for record in blast_record:
        size.append(record.alignments[0].length)
        #identity.append(record.alignments[0].title)
        if("Drosophila melanogaster" in record.alignments[0].title):
            identity.append(0)
            pielist1.append(0)
        else:
            identity.append(1)
            pielist2.append(1)
        
infile.close()
print(identity)
print(size)

##########################################################
num_bins = 50
n, bins, patches = plt.hist(size, num_bins, normed = False, alpha = 0.5, color = 'g')
plt.xlabel("Sequence Length")
plt.ylabel("Count")
plt.title("Histogram")
plt.show()
######################################################### 
# PIE CHART
labels = 'Drosophila melanogaster', 'Vitis vinifera'
sizes = [len(pielist1), len(pielist2)]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
#########################################################
bar_width = .35
data2 = []
data2.append(sum(identity))
data2.append(count - sum(identity))
index = np.arange(1)
opacity = .45
error_config = {'ecolor': '0.3'}
rects1 = plt.bar(index, [sum(identity)], bar_width, alpha=opacity,color='b', yerr=None, error_kw=error_config,label='Vitis vinifera')
rects2 = plt.bar(index + bar_width, [count - sum(identity)], bar_width,alpha=opacity, color='r', yerr=None, label='Drosophila melanogaster')
plt.xlabel('Organism')
plt.ylabel('Count')
plt.title('Vitis vinifera versus Drosophila melanogaster')
plt.xticks(index + bar_width)
plt.legend()
plt.tight_layout()
plt.show()
#########################################################

import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans,vq
import random as rnd

# data generation
data = []
for i in range(0,10):
    data.append([rnd.random(), rnd.random()])

# Perform k-means clustering
numclusters = 2
centroids,_ = kmeans(data,numclusters)
idx,_ = vq(data,centroids)

# Move data into individual lists based on clustering
clusters = []
for i in range(0, numclusters):
    clusters.append([[],[]])

for i in range(0,len(idx)):
    clusterIdx = idx[i]
    clusters[clusterIdx][0].append(data[i][0])
    clusters[clusterIdx][1].append(data[i][1])    

# Plot data points and cluster centroids
plt.plot(clusters[0][0],clusters[0][1],'ob',
     clusters[1][0],clusters[1][1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()