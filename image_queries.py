import os
import glob
import imageio
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
#############################################################################
# TODO: Add additional imports
#############################################################################


from scipy.spatial.distance import cdist
from matplotlib import image
from sklearn.cluster import MiniBatchKMeans
from skimage.color import rgb2gray
import matplotlib.cm as cm
import operator
import imageio
from dist2 import dist2

def match_descriptors(desc1, desc2):
    """ Finds the `descriptors2` that best match `descriptors1`
    
    Inputs:
    - desc1: NxD matrix of feature descriptors
    - desc2: MxD matrix of feature descriptors

    Returns:
    - indices: the index of N descriptors from `desc2` that 
               best match each descriptor in `desc1`
    """
    N = desc1.shape[0]
    indices = np.zeros((N,), dtype="int64")
    ############################
    # TODO: Add your code here #
    ############################
    
    dist = dist2(desc1, desc2)
    indices = np.argmin(dist, axis = 1)

    # ############################
    # #     END OF YOUR CODE     #
    # ############################
    return indices

def calculate_bag_of_words_histogram(vocabulary, descriptors):
    """ Calculate the bag-of-words histogram for the given frame descriptors.
    
    Inputs:
    - vocabulary: kxd array representing a visual vocabulary
    - descriptors: nxd array of frame descriptors
    
    Outputs:
    - histogram: k-dimensional bag-of-words histogram
    """
    k = vocabulary.shape[0]
    histogram = np.zeros((k,), dtype="int64")

    ############################
    # TODO: Add your code here #
    ############################
    
    ########### this works!!! ############
    # for d in descriptors:
    #     matches = []
    #     for i in range (k):
    #         sse = sum((vocabulary[i]-d)**2)
    #         matches.append(sse)
    #     mindx = np.argmin(matches)
    #     histogram[mindx] +=1
    

    


    ########### Optimizing, going off the same logic ############

    dist = dist2(descriptors, vocabulary)
    indicies = np.argmin(dist, axis = 1)
    for i in indicies:
      histogram[i] += 1
    

    ############################
    #     END OF YOUR CODE     #
    ############################
    
    return histogram

def caculate_normalized_scalar_product(hist1, hist2):
    """ Caculate the normalized scalar product between two histograms.
    
    Inputs:
    - hist1: k-dimensional array
    - hist2: k-dimensional array
    
    Outputs:
    - score: the normalized scalar product described above
    """
    score = 0
    ############################
    # TODO: Add your code here #
    ############################
    score = np.dot(hist1, hist2) / (np.linalg.norm(hist1) * np.linalg.norm(hist2))
    ############################
    #     END OF YOUR CODE     #
    ############################
    return score


