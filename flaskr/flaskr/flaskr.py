
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

	        if (status_valuetype1 == "Lost"):
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

	
	return jsonify(json1=result, json2 = secresult, json3 = thirdresult, json4 = fourthresult, json5 = fifthresult, json6 = sixthresult)	

