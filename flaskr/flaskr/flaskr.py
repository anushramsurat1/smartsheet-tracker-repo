
#!/usr/bin/env python3
import http.client
import base64
import ssl
import sys
from flask import render_template, url_for
from flask import Flask, request, jsonify, session, redirect
import json
import yaml
import jinja2
from jinja2 import Environment, FileSystemLoader, Template
import imp
import smartsheet





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('table.html')


@app.route('/processing', methods=['GET'])
# Install the smartsheet sdk with the command: pip install smartsheet-python-sdk
def fncall():

	access_token = '1z5jdg7hcu19r4029w6ni7bo54'
	sheet_id = 3036915575351172
	column_map = {}
	ss = smartsheet.Smartsheet(access_token)
	ss.errors_as_exceptions(True)
	sheet = ss.Sheets.get_sheet(sheet_id)
	global r1 
	r1 = []
	global r2
	r2 = []
	global r3
	r3 = []
	global r4
	r4 = []
	global r5
	r5 = []
	global r6
	r6 = []

	global c1 
	c1 = []
	global c2
	c2 = []
	global c3
	c3 = []
	global c4
	c4 = []
	global c5
	c5 = []
	global c6
	c6 = []

	global d1 
	d1 = []
	global d2
	d2 = []
	global d3
	d3 = []
	global d4
	d4 = []
	global d5
	d5 = []
	global d6
	d6 = []


	def get_cell_by_column_name(row, column_ame):
	    column_id = column_map[column_ame]
	    return row.get_column(column_id)

	def evaluate_row_and_build_updates(source_row):
	    # Find the cell and value we want to evaluate
	    
	    
	        status_celltype1 = get_cell_by_column_name(source_row, "Status")
	        status_valuetype1 = status_celltype1.display_value
	        #remaining_cell = get_cell_by_column_name(source_row, "Remaining`111")
	        print("Row #" + str(source_row.row_number))
	        global project_cell
	        project_cell = get_cell_by_column_name(source_row, "Project Name")
	        global project_value
	        project_value = project_cell.display_value
	        global result
	        result = jsonify(project_value)
	        
	        

	        description_cell = get_cell_by_column_name(source_row, "Description")
	        description_value = description_cell.display_value
	        print(str(description_value))

	        customers_cell = get_cell_by_column_name(source_row, "Key Customer")
	        customers_value = customers_cell.display_value
	        print(str(customers_value))

	        techlead_cell = get_cell_by_column_name(source_row, "Tech Lead")
	        techlead_value = techlead_cell.display_value
	        print(str(techlead_value))

	        
	        print(str(status_valuetype1))

	        info_cell = get_cell_by_column_name(source_row, "Additional Info")
	        info_value = info_cell.display_value
	        print(str(info_value))

	        if (status_valuetype1 == "Lost" or status_valuetype1 == "Inactive"):
	        	r1.append(project_value)
	        	print(str(project_value))
	        	r2.append(description_value)
	        	print(str(description_value))
	        	r3.append(customers_value)
	        	print(str(customers_value))
	        	r4.append(techlead_value)
	        	print(str(techlead_value))
	        	r5.append(status_valuetype1)
	        	print(str(status_valuetype1))
	        	r6.append(info_value)
	        	print(str(info_value))


	        if (status_valuetype1 == "Complete"):
	        	c1.append(project_value)
	        	print(str(project_value))
	        	c2.append(description_value)
	        	print(str(description_value))
	        	c3.append(customers_value)
	        	print(str(customers_value))
	        	c4.append(techlead_value)
	        	print(str(techlead_value))
	        	c5.append(status_valuetype1)
	        	print(str(status_valuetype1))
	        	c6.append(info_value)
	        	print(str(info_value))

	        if (status_valuetype1 == "Active"):
	        	d1.append(project_value)
	        	print(str(project_value))
	        	d2.append(description_value)
	        	print(str(description_value))
	        	d3.append(customers_value)
	        	print(str(customers_value))
	        	d4.append(techlead_value)
	        	print(str(techlead_value))
	        	d5.append(status_valuetype1)
	        	print(str(status_valuetype1))
	        	d6.append(info_value)
	        	print(str(info_value))









            
	    
	    
	   
	#resulting=jsonify(project_value)       

	for column in sheet.columns:
	    column_map[column.title] = column.id

	rowsToUpdate = []

	for row in sheet.rows:
	    evaluate_row_and_build_updates(row)

	for i in r1:
		print(i)




	
	#for i in x:
	#	print(i)

	#for row in sheet.rows:
	result = r1
	secresult = r2
	thirdresult = r3
	fourthresult = r4
	fifthresult = r5
	sixthresult = r6
	#print(result)   

	ctab1 = c1
	ctab2 = c2
	ctab3 = c3
	ctab4 = c4
	ctab5 = c5
	ctab6 = c6

	dtab1 = d1
	dtab2 = d2
	dtab3 = d3
	dtab4 = d4
	dtab5 = d5
	dtab6 = d6


	
	return jsonify(json1=result, json2 = secresult, json3 = thirdresult, json4 = fourthresult, json5 = fifthresult, json6 = sixthresult, cson1 = ctab1, cson2 = ctab2, cson3 = ctab3, cson4 = ctab4, cson5 = ctab5, cson6 = ctab6, dson1 = dtab1, dson2 = dtab2, dson3 = dtab3, dson4 = dtab4, dson5 = dtab5, dson6 = dtab6)	

