# Prerequisites

This document includes the instructions for setting up TensorFlow Lattice
environment to run jupyter notebooks.

## Colab links

Click on the links below to open these notebooks in [Colaboratory](https://colab.research.google.com), a hosted Jupyter notebook environment that's free to use and requires no setup.

* [00_test_install](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/tensorflow_lattice/00_test_install.ipynb)
* [01_lattice_estimator_basics](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/tensorflow_lattice/01_lattice_estimator_basics.ipynb)
* [02_advanced_lattice_estimators](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/tensorflow_lattice/02_advanced_lattice_estimators.ipynb)
* [03_calibrator_basics](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/tensorflow_lattice/03_calibrator_basics.ipynb)
* [04_lattice_basics](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/tensorflow_lattice/04_lattice_basics.ipynb)
* [05_lattice_mnist](https://colab.research.google.com/github/tensorflow/workshops/blob/master/extras/tensorflow_lattice/05_lattice_mnist.ipynb)


## Requirements

__Requirement 1__: Mac or Linux machine (TensorFlow Lattice does not support
Windows)

__Requirement 2__: Please follow the instructions below to have the following
software installed and get the dataset.

*   python 2.7 or 3.4+
*   virtualenv
*   pip
*   TensorFlow
*   TensorFlow Lattice
*   Numpy
*   Matplotlib
*   Jupyter
*   Pandas
*   Census income dataset
*   MNIST dataset

## Linux instructions

First, we'll setup the virtual environment and install software as follows.

```bash
$ sudo apt-get install python-pip python-dev python-virtualenv
$ cd ~/
~$ virtualenv --system-site-packages tf-lattice
~$ source ~/tf-lattice/bin/activate
(tf-lattice) ~$ pip install --upgrade pip
(tf-lattice) ~$ pip install --upgrade tensorflow-lattice ipykernel
(tf-lattice) ~$ python -m ipykernel install --user --name=tf-lattice
(tf-lattice) ~$ pip install --upgrade jupyter pandas pillow matplotlib numpy
(tf-lattice) ~$ deactivate
```

Next we'll clone TensorFlow workshop git repository to download jupyter
notebooks by following these instructions.

```bash
~$ sudo apt-get install git
~$ mkdir ~/tfl-tutorial && cd ~/tfl-tutorial
~/tfl-tutorial$ git clone https://github.com/tensorflow/workshops.git
```

Now let's download the datasets.

```bash
~$ mkdir -p /tmp/tfl-data && cd /tmp/tfl-data
/tmp/tfl-data$ wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
/tmp/tfl-data$ wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
/tmp/tfl-data$ wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
/tmp/tfl-data$ wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
/tmp/tfl-data$ wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
/tmp/tfl-data$ wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
```

## Mac instructions

First, we'll setup the virtual environment and install software as follows.

```bash
$ sudo easy_install pip
$ cd ~/
~$ virtualenv --system-site-packages tf-lattice
~$ source ~/tf-lattice/bin/activate
(tf-lattice) ~$ pip install --upgrade pip
(tf-lattice) ~$ pip install --upgrade tensorflow-lattice ipykernel
(tf-lattice) ~$ python -m ipykernel install --user --name=tf-lattice
(tf-lattice) ~$ pip install --upgrade jupyter pandas pillow matplotlib numpy
(tf-lattice) ~$ deactivate
```

TIP: ipykernel install may require xcode.

Next we'll clone TensorFlow workshop git repository to download jupyter
notebooks by following these instructions. Please install git from
https://git-scm.com/download/mac if you don’t have git.

```bash
~$ mkdir ~/tfl-tutorial && cd ~/tfl-tutorial
~/tfl-tutorial$ git clone https://github.com/tensorflow/workshops.git
```

Now let's download the datasets.

```bash
~$ mkdir -p /tmp/tfl-data
```

Then download all these datasets and place them under `/tmp/tfl-data`.

1.  https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
1.  https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test
1.  http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
1.  http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
1.  http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
1.  http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
