"""
trashlib for GUI
"""



# Process ag file for d3 display
result_file_name = "data/ag_exploration.csv"
result_file = open(result_file_name, "w")
for x in range(1,6):
	
	panel = "pan"+str(x)
	data_file_name = "../RD/sample/DATA/EXPLORATION/panel_"+str(x)+"_filtered_processed.csv" 

	input_data = open(data_file_name, "r")

	for line in input_data:
		line = line.split("\n")
		line = line[0]
		lineInArray = line.split(",")
		result_file.write(panel +","+str(lineInArray[0]+","+str(lineInArray[1]))+"\n")

	input_data.close()
result_file.close()