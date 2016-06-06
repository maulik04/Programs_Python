#!/usr/bin/python

################### MAULIK BHENSDADIA ###################3

import os ## Import OS module

def child():
   print('\nA new child ',  os.getpid()) ## Get the child id
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork() ## Generate child of parent
      if newpid == 0: 
         child()
      else:
         pids = (os.getpid(), newpid)  ##Parent ID
         print("parent: %d, child: %d\n" % pids)
     

parent()
