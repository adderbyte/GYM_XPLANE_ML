-------------------------
###### Expected Sarsa
--------------------

Implementation of expected sarsa in continuous state and action space.  
Work in progress ...


-------------------------
###### Installation 
--------------------
 Follow these steps: 
 ```
   * clone the repository
   * cd Expected_sarsa_continuous_space  #  ( to Change directory to Expected_sarsa_continuous_space )
   * pip install -e . 
 (-e : Install a project in editable mode  from a local project path or a VCS url , "." signifies present directory )

```

-------------------------
###### To-Do List
--------------------
 - [x] use LSTM to model Actor (action predictor)   -- LSTM models MDP pretty well 
 - [x] save sample action space data 
 - [ ] pre-train LSTM (actor network) (LSTM takes longer to train why not pretrain. Pretrain: give model apriori knowledge of sample space) 
 - [ ] Gaussian Mixture model (Using Maximum Likelihood Estimate algorithm) for probabilistic distribution evaluation of preicted values from LSTM.
 - [ ] Weight action values by the probabilities of MLE
 
 -------------------------
 #### Note on GMM-MLE
 -------------------------
 
 ![equation](https://latex.codecogs.com/svg.latex?%5Cmathb%7BP%7D%20%28a%20%7C%20b%29)
