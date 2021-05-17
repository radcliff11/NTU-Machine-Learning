#!/usr/bin/env python
# coding: utf-8

# In[1]:


h = 2
data = []
n = []
output = []
file = open('data.txt','r')
data = file.readlines()
file.close()
data = list(map(lambda s: s.strip(), data))
instance,dimension= data[0].split(',')
instance = int(instance)
dimension = int(dimension)
data.pop(0)
for x in range(len(data)):
    n.append(list(map(float,data[x].split(' ')))) # converst string to float and split

#single-dimension
#          #{x - (h/2) < xi <= x + (h/2)}
# p(x) = -----------------------------------
#                  instance * h   
# #multi-dimension
# #          #{x - (h/2) < xi <= x + (h/2)}    Note:(1 direction pov and xi is the cur point in dimension)
# # p(x) = -----------------------------------
# #                  instance * h^d
             
for row in range(len(n)):
    count = 0
    #print("cur instance:", n[row])
    #if one dimension of instance is wrong, put in list. at the end of comparisson for instance, correct ones counted
    wrong = []#list(range(0,instance))
    for row1 in range(len(n)):
        for col in range(dimension):
            left = n[row][col]-(h/2)
            right = n[row][col]+(h/2)
            #print(n[row][col],n[row1][col])
            #print(left,right)
            if(n[row1][col]>left and n[row1][col]<=right):   
                # print("correct : ", n[row1][col])
                next
                 
            else:
                 wrong.append(row1)
                 #print(wrong)
                 #print(n[row1][col])
    #print(wrong)
    calc = (instance - len(set(wrong)))/ (instance * (h**dimension))
    output.append(calc)
        #print(calc)        
#print(output)

#If file alr exists clear output
try:
    file = open("output.txt","r+")
    file.truncate(0)
    file.close()
#else if file dont exist create
except FileNotFoundError:
    file = open("output.txt","x")
    file.close()

for i in output:
    file =  open('output.txt', 'a') #as the_file:
    file.write(str(i))   #the_file.write(str(i))
    file.write("\n")
    file.close()
#output


# In[ ]:




