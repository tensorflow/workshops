# TFX Labs

The following are labs for teaching TFX developer training sessions.

### [Lab 1 - Running a simple pipeline manually in a Colab Notebook](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_1_Pipeline_in_Colab.ipynb)

This notebook demonstrates how to use Jupyter/Colab notebooks for TFX iterative development. Here, we walk through the Chicago Taxi example in an interactive notebook.

Working in an interactive notebook is a useful way to become familiar with the structure of a TFX pipeline. It's also useful when doing development of your own pipelines as a lightweight development environment, but you should be aware that there are differences in the way interactive notebooks are orchestrated, and how they access metadata artifacts.

### [Lab 2 - Introduction to Apache Beam](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_2_Intro_to_Apache_Beam.ipynb)

TFX is designed to be scalable to very large datasets which require substantial resources. Distributed pipeline frameworks such as Apache Beam offer the ability to distribute processing across compute clusters and apply the resources required. Many of the standard TFX components use Apache Beam, and custom components that you may write may also benefit from using Apache Beam for distibuted processing.

This notebook introduces the concepts and code patterns for developing with the Apache Beam Python API.

### [Lab 3 - Using the Apache Beam Orchestrator for TFX](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_3_Beam_Orchestrator.ipynb)

This notebook demonstrates how to use Apache Beam as an orchestrator for TFX. Pipelines are also created in Apache Beam, which means that Beam sequences tasks according to the dependencies of each task, running each task as its dependencies are met. Beam is also highly scalable and runs tasks in parallel in a distributed environment. That makes Beam very powerful as an orchestrator for other pipelines, including TFX.

When using the InteractiveContext in a notebook, running each cell orchestrates the creation and running of each of the components in the TFX pipeline. When using a separate orchestrator, as in this example, the components are only run once the TFX pipeline DAG has been defined and the orchestrator has been triggered to start an execution run.

In this example you will define all the supporting code for the TFX components before instantiating the components and running the TFX pipeline using an Apache Beam orchestrator. This is the pattern which is typically used in a production deployment of TFX.

### [Lab 4 - TensorFlow Data Validation](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_4_Data_Validation.ipynb)

This example colab notebook illustrates how TensorFlow Data Validation (TFDV) can be used to investigate and visualize your dataset. That includes looking at descriptive statistics, inferring a schema, checking for and fixing anomalies, and checking for drift and skew in our dataset. It's important to understand your dataset's characteristics, including how it might change over time in your production pipeline. It's also important to look for anomalies in your data, and to compare your training, evaluation, and serving datasets to make sure that they're consistent.

### [Lab 5 – Preprocessing data with TensorFlow Transform](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_5_TensorFlow_Transform.ipynb)

This example colab notebook provides a somewhat more advanced example of how [TensorFlow Transform](https://www.tensorflow.org/tfx/transform/) can be used to preprocess data using exactly the same code for both training a model and serving inferences in production.

TensorFlow Transform is a library for preprocessing input data for TensorFlow, including creating features that require a full pass over the training dataset.

### [Lab 6 – Model Analysis](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_6_Model_Analysis.ipynb)

This example colab notebook illustrates how TensorFlow Model Analysis (TFMA) can be used to investigate and visualize the characteristics of a dataset and the performance of a model. We'll use a model that we trained previously, and now you get to play with the results!

### [Lab 7 – Fairness Indicators](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_7_Fairness_Indicators.ipynb)

In this activity, you'll use Fairness Indicators to explore the [Civil Comments](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification) dataset. Fairness Indicators is a suite of tools built on top of [TensorFlow Model Analysis](https://www.tensorflow.org/tfx/model_analysis/get_started) that enable regular evaluation of fairness metrics in product pipelines.

### [Lab 8 – Custom Components](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_8_Custom_Components.ipynb)

This notebook demonstrates how to build and use a custom component in your TFX pipeline. We will train an image classification model on the [UC Merced Land Use Dataset](http://weegee.vision.ucmerced.edu/datasets/landuse.html) of aerial pictures, using a custom component to perform image augmentation.

### [Lab 9 – Alternate Pipeline Architectures](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_9_Alternate_Pipeline_Architectures.ipynb)

This notebook demonstrates how to build and use TFX with a different pipeline architecture.  Specifically, the pipeline in this example will branch following the feature engineering with Transform, so that two different Trainers each train and deploy two different model architectures from the same dataset.  This illustrates one possible approach to doing A/B testing.

We will train an image classification model on the [UC Merced Land Use Dataset](http://weegee.vision.ucmerced.edu/datasets/landuse.html) of aerial pictures.

### [Lab 10 – Neural Structured Learning](https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_10_Neural_Structured_Learning.ipynb)

This notebook describes graph regularization for sentiment classification by synthesizing a graph from input data. An end-to-end workflow using the [Neural Structured Learning](https://www.tensorflow.org/neural_structured_learning) framework is demonstrated in a TFX pipeline using several TFX custom components as well as a graph-regularized trainer component.

