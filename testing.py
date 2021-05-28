def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    #creates empty dictionary for results_Stats_dic
    results_stats_dic = dict()
    
    #sets all counters to initial values of zero so that they can 
    #be incremented while processing through the images in results_dic
    results_stats_dic['n_dogs_images']= 0
    results_stats_dic['n_matches']= 0
    results_stats_dic['n_correct_dogs']= 0
    results_stats_dic['n_correct_notdogs']= 0
    results_stats_dic['n_correct_breeds']= 0
    
    #iterate through the results dictionary
    for key in results_dic:
         #labels match excatly
         if results_dic[key][2] == 1:
            results_stats_dic['n_matches'] +=1
            
         #image label is a dog and Labls match - counts correct breeds
         if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breeds'] +=1
                    
         # pet images label is a dog - counts number of dog images
         if results_dic[key][3]== 1:
             results_stats_dic['n_dogs_images'] +=1 
       
            # classifier classifies images as dog - counts number of correct dogs
             if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] +=1
                   
         
         # pet images label is Not a dog - not match
         else:
             # classifier classifies images as not dog - counts number of correct not dogs
             if results_dic[key][4] == 0:
               results_stats_dic['n_correct_notdogs'] +=1
       
     
    #calculates run statistics (counts, percentages) that are calculates using a counter above
    # calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)
    
    #calculates number of not a dog images - using images and not dog images
    results_stats_dic['n_notdog_images']= (results_stats_dic['n_images']- 
                                            results_stats_dic['n_dogs_images'])
    
    # Calculates % correct for matches
    results_stats_dic['pct_match']= (results_stats_dic['n_matches']/ 
                                     results_stats_dic['n_images'])*100.0
    
    try:                                   
       # Calculates % correct dogs
       results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs']/ results_stats_dic['n_dogs_images'])*100.0                                                           except ZeroDivisionError as e:
           print("ZeroDivisionError occurred: {}".format(e))
        
    try:    
        results_stats_dic['pct_correct_breeds'] =(results_stats_dic['n_correct_breeds']/
                                                  results_stats_dic['n_dogs_images'])*100.0
    except ZeroDivisionError as e:
           print("ZeroDivisionError occurred: {}".format(e))

     # Calculates % correct not-a-dog images
     # Useing conditional statement for when no 'not a dog' images were submitted     
    if results_stats_dic['n_notdog_images'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs']/
                                                 results_stats_dic['n_notdog_images'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
        
    return results_stats_dic
  
