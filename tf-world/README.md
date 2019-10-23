# Booth Demos for TensorFlow World

### <a target='#' href='https://colab.sandbox.google.com/github/tensorflow/workshops/blob/master/tfx_labs/Lab_1_Pipeline_in_Colab.ipynb'>Interactive Notebook</a>

This notebook demonstrates how to use Jupyter/Colab notebooks for TFX iterative development. Here, we walk through the Chicago Taxi example in an interactive notebook.

Working in an interactive notebook is a useful way to become familiar with the structure of a TFX pipeline. It's also useful when doing development of your own pipelines as a lightweight development environment, but you should be aware that there are differences in the way interactive notebooks are orchestrated, and how they access metadata artifacts.

### <a target='#' href='https://colab.corp.google.com/drive/13NXkylgiyIHkw0B1NiqjlWqZtE6cJ5CN'>Fairness Indicators and What-If Tool</a>

In this activity, you'll use Fairness Indicators to explore the [Civil Comments dataset](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification). Fairness Indicators is a suite of tools built on top of [TensorFlow Model Analysis](https://www.tensorflow.org/tfx/model_analysis/get_started) that enable regular evaluation of fairness metrics in product pipelines.

### <a target='#' href='../tfx_airflow/README.md'>Airflow and Jupyter</a>

This is a Docker image for running the [TFX Developer Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/workshop). It includes TensorFlow and TFX, and initializes a clean, basic environment for running the workshop.