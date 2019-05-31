import numpy as np


# def sfill(x, max_chars=10, justify='>'):
#     """Fill a string with empty characters"""
#     return '{}' \
#         .format('{:' + justify + str(max_chars) + '}') \
#         .format(x)


# def sfloat(x, num_chars=10):
#     """Stringify a float to have exactly some number of characters"""
#     x = float(x)
#     num_chars = int(num_chars)
#     start, end = str(x).split('.')
#     start_chars = len(str(float(start)))
#     if start_chars > num_chars:
#         raise Exception('Try num_chars = {}'.format(start_chars))
#     return '{}' \
#         .format('{:' + str(num_chars) + '.' +
#                 str(num_chars - start_chars + 1) + 'f}') \
#         .format(x)


# def shess(hess, num_chars=10):
#     """Stringify an n x n Hessian matrix"""
#     n = hess.shape[0]
#     s = 'Hessian:' + ('\n' + '| {} ' * n + '|') * n
#     return s.format(*[sfloat(h, num_chars)
#                       for h in np.array(hess).reshape(-1)])


# def sarray(x, num_chars=10):
#     n = len(x)
#     return '({})'.format(', '.join([sfloat(xi, num_chars / n) for xi in x]))








import numpy as np
import tensorflow as tf


MAX_CHARS = 15

# generate sample
# np.random.seed(0)
# z_obs = np.random.choice(range(NUM_COMPONENTS),
#                          size=SAMPLE_SIZE,
#                          p=TRUE_PROBS)
# self.train = np.random.normal(loc=TRUE_MU[z_obs],
#                          scale=TRUE_SIGMA[z_obs],
#                          size=SAMPLE_SIZE)

# plot
# import matplotlib.pyplot as plt
# plt.hist([x_obs[z_obs == i] for i in range(NUM_COMPONENTS)],
#          bins=100, stacked=True, alpha=0.5, normed=True,
#          label=['component {}'.format(i + 1) for i in range(NUM_COMPONENTS)])
# plt.legend(loc='upper left')
# plt.show()

# center and scale the data

