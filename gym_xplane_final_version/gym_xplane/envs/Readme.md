______________________________

##### Base environment definition
_____________________________


###### Note :


  1. The simulation  regularly sends pause command to ensure no other force (perhaps due to stability or control augmentation in XPlane) is acting on the aircraft. Doing this preserves the Markov Decision Process  of the model and is critical for agent learning.
  2. Another way to do this is to just disbale control and stability augmentation in xplane. This is the more robust option. And would be incorporated in future models
