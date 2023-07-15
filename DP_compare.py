import numpy as np
import csv
import random

# laplaceMechanism(img, length, width, epsilon)
# epsilon
#   The privacy budget of the laplace Mechanism.
#   The smaller the value is, the better privacy protection.
def laplaceMechanism(num, n,max, epsilon=1):
    # Generate laplace noise mask
    dp_noise = np.random.laplace(0, 1.0/epsilon, n).round() % max # round
    num_out = (num + dp_noise) % max # round
    # Reshape to origin form
    return num_out

with open('DPcompare.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['cases', 'sorted', 'unsort', 'sorted extra', 'unsort extra'])
    max_data=[1023,2047]
    ep=[1,0.1,0.05,0.02,0.01]
    case_num=3000
    # parameter setting
    for a in range(0,2):
        min = 0
        max = max_data[a]
        num = []
        num_id=range(0,case_num)
        for i in range(0,case_num):
            n = random.randint(min,max)
            num.append(n)
        bnum=[]
        for x in num:
            bnum.append(x)
        list_ref=[]
        buf=sorted(num, key=int, reverse=False)
        for x in buf:
            if x in num:
                list_ref.append(num_id[num.index(x)])
                num[num.index(x)]=-1
        for b in ep:
            epsilon=b # epsilon 1 -> 0.1 -> 0.05 -> 0.02 -> 0.01
            # Check original data
            #print(num)
            num_out = laplaceMechanism(buf, case_num, max, epsilon)
            num_out.sort()
            num_ans=[]
            for i in range(0,case_num):
                num_ans.append(num_out[list_ref.index(i)])
            # Check sorted DP data
            #print(num_ans)
            # Count score
            n1=0
            n1ex=0
            for i in range(0,case_num):
                n1+=abs(num_ans[i]-bnum[i])
                if abs(num_ans[i]-bnum[i])>(max-min)/2:
                    n1ex+=abs(num_ans[i]-bnum[i])
            num_out = laplaceMechanism(bnum, case_num, max, epsilon)
            # Check unsort DP data
            #print(num_out)
            # Count score
            n2=0
            n2ex=0
            for i in range(0,case_num):
                n2+=abs(num_out[i]-bnum[i])
                if abs(num_out[i]-bnum[i])>(max-min)/2:
                    n2ex+=abs(num_out[i]-bnum[i])
            # Check scores
            caseStr=''
            if a == 1:
                caseStr+='Double range, '
            caseStr+='epsilon = '+str(b)
            print(caseStr)
            print('DP with sort: ',n1, ', Because of over flow: ', n1ex)
            print('DP without sort: ',n2, ', Because of over flow: ', n2ex)
            writer.writerow([caseStr, n1, n2, n1ex, n2ex])