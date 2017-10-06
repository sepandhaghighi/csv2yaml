from .csv2yaml import *
import time
import sys
import doctest
import os
def run(filename,header=None,error_pass=False):
    first_time = time.perf_counter()
    print("Converting ... ")
    json_size=json_convert(filename,header=header,error_pass=error_pass)
    if json_size!=None:
        pickle_size=json_to_pickle(filename,error_pass=error_pass)
        yaml_size=json_to_yaml(filename,error_pass=error_pass)
        print(json_size)
        print(pickle_size)
        print(yaml_size)
    second_time = time.perf_counter()
    elapsed_time = second_time - first_time
    elapsed_time_format = time_convert(str(elapsed_time))
    print("Converted In " + elapsed_time_format)
    print("Where --> " + Source_dir)
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",verbose=True)
        elif args[1].upper()=="ALL":
            file_header=None
            if len(args)>2:
                file_header=args[2]
            for file in os.listdir():
                if file.find(".csv")!=-1:
                    run(filename=file,header=file_header,error_pass=True)
        elif len(args)>2:
            run(args[1],header=args[2])
        else:
            run(args[1])
    else:
        print("Please pass filename to csv2yaml")
        print("python -m csv2yaml test.csv header(optional)")
        sys.exit()
