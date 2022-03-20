#!/usr/bin/env python
# coding: utf-8

# In[4]:


def union(a,b):
    a=set(a+b)
    return list(a)
union([1,2,3,4,5],[1,2,3])


# In[18]:


class Solution:
  
   def doUnion(self,a,n,b,m):
        a=set(a+b)
        return len(a)
    
if __name__=='__main__':
    
    #It's boilerplate code that proctects users from accidentally invoking the script when they did'nt intent to.
    #__name__ is a global variable and wokrs in a similar way to global
    #__main__ : like other programming language,python too has an execution entry point, i.e. __main___ is the name of the scope in which top-level code executes.
    #We use two ways to run a module in Python: 1) run it directly as a script or import it.
    t = int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        #we use split() to add comma after each element and strip for removing white/extra spaces
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.doUnion(a,n,b,m))
        
#driver code ends here





# In[14]:


print(__name__)

