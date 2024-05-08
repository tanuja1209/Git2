#!/usr/bin/env python
# coding: utf-8

# In[1]:


def n_tsp(dist):
    n=len(dist)
    opt_cost=float('inf')
    opt_tour=[]

    for start in range(n):
        unvisited=set(range(n))
        curr_city=start
        tour=[curr_city]
        total_cost=0
        unvisited.remove(start)
        
        while unvisited:
            nearest_city=min(unvisited,key=lambda city:dist[curr_city][city])
            total_cost+=dist[curr_city][nearest_city]
            tour.append(nearest_city)
            unvisited.remove(nearest_city)
            curr_city=nearest_city
            
        total_cost+=dist[curr_city][start]
        tour.append(start)

        if total_cost<opt_cost:
            opt_cost=total_cost
            opt_tour=tour
    
       
              
    print("total cost:",opt_cost)
    print("Optimal tour:",opt_tour)


if __name__=="__main__":
    num_cities=int(input("Enter number of cities:"))
    print("Enter matrix:")

    distance=[]
    for _ in range(num_cities):
        row=list(map(int,input().split()))
        distance.append(row)
    
n_tsp(distance)


# In[ ]:




