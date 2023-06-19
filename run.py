from data import LoadData
import data
from custom_arguments import parse_arguments
from features import GetFeatures
from preprocess import PreProcess
import numpy as np

def main():
    parser=parse_arguments()
    args=parser.parser.parse_args()
    
    if args.input_path:
        loader=LoadData(args.input_path)
        loader.load()
        loader.label_encode()
        PP=PreProcess(loader.data_array,channels=args.channels)
        PP.notched_wave()
        dat=PP.nw   # data array with notch filter applied already
        labels=loader.labels   #labels are encoded
        print(np.array(dat).shape)
        
        print("sampling frequency=",PP.sr, "notch frequency=",PP.nf,"channels=",PP.ch)
        
    else:
        print("Please provide path")
    
    
    
if __name__=="__main__":
    main()