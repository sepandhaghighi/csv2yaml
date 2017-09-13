import os
import yaml
import pickle
import json
import sys
Source_dir=os.getcwd()


def zero_insert(input_string):
    '''
    This function get a string as input if input is one digit add a zero
    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    >>> zero_insert("22")
    >>> '22'
    '''
    if len(input_string)==1:
        return "0"+input_string
    return input_string



def convert_bytes(num):
    """
    convert num to idiomatic byte unit
    :param num: the input number.
    :type num:int
    :return: str
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def filesize(fileaddr,fileformat):
    '''
    This function calculate output file size
    :param fileaddr: file addresses
    :type fileaddr:str
    :return: file size for print as string
    '''
    file_info=os.stat(fileaddr+"."+fileformat)
    file_size= file_info.st_size
    print(fileformat.upper()+" File Size : "+convert_bytes(file_size))

def time_convert(input_string):
    '''
    This function convert input_string from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=float(input_string)
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds"

def json_convert(file_name):
    '''
    This function create output file in json format
    :param file_name: file name
    :type file_name:str
    :return: None
    '''
    try:
        file_name=file_name.split(".")[0]
        csv_file=open(file_name+".csv","r")
        json_file = open(file_name + ".json", "w")
        csv_lines=csv_file.readlines()
        data='\t\t\t"data":[\n'
        first_line=csv_lines[0].split(",")
        first_line[-1]=first_line[-1][:-1]
        for index in range(1,len(csv_lines)):
            data = data + '\t\t\t{'
            splited_data=csv_lines[index].split(",")
            data = data + '\n\t\t\t\t' + '"id"' + ':' + '"' + str(index) + '",'
            for i in range(len(first_line)):
                line_data=splited_data[i].replace("\n","")
                line_data=line_data.replace('"','')
                data=data+'\n\t\t\t\t'+'"'+first_line[i]+'"'+':'+'"'+line_data+'",'
            data=data[:-1]+"\n\t\t\t},\n"
        data=data[:-2]+"\n\t\t]\n\t}\n}"
        json_file.write('{\n\t'+'"'+json_file.name+'"'+': {\n')
        json_file.write(data)
        json_file.close()
        csv_file.close()
        filesize(file_name,"json")
    except Exception as e:
        print(str(e))
        print("[Error] Bad Coversion!")
        sys.exit()

def json_to_yaml(filename):
    '''
    This function convert json file to yaml file
    :param filename: filename
    :type filename: str
    :return: None
    '''
    try:
        filename = filename.split(".")[0]
        file=open(filename+".json","r")
        json_data=json.loads(file.read())
        yaml_file = open(filename + ".yaml", "w")
        yaml.safe_dump(json_data,yaml_file,default_flow_style=False)
        file.close()
        yaml_file.close()
        filesize(filename, "yaml")
    except FileNotFoundError:
        print("[Error] Bad Input File")
        sys.exit()


def json_to_pickle(filename):
    '''
    This function convert json file to yaml file
    :param filename: filename
    :type filename: str
    :return: None
    '''
    try:
        filename = filename.split(".")[0]
        file=open(filename+".json","r")
        pickle_file=open(filename+".p","wb")
        json_data=json.loads(file.read())
        pickle.dump(json_data,pickle_file)
        pickle_file.close()
        file.close()
        filesize(filename, "p")
    except FileNotFoundError:
        print("[Error] Bad Input File")
        sys.exit()






