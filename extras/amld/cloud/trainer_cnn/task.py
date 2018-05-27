r"""Standalone executable wrapping tf.estimator.train_and_evaluate().

This program passes parameters from the command line to the estimator via a
tf.contrib.training.HParams object. This mechanism can both be used to define
parameters passed on to the model, as well as parameters used to set up the
TrainSpec and EvalSpec.

Example command for running locally (executed in parent directory; note that
you first need to run the ../notebooks/solutions/1_qd_data.ipynb notebook to
generate the data):

DATASET='../notebooks/data/dataset_img'
PYTHONPATH=. python -m trainer_cnn.task \
    --job-dir=/tmp/models/cnn1 \
    --n-classes=10 \
    --train-files="${DATASET}/train-*" \
    --eval-files="${DATASET}/eval-*"

Example command for running on Google Cloud using Cloud ML (note that you need
to replace the GCS_MODEL_DIR with some bucket where you have write access):

GCS_MODEL_DIR='gs://amld-models'
JOB_NAME='amld_cnn_1'
GCS_JOB_DIR="${GCS_MODEL_DIR}/models/${JOB_NAME}"
DATASET='gs://amld-datasets/zoo_img'
gcloud ml-engine jobs submit training $JOB_NAME \
    --region=us-east1 \
    --scale-tier=standard-1 \
    --runtime-version=1.7 \
    --job-dir=$GCS_JOB_DIR \
    --module-name=trainer_cnn.task --package-path=trainer_cnn/ \
    -- \
    --n-classes=10 \
    --train-files="${DATASET}/train-*" \
    --eval-files="${DATASET}/eval-*"

For more information abour runninbg on Cloud ML refer to this blog post:
https://cloud.google.com/blog/big-data/2018/02/easy-distributed-training-with-tensorflow-using-tfestimatortrain-and-evaluate-on-cloud-ml-engine
"""

import argparse

import tensorflow as tf

from . import model


def make_serving_input_fn():
  """Returns an inpt_fn for serving."""
  def serving_input_fn():
    example_tensor = tf.placeholder(shape=[None], dtype=tf.string)
    features = tf.parse_example(example_tensor, model.feature_spec)
    return tf.estimator.export.ServingInputReceiver(
            # Features expected by the model.
            features=features,
            # Default serving signatures expects to parse tf.Example.
            receiver_tensors={'example_proto': example_tensor},
            # Alternative serving signature to directly pass in features.
            # (optional)
            receiver_tensors_alternatives={'features': features})
  return serving_input_fn


def run_experiment(params):
  """Runs estimator returned by model.create_estimator()."""

  # Set up TrainSpec.
  train_input_fn = model.make_input_fn(
          files_pattern=params.train_files, batch_size=params.batch_size)
  train_spec = tf.estimator.TrainSpec(
          input_fn=train_input_fn,
          max_steps=params.train_steps)

  # Set up EvalSpec.
  eval_input_fn = model.make_input_fn(
          files_pattern=params.eval_files, batch_size=params.batch_size)
  final_exporter = tf.estimator.FinalExporter(
          'final', make_serving_input_fn())
  eval_spec = tf.estimator.EvalSpec(
          input_fn=eval_input_fn,
          steps=params.eval_steps,
          exporters=[final_exporter])

  # Train and evaluate.
  run_config = tf.estimator.RunConfig()
  run_config = run_config.replace(model_dir=params.job_dir)
  estimator = model.create_estimator(run_config, params)
  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument(
      '--job-dir', help='Model directory (local or on GCS).',
      required=True)
  parser.add_argument(
      '--n-classes', help='Number of classes.', type=int, required=True)
  parser.add_argument(
      '--train-files', help='Training file pattern (local or on GCS).',
      required=True)
  parser.add_argument(
      '--eval-files', help='Evaluation file pattern (local or on GCS).',
      required=True)
  parser.add_argument(
      '--train-steps', help='Training steps.', type=int, default=1000)
  parser.add_argument(
      '--eval-steps', help='Evaluation steps.', type=int, default=1000)
  parser.add_argument(
      '--batch-size', help='Batch size.', type=int, default=64)

  args = parser.parse_args()
  tf.logging.set_verbosity('INFO')

  hparams = tf.contrib.training.HParams(**args.__dict__)
  run_experiment(hparams)

