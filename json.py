# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 15:59:43 2023

@author: Sh_Jurayeff
"""

import json

# x = 10
# x_json = json.dumps(x)

# y = 5.5
# y_json = json.dumps(y)

# n = True
# n_json = json.dumps(n)

# numbers = (23,43,32,34)
# numbers_json = json.dumps(numbers)

# patient = {
#     "fullname" : "Sherali Jo'rayev",
#     "age" : 20 , 
#     "family" : True,
#     "children" : ("Muhammadali","Ko'hinur"),
#     "alergy"  : None,
#     "drugs" : [
#         {"name" : "Kupen" , "amount" : 0.5} , 
#         {"name" : "Totema" , "amount" : 1}
#         ]    
#     }
# patient_json = json.dumps(patient , indent=4 , sort_keys= True )
# print(patient_json)


# with open('patient.json' , 'w') as file:
#     json.dump(patient, file)

# with open('numbers.json' , 'w') as file:
#     json.dump(numbers, file)

# patient2 = json.loads(patient_json)

# print(type(patient))

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# with open("data.json", 'w') as file:
#     json.dump(data, file)
data_json = json.dumps(data, indent= 10)
#print(data_json)      

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
print(talaba_json)













