import json
import numpy as np

with open("datainh.txt","r") as file:
    data = json.load(file)
    score = data["score"]
my_max = np.max(score,axis=0)[0]
score = score[-50:]

print("last 50 matches mean_my_score and my_max:", np.mean(score, axis=0)[0], my_max)
