import json
import numpy as np
import matplotlib.pyplot as plt 


with open("datainh2.txt","r") as file:
    data = json.load(file)
    score = data["score"]
    reward = data["reward"]
    time = data["saving_time"]
my_max = np.max(score,axis=0)[0]
score = score[-50:]

print("last 50 matches mean_my_score and my_max:", np.mean(score, axis=0)[0], my_max)

plt.figure()
plt.plot(time,reward)
plt.xlabel("time")
plt.ylabel("reward")
plt.show()
