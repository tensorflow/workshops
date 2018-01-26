# AMLD "Tensorflow Basics" Workshop

This workshop was given during the Applied ML days at EPFL:

https://www.appliedmldays.org/workshop_sessions/tensorflow-basics.1

The workshop introduces basic Tensorflow concepts and contains example code to
build different estimators (canned, 2D convolutional, RNN). We use the
["Quick, Draw" dataset](quickdraw.withgoogle.com/data). The repository also
contains example code for training the models on Google's
[Cloud ML](https://cloud.google.com/ml-engine/).


## Installation

1. Install [Docker CE](https://www.docker.com/community-edition)
2. Download this repository: `git clone https://github.com/tensorflow/workshops`
3. Change directory: `cd workshops/extras/amld`
4. Run Tensorflow Docker image:
   `docker run -it -v $(pwd)/notebooks:/notebooks/amld -p 127.0.0.1:8888:8888 -p 127.0.0.1:6006:6006 tensorflow/tensorflow`
5. Navigate to http://localhost:8888/tree/amld/exercises
6. Work through exercises `0_intro.ipynb` ... `5_qd_cloud.ipynb`.

