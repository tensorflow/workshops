# [AMLD](https://www.appliedmldays.org) TensorFlow Workshop

This workshop was given during the Applied ML days at EPFL:

https://www.appliedmldays.org/workshop_sessions/tensorflow-basics.1

The workshop introduces basic TensorFlow concepts and contains example code to
build different estimators (canned, 2D convolutional, RNN). We use the
["Quick, Draw" dataset](quickdraw.withgoogle.com/data). The repository also
contains example code for training the models on Google's
[Cloud ML](https://cloud.google.com/ml-engine/).

[![Workshop Slides (link)](workshop_slides.png)](https://goo.gl/395fmU)

## Run notebooks on Colab

Click on the links below to open these notebooks in
[Colaboratory](https://colab.research.google.com), a hosted Jupyter notebook
environment that's free to use and requires no setup.

* [0_intro.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/exercises/0_intro.ipynb)
* [1_qd_data.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/exercises/1_qd_data.ipynb)
* [2_tf_basics.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/exercises/2_tf_basics.ipynb)
* [3_tf_ml.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/exercises/3_tf_ml.ipynb)
* [4_qd_estimator.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/exercises/4_qd_estimator.ipynb)
* [5_qd_cloud.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/exercises/5_qd_cloud.ipynb)

Note that these notebooks depend on being run in order because earlier notebooks
will download files and write shared Python code to the local filesystem and
later notebooks depend on these files.

If you get stuck with the exercises, you can checkout the "solution" notebooks:

* [0_intro.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/solutions/0_intro.ipynb)
* [1_qd_data.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/solutions/1_qd_data.ipynb)
* [2_tf_basics.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/solutions/2_tf_basics.ipynb)
* [3_tf_ml.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/solutions/3_tf_ml.ipynb)
* [4_qd_estimator.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/solutions/4_qd_estimator.ipynb)
* [5_qd_cloud.ipynb](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/amld/notebooks/solutions/5_qd_cloud.ipynb)

## Run notebooks locally

Alternatively, you can also install
[TensorFlow](https://www.tensorflow.org/install/) on your local machine, clone
this repository, and then run [Jupyter](jupyter.org/install) locally.

