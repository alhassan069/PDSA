# *PDSA WEEK 3 GRPA 1*


def DishPrepareOrder(order_list):
  menu=[1001,1002,1003,1004,1005,1006,1007,1008,1009]
  dic={}
  for i in menu:
    dic[i]=order_list.count(i)

  return SortDishes(menu,dic)
  
def SortDishes(L,d):
  n = len(L)
  if n < 1:
      return(L)
  for i in range(n):
      j = i
      while(j > 0 and d[L[j]] > d[L[j-1]]):
        (L[j],L[j-1]) = (L[j-1],L[j])
        j = j-1
#to remove dishes that have 0 orders
  for i in d:
    if d[i]==0:
      L.remove(i)

  return L





# *PDSA WEEK3 GRPA 2*

def eval(o,a,b) :
  if o == '+' :
    return str(float(a)+float(b))
  if o == '-' :
    return str(float(a)-float(b))
  if o == '*' :
    return str(float(a)*float(b))
  if o == '/' :
    return str(float(a)/float(b))
  if o == '**' :
    return str(float(a)**float(b))

def EvaluateExpression(exp) :
  op = ['+','-','*','/','**']
  stack = list()
  exp = exp + ' '
  i = 0
  while( i < len(exp)) :
    if exp[i] == ' ' :
      pass
    else :
      j = i
      while(exp[j] != ' ') :
        j += 1
      if exp[i:j] in op :
        b = stack.pop(0)
        a = stack.pop(0)
        c = eval(exp[i:j],a,b)
        stack.insert(0,c)
        i = j+1
      else:
        stack.insert(0,exp[i:j])
        i = j+1      
  return stack[0]








# *PDSA WEEK 3 GRPA 3*

def reverse(root):
    if root.value==None or root.next==None:
        return root
    newroot=reverse(root.next)
    root.next.next=root
    root.next=None
    
    return newroot








# **PDSA WEEK 4 GRPA 1 ***


class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return(str(self.queue))
        
def findConnectionLevel(n, Gmat, px, py):
  level={}
  parent={}
  for i in range(n):
    level[i]=0
    parent[i]=-1
  q=Queue()

  level[px]=0
  q.addq(px)

  while(not q.isempty()):
    j= q.delq()
    for k in range(n):
      if (level[k]==0 and Gmat[j][k]==1):
        level[k]=level[j]+1
        parent[k]=j
        q.addq(k)

  return (level[py])




# **PDSA WEEK 4 GRPA 2 ***

def findMasterTank(tanks, pipes):
  
  indegree={}
  l=[]
  for i in tanks:
    indegree[i]=0

  for j in pipes:
    indegree[j[1]]+=1
 
  for i in tanks:
    if indegree[i]==0:
      l.append(i)
  if len(l)==1:
      return(l[0])

  return 0


# **PDSA WEEK 4 GRPA 3 ***

class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return(str(self.queue))


def longJourney(AList):
  indegree={}
  lpath={}
  parent={}
  l=[]
  zerodegreeq = Queue()


  for u in AList.keys():
    (indegree[u],lpath[u],parent[u]) = (0,0,None)
    
  for u in AList.keys():
    for v in AList[u]:
      indegree[v] = indegree[v] + 1

  for u in AList.keys():
    if indegree[u] == 0:
      zerodegreeq.addq(u)
      parent[u]

  while (not zerodegreeq.isempty()):
    j = zerodegreeq.delq()
    indegree[j] = indegree[j]-1
    for k in AList[j]:
      parent[k]=j
      indegree[k] = indegree[k] - 1
      lpath[k] = max(lpath[k],lpath[j]+1)
      if indegree[k] == 0:
        zerodegreeq.addq(k)
  
             
  while not(k==None):
    l.append(k)
    k=parent[k]
  
  l.reverse()
  return (l)











# ***WEEK  5 GRPA1  ****

def FiberLink(WL):
    infinity = 1 + max([d for u in WL.keys() for (v,d) in WL[u]])
    (visited,distance,treeEdges) = ({},{},[])
    totalDist = 0
    for v in WL.keys():
        (visited[v],distance[v]) = (False, infinity)
    
    visited[0]= True
    for (v,d) in WL[0]:
        distance[v] = d
    
    for i in WL.keys():
        (mindist, nextv) = (infinity, None)
        for u in WL.keys():
            for (v,d) in WL[u]:
                if visited[u] and (not visited[v]) and d < mindist:
                    (mindist, nextv, nexte) = (d,v,(u,v))
        
        if nextv is None:
            break
        totalDist += mindist
        visited[nextv] = True
        treeEdges.append(nexte)
        
        for (v,d) in WL[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v], d)
    return totalDist




