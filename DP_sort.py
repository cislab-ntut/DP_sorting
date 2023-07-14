import numpy as np
import csv
import random

# laplaceMechanism(img, length, width, epsilon)
# epsilon
#   The privacy budget of the laplace Mechanism.
#   The smaller the value is, the better privacy protection.
def laplaceMechanism(num, n,max, epsilon=1):
    # Generate laplace noise mask
    dp_noise = np.random.laplace(0, 1.0/epsilon, n).round() % max # round # mod 256
    num_out = (num + dp_noise) % max # round
    # Reshape to origin form
    return num_out

# parameter setting
min = 0
max = 1023
case_num=3000
epsilon=0.05 # epsilon 1 -> 0.1 -> 0.05 -> 0.02 -> 0.01
num = []
num_id=range(0,case_num)
for i in range(0,case_num):
    n = random.randint(min,max)
    num.append(n)
# Check original data
#print(num)
bnum=[]
for x in num:
    bnum.append(x)
list_ref=[]
buf=sorted(num, key=int, reverse=False)
for x in buf:
    if x in num:
        list_ref.append(num_id[num.index(x)])
        num[num.index(x)]=-1
num_out = laplaceMechanism(buf, case_num, max, epsilon)
num_out.sort()
num_ans=[]
for i in range(0,case_num):
    num_ans.append(num_out[list_ref.index(i)])
# Check sorted DP data
#print(num_ans)
# Count score
n1=0
for i in range(0,case_num):
    n1+=abs(num_ans[i]-bnum[i])
num_out = laplaceMechanism(bnum, case_num, max, epsilon)
# Check unsort DP data
#print(num_out)
# Count score
n2=0
for i in range(0,case_num):
    n2+=abs(num_out[i]-bnum[i])
# Check scores
print('DP with sort: ',n1)
print('DP without sort: ',n2)
with open('NPoutput.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(bnum)
    writer.writerow(num_ans)
    writer.writerow(num_out)