json1_file = open('keepHeading.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
data = [json1_data[k][1][3] for k in json1_data.keys()]
x_obs = np.array(data) 

class GaussMixture:
#print (len(k))
      def __init__(NUM_COMPONENTS = 3, LOGIT_PARAMS={'mean': 0.0, 'stddev': 0.1},PHI_PARAMS={'mean': 0.0, 'stddev': 0.1}, MU_PARAMS={'mean': 0.0, 'stddev': 0.1},LEARNING_RATE = 0.001, iterations=141,train_episode=2)

          ############# initilisation parameters for the model #############################
          self.LEARNING_RATE = LEARNING_RATE # learning rate
          self.MAX_ITER = iterations #10000
          self.TOL_PARAM, self.TOL_LOSS, self.TOL_GRAD = 1e-8, 1e-8, 1e-8 # criteria for stopping training 
          self.NUM_COMPONENTS =  NUM_COMPONENTS # number of gaussian mixture to use 
          self.train_episode = train_episode
          ############# initilisation parameters for the model #############################

          

          #### initialise tensorflow variables placeholders #################################
          with tf.variable_scope("variable_palceholder"): 
              self.x = tf.placeholder(dtype=tf.float32)
              # initialise logit parameters: from a distribution with mean 0.0. and standard deviation of 0.1
              self.logit = tf.Variable(initial_value=tf.random_normal(shape=[NUM_COMPONENTS],
                                                                 seed=RANDOM_SEED,
                                                                 **INIT_LOGIT_PARAMS),
                                  dtype=tf.float32)

              self.p = tf.nn.softmax(logits=logit)
              #initialise mean parameters: from a distribution with mean 0.0. and standard deviation of 0.1
              self.mu = tf.Variable(initial_value=tf.random_normal(shape=[NUM_COMPONENTS],
                                                              seed=RANDOM_SEED,
                                                              **INIT_MU_PARAMS),
                               dtype=tf.float32)
              # initialise phi parameters: from a distribution with mean 0.0. and standard deviation of 0.1
              self.phi = tf.Variable(initial_value=tf.random_normal(shape=[NUM_COMPONENTS],
                                                               seed=RANDOM_SEED,
                                                               **INIT_PHI_PARAMS),
                                dtype=tf.float32)
              self.sigma = tf.square(phi)
         #######################################################################################
          

         

          ################## store distributon paramters in list ################################
          gaussian_dists = []
          for i in range(NUM_COMPONENTS):
              gaussian_dists.append(tf.contrib.distributions.Normal(loc=self.mu[i],
                                                                    scale=self.sigma[i]))
          #######################################################################################

          ################### Loss function ######################################################
          with tf.variable_scope("loss_function"): 
              categorical_dist = tf.contrib.distributions.Categorical(probs=self.p) # the probability of each mixture model
              mixture_dist = tf.contrib.distributions.Mixture(cat=categorical_dist,
                                                          components= gaussian_dists) # Tensorflow mixture takes in the probability of each gaussian 
                                                                                     # in the mixture and its corresponding paramters(mean, std) 
          #########################################################################################
         
          ################### log_probability_and_likelihood_of_distr #############################
          with tf.variable_scope("log_probability_and_likelihood_of_distr"): 
              log_prob = self.mixture_dist.log_prob(value=self.x) # log probability of x given mixture probability
              self.neg_log_likelihood = -1.0 * tf.reduce_sum(log_prob) # negative log likelihoos
          #########################################################################################
          

          ################### optimizer and grad ###################################################
          with tf.variable_scope("log_probability_and_likelihood_of_distr"): 
              self.optimizer = tf.train.AdamOptimizer(learning_rate=self.LEARNING_RATE)
              self.train_op = optimizer.minimize(loss=self.neg_log_likelihood)
              # gradient
              self.grad = tf.gradients(self.neg_log_likelihood, [self.logit, self.mu, self.phi])
          ################### optimize #############################################################

          
          

      def __train__(data,sess,plot=False): 

          #### Normalize training data ##############################
          self.train_data = data
          self.train_mean = self.train_data.mean()
          self.train_std = self.train_data.std() + 0.000000000001
          self.train_data = (self.train_data - self.train_mean) / self.train_std
          ##################################

          # tensor for data
          output_prob,output_mean, output_log = [],[],[]
          episode_count= 1
          with episode_count <=  self.train_episode :
              #sess.run(fetches=tf.global_variables_initializer())

              i = 1
              obs_logit, self.obs_p, self.obs_mu, obs_phi, self.obs_sigma = sess.run(
                  fetches=[[self.logit], [self.p], [self.mu], [self.phi], [self.sigma]])
              obs_loss = sess.run(fetches=[self.neg_log_likelihood], feed_dict={x: self.train_data})
              obs_grad = sess.run(fetches=[self.grad], feed_dict={x: self.train_data})
              # if TRAIN :
              #     print(' {} | {} | {} | {} | {} | {}'
              #           .format(sfill('iter', len(str(MAX_ITER)), '>'),
              #                   sfill('p', MAX_CHARS + 2 * NUM_COMPONENTS, '^'),
              #                   sfill('mu', MAX_CHARS + 2 * NUM_COMPONENTS, '^'),
              #                   sfill('sigma', MAX_CHARS + 2 * NUM_COMPONENTS, '^'),
              #                   sfill('loss', MAX_CHARS, '^'),
              #                   sfill('grad', MAX_CHARS, '^')))
              episode_count+=1

              while True:
                  # gradient step
                  sess.run(fetches=self.train_op, feed_dict={self.x: self.train_data})

                  # update parameters
                  new_logit, new_p, new_mu, new_phi, new_sigma = sess.run(
                      fetches=[self.logit, self.p, self.mu, self.phi, self.sigma])
                  diff_norm = np.linalg.norm(np.subtract(
                      [param for param_list in [new_logit, new_mu, new_phi]
                       for param in param_list],
                      [param for param_list in [obs_logit[-1], self.obs_mu[-1], obs_phi[-1]]
                       for param in param_list]
                  ))

                  # update loss
                  new_loss = sess.run(fetches=self.neg_log_likelihood, feed_dict={x: self.train_data})
                  loss_diff = np.abs(new_loss - obs_loss[-1])

                  # update gradient
                  new_grad = sess.run(fetches=grad, feed_dict={x: self.train_data})
                  grad_norm = np.linalg.norm(new_grad)

                  obs_logit.append(new_logit)
                  self.obs_p.append(new_p)
                  self.obs_mu.append(new_mu)
                  self.obs_phi.append(new_phi)
                  self.obs_sigma.append(new_sigma)
                  obs_loss.append(new_loss)
                  obs_grad.append(new_grad)

                  # if (i - 1) % 100 == 0:
                  #     print(' {} | {} | {} | {} | {} | {}'
                  #           .format(sfill(i, len(str(MAX_ITER))),
                  #                   sarray(new_p, MAX_CHARS),
                  #                   sarray(new_mu, MAX_CHARS),
                  #                   sarray(new_sigma, MAX_CHARS),
                  #                   sfloat(new_loss, MAX_CHARS),
                  #                   sfloat(grad_norm, MAX_CHARS)))

                  if diff_norm < self.TOL_PARAM:
                      print('Parameter convergence in {} iterations!'.format(i))
                      break

                  if loss_diff < self.TOL_LOSS:
                      print('Loss function convergence in {} iterations!'.format(i))
                      break

                  if grad_norm < self.TOL_GRAD:
                      print('Gradient convergence in {} iterations!'.format(i))
                      break

                  if i >= MAX_ITER:
                      print('Max number of iterations reached without convergence.')
                      break

                  i += 1


          ############################# print results ##################################

            # print('Fitted MLE:')
            # for j in range(self.NUM_COMPONENTS):
            #     print('Component {}: [p={:.4f}, mu={:.4f}, sigma={:.4f}]'
            #           .format(j + 1, obs_p[-1][j],
            #                   SCALE * obs_mu[-1][j] + self.train_mean,
            #                   SCALE * obs_sigma[-1][j]))
            return  self.obs_mu, self.obs_mu, self.obs_sigma
           ############################################################################
          # print('True Values:')
          # for j in range(NUM_COMPONENTS):
          #     print('Component {}: [p={:.4f}, mu={:.4f}, sigma={:.4f}]'
          #           .format(j + 1, TRUE_PROBS[j], TRUE_MU[j], TRUE_SIGMA[j]))

          # obs_m = [i[2] for i in obs_mu]
          # obs_s = [i[2] for i in obs_sigma]
              
          # plot_canonical_gauss(self.train_data, obs_m, obs_s, obs_loss,
          #                      title='canonical params, adam, alpha = {}'
          #                      .format(LEARNING_RATE))