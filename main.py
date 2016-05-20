import random
import pandas
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.utils import check_array
from sklearn.cross_validation import train_test_split
import tensorflow as tf
import tensorflow.contrib.learn as skflow

lucas = tf.constant('Hello Lucas!')
sess = tf.Session()
print(sess.run(lucas))
