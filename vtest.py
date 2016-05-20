# -*- coding: utf-8 -*-

from mechanize import Browser
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import os


training = 'http://192.168.19.20/vportal/login.html'
vp = 'http://vportal.creativevirtual15.com/vportal/'


def login(site):
	browser = webdriver.Firefox()
	browser.get(site)

	#Login creds
	tuser = 'ralphg'
	vuser = 'rgorham'
	password = 'Rrrrrrrrrrrrrr83##'

	#Enter user and pw
	time.sleep(2)
	inputUser = browser.find_element_by_name("j_username")
	inputUser.send_keys(vuser)

	inputPW = browser.find_element_by_name('j_password')
	inputPW.send_keys(password)

	#click login button
	log = browser.find_element_by_id('btnLogin').click()

	browser.execute_script("openProjectDB('#gridProjectList',3);")

	return browser



def NAT(browser,*inputs):
	browser.find_element_by_link_text('TEST').click()
	browser.find_element_by_link_text('Content').click()
	browser.find_element_by_link_text('Non Approved Data').click()

	time.sleep(2.5)
	browser.find_element_by_id('btnAsk').click()
	time.sleep(2.5)

	inputQuestion = browser.find_element_by_name("questionTxt")
	inputQuestion.send_keys(inputs)
	browser.execute_script('getAnswer();')
	
	# browser.find_element_by_id('btnAsk').click()
	time.sleep(3)

	browser.find_element_by_id('btnCondition').click()
	time.sleep(3)

	question = browser.find_element_by_id('nlpCondition_question')
	cond_question = question.get_attribute('value')
	if cond_question == '':
		cond_question = 'Safety Net'
	print inputs 
	print '------------->>>>>  %s'  % cond_question
	print ''
	browser.execute_script('closeActiveTab();')
	






def clean(fle):
        with open(fle,'r') as f:
                ignore = ['|','PAST INPUTS','_']
                lst = []
                for line in f:
                	# print line
                        if not any(word in line for word in ignore) and line.isdigit:
                                # print line
                                result = ''.join([i for i in line])
                                # print result
                                lst.append(result)


        cleaned = []
        for l in lst:
        	l = re.sub('^\d+\s', '', l)
                if len(l) >5 and l != '':
                        cleaned.append(l)

    
       

        return cleaned







try:
	os.chdir('C:\Users\Ralph Gorham\Desktop\snapp\suggestions')
	br = login(vp)
	filename = 'confirmation number.txt'
	txt = clean(filename)

	for line in txt:
		NAT(br,line.strip())
except Exception, e:
	print str(e)
else:
	pass
finally:
	pass





br.quit()


