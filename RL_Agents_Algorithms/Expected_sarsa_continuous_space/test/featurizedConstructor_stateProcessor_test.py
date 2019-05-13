from expectedsarsa.utils import feature_constructor as fc
from expectedsarsa.utils import space_processor as sp
import numpy as np

import gym 



#############################################################################33
# test  featurized constructor using  simple  input
# This example uses a simple list as input
train_data = np.array([[10.,2.],[3.,4.],[7.,9.]])
kernelRBF = fc.FeatureConstructor('RadialBasis',train_data).fittedKernel
kernelNystroem = fc.FeatureConstructor('Nystroem',train_data,n_components = train_data.shape[0] ).fittedKernel
kernelPolynomial = fc.FeatureConstructor('Polynomial',train_data).fittedKernel

# Test data and ouput
test_data = np.array([1,2])
print('Radial Basis Test: ',fc.FeatureConstructor.transform(kernelRBF,test_data)) # for single sample point reshape data
print('Nystreum Test: ',fc.FeatureConstructor.transform(kernelNystroem,test_data)) # for single sample point reshape data
print('Polynomial Test: ',fc.FeatureConstructor.transform(kernelPolynomial,test_data)) # for single sample point reshape data

#############################################################################



#############################################################################
#### Sample Gym environment usage 
# replace the array in the fisrt exampöle with samples from the state space  : do this using the state processor function
# use the state_processor to return standardized data and then apply nonlinear transform of the featurizConstructor
# this forms a simple pipeline

env = gym.make('MountainCarContinuous-v0')
n = 5
scaler_tansform = sp.standardizer(sp.state_space_sample(n,env)) # get samples from the state and fit a standard scaler to it

# apply the featurizer module which is a non-linear mapping  on feature sapce 
processedFeature = fc.FeatureConstructor('RadialBasis',scaler_tansform.transform(sp.state_space_sample(n,env))).fittedKernel
test_fit = sp.state_space_sample(1,env)
print('.....................',test_fit)
print('  (RBF) mountain car feature extractor: ',fc.FeatureConstructor.transform(processedFeature,scaler_tansform.transform(test_fit)))

# Nystreum
processedFeature = fc.FeatureConstructor('Nystroem',scaler_tansform.transform(sp.state_space_sample(n,env)),n_components=n).fittedKernel
test_fit = sp.state_space_sample(1,env)
print('.....................',test_fit)
print(' (Nystreum) mountain car feature extractor: ',fc.FeatureConstructor.transform(processedFeature,scaler_tansform.transform(test_fit)))

#############################################################################


###############################################################################
### Make custom extractor
train_data = np.array([[10.,2.],[3.,4.],[7.,9.]])
classInstance = fc.FeatureConstructor('myProcessor', train_data) # instantiate the Feature extractor with the new kernel function name

#*******************************************************************************
### define the new kernel class 
### dummy example shown below

class custom_feature(object):
    '''

    sample dummy class and how to use it to make a new desired feature extractor

    '''

    def __init__(self):
        self.fit = self.__fit
        

    def __fit(self):
        '''
        custom feature extractor
        '''

        # do some preprocessing
        

        return custom_feature()
    def transform(self,data):
        
        scalar = 5
        self.transform = data*scalar
        return self.transform
#*******************************************************************************



#*******************************************************************************
customFeatureClass =  custom_feature() # make an instance of new class

classInstance.FeatureDictionary['myProcessor'] = customFeatureClass.fit # set the function equal to the fit function of custom class. Notice that the name of the processor should not change

#*******************************************************************************



#*******************************************************************************
print('myProcessor is now a kernel ',[i for i in  classInstance.FeatureDictionary.keys()]) # check that the function is now in the dictionay holder for kernel functions
customFit = classInstance.fittedKernel # this returns the result of running the fit function that was set in the dictionary
fc.FeatureConstructor.transform(customFit,train_data,customkernel=True) # transform a new data points
#*******************************************************************************


################################################################################
# uncomment to test this functionality
## # Raise error if name is invalid 
train_data = np.array([[10.,2.],[3.,4.],[7.,9.]])
## kernelRBF = fc.FeatureConstructor('Invalid Name',train_data).fittedKernel  
################################################################################