# ***WEEK  5 GRPA 2 ****


def path(prev, s, t):
    p = []
    dest = s
    while dest != t:
        p += [dest]
        dest = min([j for i,j in prev.items() if i == dest])
    return p

def min_cost_walk(WList, s, e, t):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()
                           for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)
        
    distance[t] = 0
    prev = {}
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys()
                        if not visited[v]])
        nextvlist = [v for v in WList.keys()
                        if (not visited[v]) and
                            distance[v] == nextd]

        if visited[s] and visited[e]:
            break
            
        nextv = min(nextvlist)
        visited[nextv] = True        
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],distance[nextv]+d)
                if distance[v] == distance [nextv] + d:
                    prev[v] = nextv
    
    return(distance[s] + distance [e], path(prev, s, t) +[t]+ path(prev,e,t)[::-1])
    




# Week 5 Grpa 3

def IsNegativeWeightCyclePresent(WList):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
        
    distance[0] = 0
    for i in range(len(WList.keys()) + 3):
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v] = min(distance[v], distance[u] + d)
        
    for u in WList.keys():
        for (v,d) in WList[u]:
            if distance[v] > distance[u] + d:
                return True
    return False


size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))





# week 6 grpa 1
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

def mergeKLists(listy):
    superListy=list()
    for l in listy:
        superListy.extend(l)
    quickSort(superListy,0,len(superListy)-1)
    return superListy





# week6 grpa 2 
# 3 test cases passed
def maxLessThan(root, k):
    if root.value == k:
        return root.value
    if root.isleaf():
        if root.value < k:
            return root.value
        else:
            return None
            
    if root.value > k:
        if root.left.isempty():
            return None
        return maxLessThan(root.left, k)
    else:
        if root.right.isempty():
            return root.value
        if root.right.value > k:
            return root.value
        return maxLessThan(root.right, k)

# 5 all cases passed
def maxLessThan(root, K):
    current = root
    max_val = None
    
    while not current.isempty():
        if current.value <= K:
            max_val = current.value
            current = current.right
        else:
            current = current.left
            
    return max_val




# week 6 grpa 3
def MaxHeapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, n)
 
def min_max(arr):
    n = len(arr)
    for i in range(int((n - 2) / 2), -1, -1):
        MaxHeapify(arr, i, n)







# GrPA 1 wk 7 PDSA

def height(self):
    if self.isempty():
        return(0)
    else:
        return 1 + max(self.left.height(), self.right.height())

def update_height(self):
 self.height = 1 + max(self.left.height, self.right.height)

def slope(self):
 return self.left.height - self.right.height
   
def rebalance(self):
    if self.slope() in (-1, 0, 1):
        return
        
    elif self.slope() >= 2:
        if self.left.slope() < 0:
            self.rightrotate()
            self.right.update_height()
            self.update_height()
            
            self.right.rightrotate()
            self.right.right.update_height()
            self.right.update_height()
            self.update_height()
            
            self.leftrotate()
            self.left.update_height()
            self.update_height()
            
        else:
            self.rightrotate()
            self.update_height()
            
    elif self.slope() <= 2:
        if self.right.slope() > 0:
            self.leftrotate()
            self.left.update_height()
            self.update_height()
            
            self.left.leftrotate()
            self.left.left.update_height()
            self.left.update_height()
            
            self.rightrotate()
            self.right.update_height()
            self.update_height()
            
        else:
            self.leftrotate()
            self.update_height()

def insert(self,v):
    if self.isempty():
        self.value = v
        self.left = AVLTree()
        self.right = AVLTree()
        self.update_height()
        
    if v < self.value:
        self.left.insert(v)
        self.update_height()
        self.rebalance()
        
    if v > self.value:
        self.right.insert(v)
        self.update_height()
        self.rebalance()





# GrPA 2 wk 7 PDSA

