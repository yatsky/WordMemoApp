#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cfg

def Hello():
	print "Welcome to word memorize app!"
	
def UserInfo():
	info = []
	info.append(raw_input("Please tell me your name."))
	info.append(raw_input("Please tell me your age."))
	
	cfg.UserInfo = info
	
def Bye():
	bye = "I hope you enjoyed this app!\nBye!"
	print bye