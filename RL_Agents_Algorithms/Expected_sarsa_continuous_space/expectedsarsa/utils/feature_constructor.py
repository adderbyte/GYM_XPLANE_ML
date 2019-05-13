 
import  expectedsarsa.exception as ThrowErrors #import ExpectedSarsaError # handle errors
from sklearn.kernel_approximation import Nystroem,RBFSampler
from sklearn.preprocessing import PolynomialFeatures
import sklearn.pipeline

class FeatureConstructor(object):
    
    def __init__(self, featureProcessor = "None",sampledStates='None', n_components=60,gamma = [0.02],n_kernels=1,polynomial_degree=2):

        '''
        This class contains functions that approximate the feature mappings that correspond to certain kernels, 
        and are used for non linear approximation of the state space as discussed in sutton and Barton Introduction to 
        Reinforcement learning.

        input: 
            featureProcessor: a string specifying the name of the feature processor to use. String should be
                              one of RadialBasis, Nystreum or Tilecoding
            sampledStates: an array sampled from the state space of the agent
            n_components : number of components to return during fitting
            n_kernels    :  an integer; the number of kernels (there might be different kernels each with different parameter gamma)
            gamma        :  a list;  the list of pamameter for each the kernel (n_kernel should equal length or size of gamma)
            polynomial_degree : an int, if polynomial kernel is used this should be specified

        Output: (depends on the function called)

            fittedKernel: an array, the result of applying one of the feature processor on the sampled State.
            


        To define custom Feature Processor :
        Example :
        
        classInstance = FeatureConstructor('myprocessor',sampledDataArray)
        classInstance.FeatureDictionary['myProcessor'] =  Function() # set the function to equal a value in the dictonary
        classInstance.fittedKernel # the returned fitted function (and use transfrom on new sample point) 
                                     # transform function should return the processed state

        '''

        self.polynomial_degree = polynomial_degree
        self.sampledStates =  sampledStates
        
        self.featuresProcessor = featureProcessor # name for the feature extractor function
        self.n_components = n_components
        self.gamma = gamma
        self.n_kernels = n_kernels
        self.FeatureDictionary = self.__FeatureDictionary() # return dictionary
        

    def __FeatureConstrutorType(self):
        '''
        This function enables to specify the kind of agent we want to use
        Add as many agent as you want here.

        '''
       ################################################################################
        # check that the supplied named function is  either Radial, Nystreum or 
        if self.featuresProcessor is not None: # check if agent name is valid
            if  self.featuresProcessor in self.FeatureDictionary.keys():
                return self.FeatureDictionary[self.featuresProcessor]()
            else:
                raise ThrowErrors.ExpectedSarsaError('provide a valid name ("RadialBasis","Nystroeum","Polynomial") for string input name for feature \
                    extractor or add a new custom kernel function')
       ################################################################################
        else:
            return sampledStates # if none is specified return the sampled data itself
    
    def __FeatureDictionary(self):
        '''
        dictionary with key constiting of name of the kernel function and value the function definition of
        the kernel function
        '''
        ################################################################################
        ########## dictionry for kernel functions 
        # can be extended to include custom function
        self.__FeatureDictionarys = dict(
                                 RadialBasis=self.__RadialBasis,
                                Nystroem=self.__Nystroem,
                                Polynomial=self.__Polynomial) # keep the feature extrator and the function in a dictionary
                                                                # this makes it possible to define a new function
        ################################################################################
        
        return self.__FeatureDictionarys

    @property
    def fittedKernel(self):
        '''
        @property : using this as a syntactic sugar (ie as a way of saying) get the value of a variable returned
        from an private function (self__FeatureConstructor)

        '''

        self._ProcessedState = self.__FeatureConstrutorType() # return the fitted kernel function.
                                                           
        return self._ProcessedState

    def __componentTest(self):
        
        if not  len(self.gamma) == self.n_kernels:
                raise ThrowErrors.ExpectedSarsaError('length of parameter gamma should be same as number of kernels')

    def __RadialBasis(self):

        '''
        This is where the feature extractor function is defined .
        output: returns the radial basis funtion after being fited to the data

        '''
        #############################################################################################################
        self.__componentTest() # test that sample self.n_kernels is equal to length of list self.n_gamma
        #############################################################################################################


        #############################################################################################################
        # kernel function initialised
        # notice the use of for loop list comprehension hence why we need to check that gamma is in range of n_kernels
        # ths ensures self.gamma[i] returns a value for each self.kernels we make
        # str(i) is the unique name for each kernel
        kernel = sklearn.pipeline.FeatureUnion([
        (str(i), RBFSampler(gamma=self.gamma[i], n_components = self.n_components)) for i in range(self.n_kernels)])
        # fit the sample data point to the initialised kernel function
        kernel.fit(self.sampledStates)
        #############################################################################################################
        return kernel 

        

    def __Polynomial(self):

        '''
        This is where the feature extractor function is defined .
        output: returns the polynomial funtion after being fited to the data
        '''
        ################################################################################
        polyfit = PolynomialFeatures(degree=self.polynomial_degree)
        ################################################################################


        ################################################################################
        # train data point
        train_data = self.sampledStates[0].reshape(1,-1)
        # fit data point
        polyfeat = polyfit.fit(train_data)
        ################################################################################

        return polyfeat

    def __Nystroem(self):

        '''
        This is where the feature extractor function is defined .
        output: returns the Nystreum kernel funtion after being fited to the data
        '''
        #############################################################################################################
        self.__componentTest() # test that sample self.n_kernels is equal to length of list self.n_gamma
        #############################################################################################################


        #############################################################################################################
        # kernel function initialised
        # notice the use of for loop list comprehension hence why we need to check that gamma is in range of n_kernels
        # ths ensures self.gamma[i] returns a value for each self.kernels we make
        # str(i) is the unique name for each kernel

        kernel = sklearn.pipeline.FeatureUnion([
        (str(i), Nystroem(gamma=self.gamma[i], n_components = self.n_components)) for i in range(self.n_kernels)])
        # fit the sample data point to the initialised kernel function
        kernel.fit(self.sampledStates)
        #############################################################################################################


        return kernel 


    @staticmethod
    def transform(kernel,data,customkernel=False):
        '''
        After fitting the feature extractor,
        call transform to transfrom any new data point

        input : 
               kernel :  the fitted function kernel function
               data   :  an array, the data point to be transformed 
               customkernel : set this to True of you have used a custom kernel Function
        output :
               output : the transformed data. 



        '''
        #############################################################################################################
        #precondition : kernel should be an instance of  kernel function from FeatureConstructor or other custom function
        if  type(kernel) != sklearn.pipeline.FeatureUnion and type(kernel) != sklearn.preprocessing.data.PolynomialFeatures:
            if  not customkernel:
                raise ThrowErrors.ExpectedSarsaError('You should first call FeatureConstructor to fit a kernel to sampled Data')
            elif  customkernel:
                pass 
        #############################################################################################################

        #############################################################################################################
        # if data is 1 dimensional or single sample point reshape the data 
        if data.ndim ==1:
            data = data.reshape(1,-1)
        #############################################################################################################

        #############################################################################################################
        # apply kernel transform
        result = kernel.transform(data)
        #############################################################################################################

        #############################################################################################################
        # if data is 1 dimensional or single sample point reshape the data 
        if data.ndim ==1:
            result = result.reshape(result.shape[1],)
        #############################################################################################################
        return result