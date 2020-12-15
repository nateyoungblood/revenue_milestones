# We keep track of the revenue x makes every day, 
# and we want to know on what days x hits certain revenue milestones. 
# Given an array of the revenue on each day, and an array of milestones x wants to reach, 
# return an array containing the days on which x reached every milestone.

revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]

def cumul(rev):
    cumul=[]
    cumul.append(rev[0])
    for x in range(1,len(rev)):
        cumul.append(rev[x]+cumul[x-1])
    return(cumul)

def reached(rev,mil):
    cumulate=cumul(rev)
    output=[]
    for y in range(len(mil)):
        for x in range(0,len(cumulate)):
            if cumulate[x]>=mil[y]:
                output.append(x+1)
                break
#         output.append(milestones[y])
    print(output)

reached(revenues,milestones)