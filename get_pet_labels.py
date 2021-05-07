#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:Eman Abdelhalim
# DATE CREATED: 2/5/2021                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
     """
    #Retrieve the file names from folder pet_images
    filename_list = listdir("pet_images/")
    
    #print 10 files from pet_images folder
    print("\nPrints 10 files from pet_images folder/")
    for idx in range(0,10,1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]))
    
    #create empty dictionary named results_dir
    results_dic = dict()
    
    # Determines number of items in dictionary 
    items_in_dic = len(results_dic)
    print("\nEmpty dictionary results_dic - n items =",items_in_dic)
    
    # Add new key-value pairs to dictionary only when key doesn't already exist. the value is a      list contian only one item the pet image label
    filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
    pet_labels = ["beagle", "boston terrier"]
    for idx in range(0,len(filenames),1):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("** warning: key=", filenames[idx] ,"already exists in result_dic with value=", results_dic[filenames[idx]])
            
     # iterating through a dictionary printing all keys and their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "pet_labels=", results_dic[key][0])
        
    # Format the pet image labels such that they can be matched to the classifier function         labels and the dog names in dognames.txt
    
    # set pet_images varibale to a filename
    pet_image = "Boston_terrier_02259.jpg"
    
    #set strings to lower case letters
    low_pet_images = pet_image.lower()
    
    #splits lower case string by _ to break into words
    word_list_pet_image = low_pet_images.split("_")
    
    # Creates temporary label variable to hold pet label name extracted
    pet_name = ""
    
    #create loops to check if word in pet name contains only alphabetic characters -
    #if true append word to pet_name seprated by space
    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "
            
    # strip off starting/trailing whitespace characters
    pet_name = pet_name.strip()
    
    #print results pet_name
    print("Filename =", pet_image, "Label=", pet_name)
    
      
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
