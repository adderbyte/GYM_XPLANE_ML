from expectedsarsa.utils import feature_constructor
from expectedsarsa.utils import space_processor as sp

import gym 



#############################################################################33
# test  featurized constructor using  simple  input
# This example uses a simple list as input
processedFeature = feature_constructor.FeatureConstructor('RadialBasis',[1,2,3]).ProcessedState
print('processed feature simple: ',processedFeature)
#############################################################################



#############################################################################
# replace the array in the fisrt exampöle with samples from the state space  : do this using the state processor function
# use the state_processor to return standardized data and then apply nonlinear transform of the featurizConstructor
# this forms a simple pipeline

env = gym.make('MountainCarContinuous-v0')
n = 5
scaler_tansform = sp.standardizer(sp.state_space_sample(n,env)) # get samples from the state and fit a standard scaler to it
print('standard scaler and fit: ', scaler_tansform)
# apply the featurizer module which is a non-linear mapping  on feature sapce 
processedFeature = feature_constructor.FeatureConstructor('RadialBasis',scaler_tansform.transform(sp.state_space_sample(n,env))).ProcessedState
print('processed feature mountain car: ',processedFeature)
#############################################################################