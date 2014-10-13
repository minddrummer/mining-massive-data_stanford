import pandas as pd
import numpy as np



def page_rank(connect_M, epi, belta,r_0, total_pagerank):
    '''
    page rank algorithm works for the graph network with both dead ends and also the spider traps
    '''
    rt0 =  r_0    
    running =  True  
    #record the updating times
    t = 1
    while running:    
        rt1 =np.zeros(connect_M.shape[0], dtype = np.float_)
        
        
        for j in range(rt1.shape[0]):
            r_t_j = rt1[j]
            for i in range(rt1.shape[0]):
                r_t_1_i = rt0[i]
                d_i = connect_M[j][i]
                if d_i != 0:
                    r_t_j = r_t_1_i * d_i + r_t_j
            
            rt1[j] = r_t_j
        
        rt1 = rt1 * belta
        
        #re-insert the leaker pagerank--for both the dead end part and also for the 1-belta part
        S = sum(rt1)
        rt1 = rt1 + (total_pagerank-S)/rt1.shape[0]
        
        if sum(abs(rt1 - rt0)) < epi:
            running = False
        
        #check the values of rt1 after each iteration    
        if t <= 5:
            print rt1
        #assign the updated rt1 to rt0 again
        rt0 = rt1
        # and finish the t-th times
        t += 1

    return rt0
    
#q1
#connect_M = np.array([[0,0,0],[0.5,0,0],[0.5,1,1]])
#q2
connect_M = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
epi = 0.0001
belta = 0.85
len_r = connect_M.shape[0]
r_0_lst = []
total_pagerank = 1.0
for i in range(len_r):
    r_0_lst.append(total_pagerank/len_r)
r_0 = np.array(r_0_lst)

pgrk = page_rank(connect_M, epi, belta,r_0, total_pagerank)

print pgrk[1]*0.85
print pgrk[0]*.575+ pgrk[2]*.15

print pgrk[0]
print pgrk[2]*.9+ pgrk[1]*.05

print pgrk[0]*0.95
print pgrk[2]*.9+ pgrk[1]*.05

print pgrk[2]*0.85
print pgrk[0]*.575+ pgrk[1]

#q3
connect_M = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
epi = 0.0001
belta = 1
len_r = connect_M.shape[0]
r_0_lst = []
total_pagerank = 3.0
for i in range(len_r):
    r_0_lst.append(total_pagerank/len_r)
r_0 = np.array(r_0_lst)

pgrk = page_rank(connect_M, epi, belta,r_0, total_pagerank)
print pgrk








