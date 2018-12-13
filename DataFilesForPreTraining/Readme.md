## Data Files collected from X Plane Simulation (Typically used for Pre-training)
___________________________________________________________________________________

The files are categorised based on the flight phase (for example landing phase) -- the name of the file will reflect which flight phase data it is.
This could be extended to reflect the type of aircraft too. The aim of these training data is to pretrain the models or 
to find the reward or action space approximator or distribution function. This gives the agent some priors ( or "clues") about the task.

### How To Use
In each file, one finds the flight data for a particular flight phase. A string of integer values or numbers is used as a key. For each number the first value set corresponds to state and the second value set corresponds to the action that produced the state. Typically, we assume an autopilot or human pilot is flying the aircraft and at each iteration time or loop the state and action values as seen by the simulator is collected.

### State Variables and Action Definition
