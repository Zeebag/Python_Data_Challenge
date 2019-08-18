#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:45:42 2019

@author: zee_bag
"""

import sys
import os
import pandas as pd

def readCSVFile(fileName):
	try:
		df = pd.read_csv(fileName)
		return df
	except FileNotFoundError:
		print("File Not Found.." + fileName)
		return None
		
def readJSONFile(fileName):
	try:
		df = pd.read_json(fileName)
		return df
	except FileNotFoundError:
		print("File Not Found.." + fileName)
		return None
	except ValueError:
		print("Error Reading JSON file.." + fileName)
		return None

def main():
	print("Reading Prices Data file")
	fileName = "prices.csv"
	priceDF = readCSVFile(fileName)

	print("Reading Auditors Data file")
	fileName = "auditors.csv"
	auditorsDF = readCSVFile(fileName)

	print("Reading Stores Data file")
	fileName = "stores.json"
	storesDF = readJSONFile (fileName)

	#print(priceDF)
	#print(auditorsDF)

	#  we will be processing, only if there are data fetched.
	if (priceDF is not None and auditorsDF is not None):
		df = priceDF
		print (df)
		# if the stores list has been loaded, then we can populate another DataFrame merging with Stores.
		# This gives us the Banner, Region etc.
		if (storesDF is not None):
			df2 = pd.merge(df, storesDF, on="Store ID", how='outer')
 
	# - here columns is the region, values are prices, and the each row is identified by Banner + UPC.
	if (df2 is not None):
		print(df2)
		output = pd.crosstab(
			index=[df2.Banner, df2.UPC], 
			columns=df2.Region, 
			margins=True, 
			values=df2.Price,
			dropna = False,
			aggfunc='mean'
			).round(2)
			#print(output)
	# Finally following command i have used is to write to a file.
	if (output is not None):
		output.to_csv("final_output.csv", index=True)

if __name__== "__main__":
   main()