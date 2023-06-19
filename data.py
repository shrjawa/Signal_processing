import numpy as np
import pandas as pd
import glob,os
import argparse
from sklearn.preprocessing import OneHotEncoder

class LoadData:
    def __init__(self,path):
        self.path=path
        self.data_array=[]
        self.labels=[]
    def load(self):
      
        
        file_list = glob.glob(os.path.join(self.path, '*.txt'))
        if not file_list:
            print("No files found in the specified path.")
            return
        
        for file in glob.glob(os.path.join(self.path, '*.txt')):
            #print(file)
            name=os.path.basename(file)
            label=name.split("_")[0]
            file=pd.read_csv(file,header=None,sep=",",skiprows=6)
            self.data_array.append(np.array(file.iloc[:,1:5],).reshape((4,len(file.iloc[:,1]))))
            self.labels.append(label)
        
    def label_encode(self):
        encoder=OneHotEncoder()
        encoded_data=encoder.fit_transform(np.array(self.labels).reshape(-1,1))
        encoded_data=encoded_data.toarray()
        self.labels=encoded_data
        
        



        
