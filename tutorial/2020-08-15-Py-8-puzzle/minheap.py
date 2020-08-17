# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:22:21 2020

@author: Think
"""

class MinHeapNode:
    
    def __init__(self, heapPos, priority, data):
        self.heapPos = heapPos
        self.priority = priority
        self.data = data
    
    def __repr__(self):
        return "(hpos: {0}, priority: {1}, data: {2})".format(self.heapPos,self.priority,self.data)
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    # def __le__（self, other):
    #     return self.priority <= other.priority

    # def __ge__（self, other):
    #     return self.priority >= other.priority

    # def __eq__(self, other):
    #     return self.priority == other.priority
    
    # def __ne__(self, other):
    #     return self.priority != other.priority

class MinHeap:
    
    def __init__(self, maxSize = None):
        if maxSize is not None:
            self.heap = [None] * (maxSize+1)
        else:
            self.heap = [None]
        self.len = 1
    
    def push(self, priority, data):
        '''
        把用户数据 data 按照优先级 priority 插入 Min Heap 中，返回 HeapNode

        Parameters
        ----------
        priority : TYPE
            DESCRIPTION.
        data : TYPE
            DESCRIPTION.

        Returns
        -------
        hn : TYPE
            DESCRIPTION.

        '''
        if self.len == len(self.heap):
            self.heap.append(None)
        hn = MinHeapNode(self.len,priority,data)
        self.heap[self.len] = hn
        self.len += 1
        self._bubleUp(self.len-1)
        return hn
    
    def pop(self):
        '''
        把优先级最高 (priority数值最小的) HeapNode 从 Min Heap 中删除并返回
        删除了的 HeapNode 它的 heapPos 设为 0
        Raises
        ------
        RuntimeError
            DESCRIPTION.

        Returns
        -------
        hn : TYPE
            DESCRIPTION.

        '''
        if self.len == 1:
            raise RuntimeError("MinHeap empty")
        
        hn = self.heap[1]
        hn.heapPos = 0
        self.len -= 1
        self.heap[1] = self.heap[self.len]
        self.heap[1].heapPos = 1
        self._bubleDown(1)
        return hn
    
    def updatePriority(self, hn, newPriority):
        '''
        把一个 HeapNode 的优先级更新

        Parameters
        ----------
        hn : TYPE
            DESCRIPTION.
        newPriority : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if (hn.heapPos < 1) or (hn.heapPos >= self.len):
            raise RuntimeError("hn.heapPos: {0} is not in the heap".format(hn.heapPos))
            
        if newPriority < hn.priority:
            hn.priority = newPriority
            self._bubleUp(hn.heapPos)
        elif newPriority > hn.priority:
            hn.priority = newPriority
            self._bubleDown(hn.heapPos)
            
    
    def _bubleUp(self, current):
        parent=int(current/2)
        while parent > 0 and self.heap[parent]>self.heap[current]:
            self.heap[parent],self.heap[current]=self.heap[current],self.heap[parent]
            self.heap[parent].heapPos = parent
            self.heap[current].heapPos = current
            current=parent
            parent=int(parent/2)
    
    def _bubleDown(self, current):
        # print("==== bubleDown, current: ",current," self.len: ",self.len)
        lastFullChildren = int((self.len-2) / 2)
        while current <= lastFullChildren:
            child1=current*2
            child2=(current*2)+1
            
            if self.heap[current] > self.heap[child1] or self.heap[current] > self.heap[child2]:
                # find smaller of two children
                if self.heap[child1] > self.heap[child2]:
                    minIdx = child2
                else:
                    minIdx = child1
                
                # print("   p:{0}, c1:{1}, c2:{2}, minIdx:{3}, lastFull:{4}".format(current,child1,child2,minIdx,lastFullChildren))
                # print("***",self)
                    
                self.heap[current],self.heap[minIdx]=self.heap[minIdx],self.heap[current]
                self.heap[current].heapPos = current
                self.heap[minIdx].heapPos = minIdx
                current = minIdx
                # print("---",self,"current: ",current,"self.len: ",self.len)
            else:
                break
        
        # if current node has only one child
        child1=current*2 
        if child1==self.len-1  and self.heap[current] > self.heap[child1]:
            # print("   p:{0}, c1:{1}".format(current,child1))
            
            self.heap[current],self.heap[child1]=self.heap[child1],self.heap[current]
            self.heap[current].heapPos = current
            self.heap[child1].heapPos = child1
            
    def __len__(self):
        return self.len - 1

    def __repr__(self):
        return str(self.heap[1:self.len])
    

class PQue:    
    '''
    一个优先队列，用数组 priorities[i] 记录第 i 个元素的优先级
    popMinIdx（） 找到优先级最高（priority数值最小的)元素的下标，并把这个元素标记为离开队列
    updatePriority(idx, newPriority) 把第 idx 个元素对应的优先级更新
    push(newPriority) 在数组最后加入一个元素，它的优先级别设为 newPriority
    idInQue(idx) 检查第 idx 个元素是否还在队列里面
    '''
    def __init__(self, priorities):
        self.heapNodes = [None] * len(priorities)
        self.heap = MinHeap(maxSize=len(priorities))
        for i,p in enumerate(priorities):
            hn = self.heap.push(p, i)
            self.heapNodes[i] = hn
                
    def popMinIdx(self):
        hn = self.heap.pop()
        return hn.data
    
    def push(self, newPriority):
        idx = len(self.heapNodes)
        hn = self.heap.push(newPriority, idx)
        self.heapNodes.append(hn)
    
    def isInQue(self, idx):
        if (0 <= idx) and (idx < len(self.heapNodes)):
            return self.heapNodes[idx].heapPos > 0
        return False
    
    def updatePriority(self, idx, newPriority):
        # print("hnodes, ",self.heapNodes)
        
        if not self.isInQue(idx):
            raise RuntimeError("idx: {0} is not in que".format(idx))
        hn = self.heapNodes[idx]

        # print("idx:{0} hn:{1}".format(idx,hn))
        # print("heap ",self.heap)

        self.heap.updatePriority(hn, newPriority)

        # print("after heap ",self.heap)


import unittest

class TestMinHeap(unittest.TestCase):
    def heapSort(a):
        h = MinHeap()
        for x in a:
            hn = h.push(x, "n"+str(x))
#            print(h)
        b = []
        for i in range(len(a)):
            hn = h.pop()
            b.append(hn.priority)
#            print("{0}: {1}".format(i,hn))
#            print(h)
        return b
        
    def test_heapSort01(self):
        a = [5,4,1,2,3]
        b = TestMinHeap.heapSort(a)
        self.assertEqual(b,[1,2,3,4,5])

    def test_heapSort02(self):
        a = [5,4,1,8,3,6,7,2]
        b = TestMinHeap.heapSort(a)
        self.assertEqual(b,[1,2,3,4,5,6,7,8])
    
    def test_PQue01(self):
        PW = [0.5, 0.4, 0.1, 0.6]
        pq = PQue(PW)
        a = []
        for i in range(len(PW)):
            minIdx = pq.popMinIdx()
            a.append(minIdx)
        self.assertEqual(a, [2,1,0,3])
    
    def test_PQue02(self):
        PW = [0.5, 0.4, 0.1, 0.6]
        pq = PQue(PW)
        minIdx = pq.popMinIdx()
        self.assertEqual(minIdx, 2)
        pq.updatePriority(1, 0.7)   # [0.5, 0.7, x, 0.6] 
        minIdx = pq.popMinIdx()
        self.assertEqual(minIdx, 0)
        pq.updatePriority(3, 0.9)   # [x, 0.7, x, 0.9] 
        minIdx = pq.popMinIdx()
        self.assertEqual(minIdx, 1)
        minIdx = pq.popMinIdx()
        self.assertEqual(minIdx, 3)
    
        
if __name__ == '__main__':            
    unittest.main()