def minimum_platform(train_schedule):
    max_plt_no = 0
    for i in range(len(train_schedule)):
        plt_no = 1
        for j in range(len(train_schedule[:i])):
            if train_schedule[i][1] < train_schedule[j][2]:
                plt_no += 1
        if plt_no > max_plt_no:
            max_plt_no = plt_no
    return max_plt_no 





#  GrPA 3 wk 7 PDSA 

def no_overlap(L):
    L.sort(key=lambda x:x[2])
    applications_accepted = [L[0]]
    rem_applications = L[1:]
    for appl in rem_applications:
        last_accepted = applications_accepted[-1]
        if appl[1] > last_accepted[2]:
            applications_accepted.append(appl)
    customers_accepted = [a[0] for a in applications_accepted]
    return customers_accepted






# week8 grpa 1

def first(arr, x, n):
    low = 0
    high = n - 1
    res = None
     
    while (low <= high):
         
        mid = (low + high) // 2
         
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
             
        # If arr[mid] is same as x, we
        # update res and move to the left
        # half.
        else:
            res = mid
            high = mid - 1
 
    return res
 
def last(arr, x, n):
     
    low = 0
    high = n - 1
    res = None
     
    while(low <= high):
         
        # Normal Binary Search Logic
        mid = (low + high) // 2
         
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
             
        # If arr[mid] is same as x, we
        # update res and move to the Right
        # half.
        else:
            res = mid
            low = mid + 1
 
    return res
    
def findOccOf(L, x):
    try:
        return (L.index(x), len(L)-1-L[::-1].index(x))
    except Exception:
        return (None, None)







# **WEEK 8 GRPA 2***

def mergeAndCount(A,B):
    m, n = len(A), len(B)
    C, i, j, k, count = [], 0, 0, 0, 0
    while k < m+n:
        if i == m:
            C.append(B[j])
            j, k = j+1, k+1
        elif j == n:
            C.append(A[i])
            i, k = i+1, k+1
        elif A[i] < B[j]:
            C.append(A[i])
            i, k = i+1, k+1
        else:
            C.append(B[j])
            j, k, count = j+1, k+1, count+(m-i)
    return C, count

