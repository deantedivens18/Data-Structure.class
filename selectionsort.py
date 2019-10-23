# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:05:45 2019

@author: DMDivens.2018
"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
    
names=Stack()
names.push("Money")
print(names.peek())
names.push("Cash")
print(names.peek())

