#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cfg, os

def Hello():
	print "Welcome to word memorize app!"
	
def UserInfo():
	info = []
	info.append(raw_input("Please tell me your name."))
	info.append(raw_input("Please tell me your age."))
	
	cfg.UserInfo = info
	
def ListTermPools():
	# files = [f for f in os.listdir('TermPools') if os.path.isfile(f)] this won't work, why?
	path = 'TermPools'
	files = os.listdir(path)
	for file in files:
		print file
	
def Bye():
	bye = "I hope you enjoyed this app!\nBye!"
	print bye