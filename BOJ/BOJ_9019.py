import sys
import collections
import itertools
import copy
import heapq


sys.stdin = open("input.txt", "r")
input=sys.stdin.readline
sys.setrecursionlimit(15000)

def D(s0) :
    nx = 2*s0
    if nx <=9999:
        return nx 
    else :
        return nx%10000
    

def S(s0) :
    if s0 == 0 :
        return 9999
    else :
        return s0 -1

def L(x) :
    return 10 * (x - int(x / 1000) * 1000) + int(x / 1000)


def R(x) :
    return 1000*(x - 10*int(x/10)) + int(x/10)


Total = int(input())



for _ in range(Total):
    A, B = map(int, input().split())
    
    Q = collections.deque([])
    Q.append([A,""])
    
    
    
    visit = [False]*10000 
    visit[A]=True         
    '''
    visit를 만들어서 Q의 개수를 안늘리는게 
    메모리 초과가 안나는 비결이다 
    BFS는 visit를 만들었을떄 선형시간이다 라고한다.
    '''
    while Q:               
        num_ , log_ = Q.popleft()
        
        if num_ == B :
            print(log_)
            break
        
            
        new_num = D(num_)
        if visit[new_num]==False:
            Q.append([new_num,log_+"D"])
            visit[new_num] = True
        new_num = S(num_)
        if visit[new_num]==False:
            Q.append([new_num,log_+"S"])
            visit[new_num] = True
        new_num = L(num_)
        if visit[new_num]==False:
            Q.append([new_num,log_+"L"])
            visit[new_num] = True
        new_num = R(num_)
        if visit[new_num]==False:
            Q.append([new_num,log_+"R"])
            visit[new_num] = True

    

