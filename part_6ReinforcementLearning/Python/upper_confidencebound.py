# Upper Confidence Bound (UCB)
import math

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset_path="../../Datasets/Ads_CTR_Optimisation.csv"
dataset = pd.read_csv(dataset_path)
print(dataset)

# Implementing UCB
# N=10000
N=50
d=10

ads_selected=[]
number_of_selection=[0]*d
sums_of_rewards=[0]*d
total_reward=0

for n in range(0,N):
    ad=0
    max_upper_bound=0
    for i in range(0,d):
        if number_of_selection[i] >0:
            average_reward=sums_of_rewards[i]/number_of_selection[i]
            delta_i = math.sqrt(3/2*math.log(n+1)/number_of_selection[i])
            upper_bound=average_reward+delta_i
        else:
            upper_bound=1e400
        if upper_bound>max_upper_bound:
            max_upper_bound=upper_bound
            ad=i

    ads_selected.append(ad)
    number_of_selection[ad]+=1
    reward=dataset.values[n,ad]
    sums_of_rewards[ad]+=reward
    total_reward+=reward


# visualsing the result
plt.hist(ads_selected)
plt.title('Histogram of ad selections')
plt.xlabel('Ads')
plt.ylabel('Number of time each ad was selected')
plt.show()




