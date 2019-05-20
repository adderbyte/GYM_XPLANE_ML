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
 - [ ] use LSTM to model Actor (action predictor)   -- LSTM models MDP pretty well 
 - [ ] save sample action space data 
 - [ ] pre-train LSTM (actor network) (LSTM takes longer to train why not pretrain. Pretrain: give model apriori knowledge of sample space) 