def sortAndCount(A):
    n = len(A)

    if n <= 1:
        return A, 0

    L, countL = sortAndCount(A[:n//2])
    R, countR = sortAndCount(A[n//2:])

    B, countB = mergeAndCount(L, R)

    return B, countL+countR+countB

def countIntersection(x1, x2):
    z = list(zip(x1, x2))
    z.sort()
    A = [i[1] for i in z]
    L, ans = sortAndCount(A)
    return ans







# **WEEK 8 GRPA 3***

def Brute_ClosestPair(P):
    dists = []
    for i in P:
        for j in P:
            if i != j:
                x1, y1 = i
                x2, y2 = j
                d = ((x2-x1)**2 + (y2-y1)**2)**0.5
                dists.append((i, j, d))
    dists.sort(key=lambda x: x[2])
    return dists[0]

def ClosestPair(Px, Py):
    if len(Px) <= 3:
        return Brute_ClosestPair(Px)
    
    Qx, Rx = Px[:len(Px)//2], Px[len(Px)//2:]
    Qy, Ry = [], []
    xR = min(Rx)[0]
    for i in Py:
        if i[0] < xR:
            Qy.append(i)
        else:
            Ry.append(i)
    
    q1, q2, dQ = ClosestPair(Qx, Qy)
    r1, r2, dR = ClosestPair(Rx, Ry)

    delta = min(dQ, dR)
    Sy = []
    for i in Qy:
        if xR - i[0] <= delta:
            Sy.append(i)
    for j in Ry:
        if j[0] - xR <= delta:
            Sy.append(j)
    Sy.sort()
    dS = delta

    S = []
    c = 1
    for s1 in Sy:
        if c < len(Sy):
            for s2 in Sy[c:c+16]:
                x1, y1 = s1
                x2, y2 = s2
                d = ((x2-x1)**2 + (y2-y1)**2)**0.5
                if d < delta:
                    dS = d
                    S.append((s1, s2, dS))
        c += 1

    if S != []:
        S.sort()
        return S[0]
    else:
        final = [(q1, q2, dQ), (r1, r2, dR)]
        final.sort(key=lambda x: x[2])
        return final[0]

def minDistance(Points):
    Px = sorted(Points)
    Py = sorted(Points, key=lambda x: x[1])

    closest_pair_and_distance = ClosestPair(Px, Py)
    return round(closest_pair_and_distance[2], 2)







# **WEEK 8 GRPA 4***


def MoM7(arr):
    if len(arr) <= 7:
        arr.sort()
        return arr[len(arr)//2]

    M = []
    for i in range(0, len(arr), 7):
        X = arr[i:i+7]
        X.sort()
        M.append(X[len(X)//2])

    return MoM7(M)

def MoM7Pos(arr):
    median = MoM7(arr)
    less_than_median_dict = {}
    for i in arr:
        if i < median:
            less_than_median_dict[i] = less_than_median_dict.get(i, 0) + 1
    return sum(less_than_median_dict.values())












# ****WEEK 9****

# GRPA 1:
words = []


def constructWord(word: str, subs, temp = []):
    if word == "":
        words.append(temp)
        return [[]]

    for i in subs:
        if word.startswith(i):
            #print(word, i)
            copy = temp.copy()
            copy.append(i)
            x = constructWord(word.replace(i, ""), subs, temp=copy)
            if not x and len(x) > len(subs):
                #print(x, temp)
                words.append(x)
    return words




# GRPA2:

memo = None
def MaxCoinPath(M, x1, y1, x2, y2):
    global memo
    if memo is None:
        memo = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    if x2 == x1 and y2 == y1:
        return M[x1][y1]
    if x2 < 0 or y2 < 0:
        return 0
    #print(x2,y2)
    mx = max(MaxCoinPath(M, x1, y1, x2 - 1, y2), MaxCoinPath(M, x1, y1, x2, y2 - 1))
    #print("mx:",mx)
    memo[x2][y2] = mx+M[x2][y2] if mx > memo[x2][y2] else memo[x2][y2]

    return memo[x2][y2]




# GRPA3:

def LDS(L):
    if not L:
        return
    LDS = [[] for _ in range(len(L))]
    LDS[0].append(L[0])
    for i in range(1, len(L)):
        for j in range(i):
            if L[j] > L[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j].copy()
        LDS[i].append(L[i])
    j = 0
    for i in range(len(L)):
        if len(LDS[j]) < len(LDS[i]):
            j = i

    return LDS[j]













# **** PDSA WEEK 10 ****

 
# grpa 1

def findContinuousRepetitions(t, p):
    last = {}
    for i in range(len(p)):
        last[p[i]] = i
        
    goldFlag = False
    goldCount = 0
    goldtemp = 0
        
    poslist, i = [], 0
    while i <= (len(t) - len(p)):
        matched, j = True, len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j -= 1
        if matched:
            
            goldFlag = True
            poslist.append(i)
            if goldFlag:
                goldtemp += 1
                if goldtemp>goldCount:
                    goldCount = goldtemp
            i += len(p)
        else:
            goldFlag = False
            goldtemp = 0
            j += 1
            if t[i+j] in last.keys():
                i += max(j-last[t[i+j]], 1)
            else:
                i += j + 1
    return(goldCount)







# grpa 2

def stringmatch(t, p):
    poslist = []
    for i in range(len(t) - len(p) + 1):
        matched = True
        j = 0
        while j < len(p) and matched:
            if t[i+j] != p[j] and p[j] != "$":
                matched = False
            j += 1
        if matched:
            poslist.append((i, t[i:i+len(p)]))
    return(poslist)
    
def stringmatchrev(t, p):
    poslist = []
    for i in range(len(t) - len(p) + 1):
        matched = True
        j = len(p) - 1
        while j >= 0 and matched:
            if t[i+j] != p[j] and p[j] != "$":
                matched = False
            j -= 1
        if matched:
            poslist.append((i, t[i:i+len(p)]))
    return(poslist)
    
def FindPattern(t,p):
    if p[0] == "$":
        return stringmatch(t, p)
    else:
        return stringmatchrev(t, p)







# grpa 3

def isPalindrome(s):
       
    #to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
     
    # if length is less than 2
    if l < 2:
        return True
 
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
        
        # Call is pallindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
 
    else:
        return False

def MakePalindrome(s):
    if isPalindrome(s):
        return None
    else:
        p = s
        t = ""
        i = -1
        while not isPalindrome(p):
            p = s
            t += p[i]
            p = t + p
            i -= 1
        return t







