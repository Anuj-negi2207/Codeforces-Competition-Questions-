"""
Two interns at HackerRank are teamed up to complete a total of n tasks. Each tas to be completed by either of the two interns. Both interns have their reward point defined, where the first intern gains reward_1[i] points for completing the ith task, 
while the second intern gains reward_2[i] points for completing the ith task. Since the interns work as a team, they wish to maximize the total reward points gained by both of them combined. Find the maximum combined reward points tha can be gained if the first intern has to complete k
tasks, and the second intern completes the remaining tasks. Note: The k tasks completed by the first intern could be any amongst the n tasks.
"""
def getMaximumRewardPoints(k, reward_1, reward_2):
    n = len(reward_1)
    arr_diff = [a - b for a,b in zip(reward_1,reward_2)]
    arr_index = list(range(0,n))
    
    arr_diff_ = [x for x,_ in sorted(zip(arr_diff,arr_index))]
    arr_index_ = [_ for x,_ in sorted(zip(arr_diff,arr_index))]
    
    arr_diff, arr_index = arr_diff_, arr_index_
    
    sum = 0
    for i in range(n):
        if i < n-k:
            sum += reward_2[arr_index[i]]
        else:
            sum += reward_1[arr_index[i]]
        
    return sum
    