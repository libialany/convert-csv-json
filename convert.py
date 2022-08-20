from cmath import log
import csv
import json
import os
if __name__=="__main__":
    file_input=input("user input: ")
    str_output=os.getcwd()+'/'+file_input.split('.')[0]+'.json'
    print(str_output)
    data_dict = {}
    try:
        with open(file_input,'r',encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for rows in csv_reader:
                key =rows['nro']
                data_dict[key]=rows
    except Exception as ex:
        print(f'Err {ex}',ex)
        quit() 
    with open(str_output,'w',encoding='utf-8')as f:
        f.write(json.dumps(data_dict,indent=4))
    
