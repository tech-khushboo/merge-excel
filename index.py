import pandas as pd
import json
student = 'students.xlsx'
studentAddress = 'students-address.xlsx'
df1 = pd.read_excel(student)
df2 = pd.read_excel(studentAddress)
df1JSON = json.loads(df1.to_json(orient='records'))
df2JSON = json.loads(df2.to_json(orient='records'))

# This is more optimized way:  time complexity - N+N = 2N
temp = {}
for row2 in df2JSON:
    temp[row2['Student Id']] = row2
    
results = []
for row1 in df1JSON:
    key = row1['Id']
    row1.update({'Address':temp[key]['Address'],'Fee':temp[key]['Fee']})
    results.append(row1)
print(results)

# Simple Logic Using Nested For Loops: time complexity - N*N = N^2 (N Square)
# results = []
# for row1 in df1JSON:
#     for row2 in df2JSON:
#         if row1['Id'] == row2['Student Id']:
#             row1.update({'Address':row2['Address'],'Fee':row2['Fee']})
#             results.append(row1)
#             break
# print(results)