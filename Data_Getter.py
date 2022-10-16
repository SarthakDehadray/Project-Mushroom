# Mushroom Classification Project

# Data Validation File

#--------------------------------- Validation 1--------------------------------------------------

import pandas as pd
import os
import sys
import time
import logging as lg

# Saving the inbound data
class data_getter:
    lg.basicConfig(filename = "data_getter.log",level = lg.INFO,format = '%(asctime)s %(message)s')
    def obtain_data():
        
        try:
                name = input("Enter filename")
                lg.info("Dataset {} requested by the user".format(name))
                dataset = pd.read_csv("{}.csv".format(name))
                lg.info("Dataset {} loaded successfully".format(name))
                print("Dataset {} loaded successfully".format(name))

        except Exception as e:
                lg.info("Error loading the {} dataset".format(name))
                lg.info(str(e))
                print("Error")
                data_getter.obtain_data()

    

data_link = data_getter.obtain_data()
        
            

        
    
    
    






"""
        url = input("Enter the link here")
        
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            lg.info("Connected to {} successfully".format(url))
            code for downloading the dataset can be written here.As the current dataset is available in local environment in csv form we will use directly.
            selenium can be used for downloading data
        except:
            return "Unable to connect to the URL"

        """
