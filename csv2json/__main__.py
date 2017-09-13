from .csv2json import *
import time
import sys
import doctest
def run(filename):
    first_time = time.perf_counter()
    print("Converting ... ")
    json_convert(filename)
    json_to_pickle(filename)
    json_to_yaml(filename)
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
        else:
            run(args[1])
    else:
        print("Please pass filename to csv2json")
        print("python -m csv2json test.csv")
        sys.exit()
