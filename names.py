import csv
csv_col=['ID','name','country']
dict_data=[{'ID':1,'name':'fathima','country':'india'},
	{'ID':2,'name':'nija','country':'india'},
	{'ID':3,'name':'rameesa','country':'usa'},
	{'ID':4,'name':'rahmath','country':'usa'},
	{'ID':4,'name':'nowfi','country':'india'}]
csv_file="names.csv"
try:
 with open(csv_file,'w')as file1:
      writer=csv.DictWriter(file1,fieldnames=csv_col)
      writer.writeheader()
      for data1 in dict_data:
          writer.writerow(data1)
except IOError:
	print("I/O error")
data1=csv.DictReader(open(csv_file))
print("csv file as a dictionary:\n")
for row in data1:
    print(row)
                                        
