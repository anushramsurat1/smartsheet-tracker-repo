
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



	def get_cell_by_column_name(row, column_ame):
	    column_id = column_map[column_ame]
	    return row.get_column(column_id)

	def evaluate_row_and_build_updates(source_row):
	    # Find the cell and value we want to evaluate
	    status_celltype1 = get_cell_by_column_name(source_row, "Status")
	    status_valuetype1 = status_celltype1.display_value
	    if (status_valuetype1 == "Lost"):
	        #remaining_cell = get_cell_by_column_name(source_row, "Remaining`111")
	        print("Row #" + str(source_row.row_number))
	        global project_cell
	        project_cell = get_cell_by_column_name(source_row, "Project Name")
	        global project_value
	        project_value = project_cell.display_value
	        global result
	        result = jsonify(project_value)
	        print(str(project_value))

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




	    status_celltype2 = get_cell_by_column_name(source_row, "Status")
	    status_valuetype2 = status_celltype2.display_value       

	    if (status_valuetype2 == "Active"):
	        #remaining_cell = get_cell_by_column_name(source_row, "Remaining`111")
	        print("Row #" + str(source_row.row_number))
	        project_cell = get_cell_by_column_name(source_row, "Project Name")
	        project_value2 = project_cell.display_value	       
	        print(str(project_value2))

	        description_cell = get_cell_by_column_name(source_row, "Description")
	        description_value = description_cell.display_value
	        print(str(description_value))

	        customers_cell = get_cell_by_column_name(source_row, "Key Customer")
	        customers_value = customers_cell.display_value
	        print(str(customers_value))

	        techlead_cell = get_cell_by_column_name(source_row, "Tech Lead")
	        techlead_value = techlead_cell.display_value
	        print(str(techlead_value))

	        
	        print(str(status_valuetype2))

	        info_cell = get_cell_by_column_name(source_row, "Additional Info")
	        info_value = info_cell.display_value
	        print(str(info_value))


	    status_celltype3 = get_cell_by_column_name(source_row, "Status")
	    status_valuetype3 = status_celltype3.display_value  

	    if (status_valuetype3 == "Inactive"):
	        #remaining_cell = get_cell_by_column_name(source_row, "Remaining`111")
	        print("Row #" + str(source_row.row_number))
	        project_cell = get_cell_by_column_name(source_row, "Project Name")
	        project_value3 = project_cell.display_value
	        print(str(project_value3))

	        description_cell = get_cell_by_column_name(source_row, "Description")
	        description_value = description_cell.display_value
	        print(str(description_value))

	        customers_cell = get_cell_by_column_name(source_row, "Key Customer")
	        customers_value = customers_cell.display_value
	        print(str(customers_value))

	        techlead_cell = get_cell_by_column_name(source_row, "Tech Lead")
	        techlead_value = techlead_cell.display_value
	        print(str(techlead_value))

	        
	        print(str(status_valuetype3))

	        info_cell = get_cell_by_column_name(source_row, "Additional Info")
	        info_value = info_cell.display_value
	        print(str(info_value))            

	#resulting=jsonify(project_value)       

	for column in sheet.columns:
	    column_map[column.title] = column.id

	rowsToUpdate = []

	for row in sheet.rows:
	    evaluate_row_and_build_updates(row)

	result = str(project_value)
	print(result)    
	    

	
	return jsonify(json1=result)	

