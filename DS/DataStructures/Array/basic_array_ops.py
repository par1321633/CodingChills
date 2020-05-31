#!/usr/bin/env python
# coding: utf-8

"""
Array Operations
ADD
ADD Item at any index - O(N) time complexity
Remove Item at Index
"""



numbers = [1,2,3,4]


print ("#3 rd index")
print (numbers[3])


print ("#first number")
print (numbers[0])


# In[4]:
print ("Update Index 1 element with Adam")
numbers[1] = 'Adam'
print (numbers)

# In[5]:

numbers[1]

# In[7]:


print ("#iterate over array")
for num in numbers:
    print (num)


# In[10]:

print ("Iterate over array with Index")
for i in range(len(numbers)):
    print (i, numbers[i])


# In[11]:


#first 2 elements
print ("Slicing Operation")

print (numbers[0:2])

# In[12]:


print ("# -ve index start from end, this will remove last element")
print (numbers[:-1])



# In[13]:
numbers[:-2]


# In[16]:

print (numbers)
print ("# Max , Iterate")
numbers[1] = 15
max_num = numbers[0]
for i in numbers[1:]:
    if i > max_num:
        max_num = i
print ("Max:",max_num)
#Linear Search Complex


# In[18]:


#Adding and Appending
print ("Append 30 at end")
numbers.append(30)
print (numbers)


# In[20]:


print ("#list.insert(<position, element), Insert 20 at index 1")
numbers.insert(1, 20)

# In[21]:


print (numbers)

# In[22]:


#extend - Add element of list2 at the end
numbers.extend([100,20,30])
print (numbers)

# In[26]:


numbers.extend({'1':'1','2':'2'})
numbers.extend({'1':1,'2':2})
#Only list,tuple or iterables can be passed
numbers


# In[27]:


sum(numbers)


# In[28]:


numbers.count(20)


# In[29]:


len(numbers)


# In[30]:


numbers.index(4)


# In[31]:


numbers.index(20)


# In[34]:


numbers.index(500)


# In[35]:


min(numbers)


# In[36]:


#Deletion of List Elements


# In[37]:

print (numbers.pop(-1))

# In[39]:

numbers.pop(-2)
print (numbers)

# In[40]:

print ("del numbers[-3:-1]")
del numbers[-3:-1]
print (numbers)


# In[41]:

print ("POP")
numbers.pop()
print (numbers)

print ("SUM")
sum(numbers)

