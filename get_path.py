"""This module will allow us to use any kind of file from anywhere by getting its
abs file path"""


#Importing modules
import os

#Function to be able to connect to files in outer directories
#This will allow you to access any file/dir in Nexus folder
def get_path(*parts):
    return os.path.join((os.path.dirname(os.path.abspath(__file__))), *parts)