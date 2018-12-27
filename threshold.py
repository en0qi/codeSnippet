#thresholding and draw histgram

import cv2 as cv
import numpy as np
import os
import sys
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure as fig
from scipy import stats

args = sys.argv
line = 127 #set thresholding

if not args[1]:
	print("usage:python3 threshold.py [filename]")


if os.path.isfile('./{}'.format(args[1])):
	
	img_org = cv.imread('./{}'.format(args[1]))
	img_cvt = cv.cvtColor(img_org, cv.COLOR_BGR2GRAY) 
	img = cv.medianBlur(img_cvt,5)

	ret,th1 = cv.threshold(img,line,255,cv.THRESH_BINARY)
	th2 = img
	for x in range(0,img.shape[0]):
		for y in range(0,img.shape[1]):
			if img[x,y] == 255:
				pass
			else:
				if img[x,y] < line :
					th2[x,y] = 0
				else:
					th2[x,y] = 255

	gimg = np.array(img_cvt)
	img1dim = []
	for x in range(0,gimg.shape[0]):
		for y in range(0,gimg.shape[1]):
			if gimg[x,y] == 255:
				pass
			elif gimg[x,y] == 0:
				pass
			else:
				img1dim.append(gimg[x,y])

	m=stats.mode(img1dim,axis=None)
	ave = np.average(img1dim)
	mid = np.median(img1dim)

	titles = ['{}\nOriginal Image'.format(args[1]), 'Global Thresholding \n(v = {:.1f})'.format(line)]
	images = [img_org, th2]
	for i in range(2):
		plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
		plt.title(titles[i], fontsize = 8)
		plt.xticks([]),plt.yticks([])
	plt.subplot(2,2,3),plt.hist(img_org.ravel(),255,[0,255]),
	plt.title("mode(blue) = {0}, ave(red) = {1:.2f}\nmid(green) = {2}, threshold(black) = {3:.1f}".format(m[0][0], ave, mid, line), fontsize = 8),
	plt.vlines(m[0][0], 0, 15000, "blue", linestyles='dashed'),
	plt.vlines(ave, 0, 15000, "red", linestyles='dashed'),
	plt.vlines(mid, 0, 15000, "green", linestyles='dashed'),
	plt.vlines(line, 0, 15000, "black", linestyles='dashed')
	plt.savefig('figure_{}.png'.format(args[1]), dpi=270)

else:
	print("File {} not exist!".format(args[1]))





