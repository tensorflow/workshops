# Deep Learning with Keras - Hands-on Workshop

## What to expect:

This workshop is intended for an audience that is new to Keras with a very basic knowledge of Deep Learning.

Workshop Agenda:

Section 1:

* Introduction to Keras
* How to build and train a model using Keras APIs
* Using Callbacks
* Link to colab: 


Section 2

* Building a CNN model using Keras Layers
* Data augmentation with  ImageGenerator
* Feature extraction with pre-trained CNN model
* Introduciton to Fine Tuning
* Link to colab:


Section 3

* Word Embeddings in Keras
* Using pre-trained word embeddings with the Embedding layer
* Introduction to RNN layers
* Link to colab:


Section 4

* Workflow for solving Text Classification problems
* Using a N-gram model
* Using a Sequence model
* Link to colab:


If you want to run the notebooks in this repo locally, here are the installation instructions and the required datasets.

Installation instructions

Required packages:

* Install [Anaconda](https://www.anaconda.com/download/#macos) and create an environment that you can use for this workshop.

* Install [TensorFlow](https://www.tensorflow.org/install/). There is a section specific to installing TensorFlow in a conda environment.

* Install [Keras](https://keras.io/#installation).

* Install [Pillow](https://pypi.org/project/Pillow/2.2.1/).

* Confirm that TensorBoard is installed.
 
Required Datasets:

* Download the Cats Vs Dogs dataset from the [Kaggle website](https://www.kaggle.com/c/dogs-vs-cats/data). You will have to create an account if you don't have one already.

* Download the GloVe pre-trained embedding from the [GloVe website](https://nlp.stanford.edu/projects/glove/).

* Download the IMDB dataset from this [website](http://ai.stanford.edu/~amaas/data/sentiment/)

Verify Installation:

* git clone https://github.com/anj-s/kdd2018.git

* Activate your conda environment

* Start the Jupyter notebook by running "jupyter notebook"
 
* Verify that you can run Keras and TensorFlow by running the "Verify Installation" jupyter notebook.

NOTE:
You will need to modify the data directory paths in the notebooks since you will be pointing to a local directory. 

