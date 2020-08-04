import time
start_time = time.time()

import gzip
import json
import numpy as np

from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



#######This code is to determine the optimum number of clusters for Gender, Race, and Age Datasets#######


def clustering (dataset):
	#dataset: dictionary of stats
	df = DataFrame(dataset, columns=dataset.keys())
	df = df.T
	
	Sum_of_squared_distances = []
	K = range(1,15)
	for k in K:
		km = KMeans(n_clusters=k)
		km = km.fit(df)
		Sum_of_squared_distances.append(km.inertia_)

	plt.plot(K, Sum_of_squared_distances, 'bx-')
	plt.xlabel('k')
	plt.ylabel('Sum_of_squared_distances')
	#plt.title('Elbow Method For Optimal k for Gender Data')
	#plt.title('Elbow Method For Optimal k for Race Data')
	plt.title('Elbow Method For Optimal k for Age Data')

	print("Elapsed Time")
	print("--- %s seconds ---" % (time.time() - start_time))
	
	plt.show()


path_gender = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Percentage_Demographics/Gender_Percentage_User_Demographics.gz"
path_race = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Percentage_Demographics/Race_Percentage_User_Demographics.gz"
path_age = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Percentage_Demographics/Age_Percentage_User_Demographics.gz"




#Loading dictionaries of Promoter percentage Gender
with gzip.open(path_gender,'rt') as T1:
	demo_gender_temp = T1.read()
T1.close()

stats_gender = json.loads(demo_gender_temp)

#Loading dictionaries of Promoter percentage Race
with gzip.open(path_race,'rt') as T2:
	demo_race_temp = T2.read()
T2.close()

stats_race = json.loads(demo_race_temp)

#Loading dictionaries of Promoter percentage Age
with gzip.open(path_age,'rt') as T3:
	demo_age_temp = T3.read()
T3.close()

stats_age = json.loads(demo_age_temp)

dataset_g = stats_gender

dataset_r = stats_race

dataset_a = stats_age

#clustering (dataset_g)
#clustering (dataset_r)
clustering (dataset_a)


