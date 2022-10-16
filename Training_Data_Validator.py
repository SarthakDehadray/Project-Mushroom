# Training_Data_Validator

"""
Used for checking if the data received is according to the predecided framework
or not.
"""
import logging as lg
import pandas as pd
import os
from os.path import join
import sys
import shutil

class data_validator():
    lg.basicConfig(filename = "data_validator.log",level = lg.INFO,format = '%(asctime)s %(message)s')
    try:
        source = "mushroomaas.csv"
        df = pd.read_csv("mushrooms.csv")
        for i in df.dtypes:
            if i != "object":
                #if not os.path.exists("C:\\Users\Home\Desktop\prog\iNeuron\Project_Mushroom\\Bad_Training_Data"):
                    os.makedirs("C:\\Users\\Home\\Desktop\\prog\\iNeuron\\Project_Mushroom\\Bad_Training_Data")
                    destination_bad = "C:\\Users\\Home\\Desktop\\prog\\iNeuron\\Project_Mushroom\\Bad_Training_Data\\mushrooms{}.csv".format(i)
                    os.replace(source,destination_bad)
                    lg.info("Dataset {} moved to the Bad Training Data Folder".format(name))
                    lg.info("{} not of the requisite type".format(i))
                  
            else:
                    os.makedirs("C:\\Users\\Home\\Desktop\\prog\\iNeuron\\Project_Mushroom\\Good_Training_Data")
                    destination_good = "C:\\Users\\Home\\Desktop\\prog\\iNeuron\\Project_Mushroom\\Good_Training_Data\\mushrooms.csv"
                    os.replace(source,destination_good)
                    lg.info("Dataset {} moved to the Good Training Data Folder".format(name))
                    
    except Exception as e:
        lg.error("Unable to process the dataset")
        lg.error(str(e))


