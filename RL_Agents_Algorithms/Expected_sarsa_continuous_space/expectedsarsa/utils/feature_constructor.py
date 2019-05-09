 
import  expectedsarsa.exception as ThrowErrors # handle errors


class FeatureConstructor(object):
    
    def __init__(self, featureProcessor = "None",sampledStates='None'):

        '''

        input: 
            featureProcessor: a string specifying the name of the feature processor to use. String should be
                              one of RadialBasis, Nystreum or Tilecoding
            sampledStates: an array sampled from the state space of the agent

        Output:

            ProcessedState: an array, the result of applying one of the feature processor on the sampled State.


        To define Feature Processor :
        Example :
        
        classInstance = FeatureConstructor('myprocessor',sampledDataArray)
        classInstance.FeatureDictionary['myProcessor'] =  Function() # set the function to equal a value in the dictonary
        classInstance.ProcessedState # the returned variable from the function

        '''
        self.sampledStates = sampledStates
        self.featuresProcessor = featureProcessor # name for the feature extractor function
        self.FeatureDictionary = dict(
                                 RadialBasis=self.__RadialBasis(),
                                Nystreum=self.__Nystreum(),
                                TiledCoding=self.__TiledCoding()) # keep the feature extrator and the function in a dictionary
                                                                # this makes it possible to define a new function
        
       

    def __FeatureConstrutorType(self):
        '''
        This function enables to specify the kind of agent we want to use
        Add as many agent as you want here.

        '''
        if self.featuresProcessor is not None: # check if agent name is valid
            if  self.featuresProcessor in self.FeatureDictionary.keys():
                return self.FeatureDictionary[self.featuresProcessor]
            else:
                raise ThrowErrors.ExpectedSarsaError('provide a valid name for string input name for feature extractor or add a new function using FeatureDictionary')
        else:
            return sampledStates
            
    @property
    def ProcessedState(self):

        self._ProcessedState = self.__FeatureConstrutorType() # return the extracted feature or 
                                                           # None as applicable or raise exception
        return self._ProcessedState

    def __RadialBasis(self):

        '''
        This is where the agent  defined.
        output: returns the agent definition

        '''
        return self.sampledStates

        

    def __TiledCoding(self):

        '''

        '''
        pass

    def __Nystreum(self):

        '''
        
        '''
        pass
