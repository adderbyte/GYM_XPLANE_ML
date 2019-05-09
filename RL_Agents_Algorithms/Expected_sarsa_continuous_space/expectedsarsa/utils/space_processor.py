import numpy as np
from sklearn import preprocessing

def state_space_sample(n,environment):

    '''

    input :
            n :             size of the sampled data points
            environment:    instance of gym environrment. 
                            With continuous state or action space 
            space_to_sample :  spe

     output:

            sampled_data :  an array of size of sampled from the state or action space.


    '''

    #################################################################3
    ## check that the state space is pf type box 

    # The state space we want to check
    box_type = 'Box'
    # get state space 
    state_space_type = environment.observation_space 
    # assert the  state space is box. convert the state space from type space.Box to string
    # check that the fist word in the string is a 'Box'. The regular expression in square bracket gets the 
    # first word separated by  '('  which shuld be the word 'Box': apply len to get the length
    assert str(state_space_type)[:len(str(state_space_type).split('(', 1)[0])]== box_type  # this assertion should be true to run 
    #######################################################################


    ######################################################################
    # perform the standard scaler transformation and return the observed examples
    state_samples = np.array([environment.observation_space.sample() for x in range(n)])


    return state_samples
   
def standardizer(state_samples):
    '''
    standardize the state samples 

    input : 
            state_samples : array of state space

    output :

            standardizer : a standardized version of state space

    '''

    scaler = preprocessing.StandardScaler() # standard scaler pipeleine for sklearn
    scaler.fit(state_samples)  # fit the samples 

    return scaler

