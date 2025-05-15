#------------------------------------------------------------------------------------------------
#PYTHON FINAL PRACTICAL
#------------------------------------------------------------------------------------------------
#READ CAREFULLY AND THOROUGHLY. TEST THE FUNCTIONS THOROUGHLY.
#WHEN YOU ARE DONE,
#(1) SAVE THE FILE NAME WITH YOUR LAST NAME PYTHON FILE Ex: KelleyPythonExam2_2024.py
#(2) MAKE SURE THE FILE RUNS - NO ERRORS - EVEN IF YOU DIDN'T GET EVERYTHING CORRECT!
#(3) WHEN I RUN THE FILE IN PYTHON, NOTHING SHOULD BE PRINTED OUT (POINTS WILL BE SUBTRACTED)
#(4) SUBMIT YOUR EXAM

#----------------------------------------------------------------------------------------------------
#== FUNCTION 1 ==
#Write a function called weight_matrix, that takes in three float values as its arguments.
#Calculate the weight matrix value for the given float values.
#The first float value will be the total count of a base at a particular position (Nij).
#The second float value will be the total number of sequences in the alignment (N).
#The third float value will be the probability index of a base being at a particular position (Pi).
#Weight Matrix Equation:    [  (Nij + Pi) / (N + 1)  ]
#                        Ln |------------------------|
#                           [           Pi           ]  
#The weight matrix value should be returned.  Note: Ln is the natural log.

import math
def weight_matrix(Nij, N, Pi):
    wm_eq = ((Nij + Pi) / (N +1)) / Pi
    log_value = math.log(wm_eq)    
    return log_value

#Test the function with these data as the arguments. (return => 0.167054084663)
float2a=3  #Nij
float2b=10 #N
float2c=0.25 #Pi
print(weight_matrix(float2a,float2b,float2c))

#----------------------------------------------------------------------------------------------------
#== FUNCTION 2 ==
#Write a function called find_motifs two argument:
#  1) a motif
#  2) a dictionary of sequences
#and returns a dictionary that only includes sequences that match the motif 

import re
def find_motifs(motif, dict_seq):
    result = {}
    for key, seq in dict_seq.items():
        if re.search(motif, seq):
            result[key] = seq
    return result 
          
m='C[CG]'
test_data={0:'AGAC',1:'AGTCCC',2:'GAA',3:'GGCGG',4:'ATTAGGA'}

#Test the function with the motif and test_data
#It should return: {1: 'AGTCCC', 3: 'GGCGG'}
print(find_motifs(m, test_data))
#----------------------------------------------------------------------------------------------------
#== FUNCTION 3 ==
#Write a function called extract_pept that takes a sequence dictionary as an argument
#and returns a dictionary with only the key value pairs that have sequence that 
#begin with a start codon "ATG" or "AUG". However, the returned dictionary needs to contain
#only RNA seqeunces. In other words, all the T's need to be changed to U's.

def extract_pept(seq_di):
    result = {}
    for key, seq in seq_di.items():
        if seq[0:3] =='ATG' or seq[0:3] =='AUG':
            seq = seq.replace('T', 'U')
            result[key]=seq
    return result
          

test_data={0:'AGTACG',1:'AUGCCC',2:'GAA',3:'GGCGG',4:'ATGAGGGCG',5:'AUGGGGGAA'}

#Test the function with sequence_names, sequence_data.
#It should return: {1: 'AUGCCC', 4: 'AUGAGGGCG', 5: 'AUGGGGGAA'}
print(extract_pept(test_data))

#----------------------------------------------------------------------------------------------------
#== FUNCTION 4 ==
#Write a function called bray curtis that takes in a two lists of samples counts
#and returns the bray-curtis distance. Make sure to check that the list lengths
#are equal before doing the calculation. If they are not equal, print "The samples
#do not have the name number of features." and return 0

def bray_curtis():
   return

sampleA=[10, 50, 100, 150]
sampleB=[150, 100, 50, 10]

#Test the function with sampleA and sampleB
#It should return: 0.6129032258064516
#print(bray_curtis(sampleA, sampleB))








