"""Experiment wrapper for training on Cloud ML."""

import argparse, glob, json, os

import tensorflow as tf

# From this package.
import model


def generate_experiment_fn(data_dir, train_batch_size, eval_batch_size,
                           train_steps, eval_steps, convs, hidden,
                           **experiment_args):
  """Returns experiment_fn for a CNN classifier.

  Args:
    data_dir: Where {train,eval}-* tf.train.Example datasets can be found.
    train_batch_size: Batch size during training.
    train_batch_size: Batch size during evaluation.
    train_steps: Number of training steps.
    eval_steps: Number of evaluation steps.
    convs: Convolution configuration as string (e.g.
        "[[kernel1, stride1, filters1], ...]").
    hidden: Number of units in hidden layers.
    experiment_args: Additional arguments when `tf.contrib.learn.Experiment`
        is instantiated.
  """

  classes = tf.gfile.Open('%s/labels.txt' % data_dir).read().splitlines()
  n_classes = len(classes)

  if convs:
    convs = json.loads(convs)
  params = tf.contrib.training.HParams(
      convs=convs,
      hidden=hidden,
  )
  config = tf.contrib.learn.RunConfig()

  def _experiment_fn(output_dir):
    return tf.contrib.learn.Experiment(
        model.build_estimator(output_dir, n_classes, params, config),
        train_input_fn=model.make_input_fn(
          files_pattern=os.path.join(data_dir, 'train-*'),
          batch_size=train_batch_size),
        eval_input_fn=model.make_input_fn(
          files_pattern=os.path.join(data_dir, 'eval-*'),
          batch_size=eval_batch_size),
        export_strategies=[
            tf.contrib.learn.utils.saved_model_export_utils.make_export_strategy(
                model.serving_input_fn,
                exports_to_keep=1)
        ],
        train_steps=train_steps,
        eval_steps=eval_steps,
        **experiment_args
        )
  return _experiment_fn


if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)

  parser = argparse.ArgumentParser()
  parser.add_argument(
          '--data_dir',
          help='GCS or local path to training data',
          required=True
          )
  parser.add_argument(
          '--train_batch_size',
          help='Batch size for training steps',
          type=int,
          default=100
          )
  parser.add_argument(
          '--eval_batch_size',
          help='Batch size for evaluation steps',
          type=int,
          default=100
          )
  parser.add_argument(
          '--train_steps',
          help='Steps to run the training job for.',
          type=int,
          default=10000
          )
  parser.add_argument(
          '--eval_steps',
          help='Number of steps to run evalution for at each checkpoint',
          default=100,
          type=int
          )
  parser.add_argument(
          '--output_dir',
          help='GCS location to write checkpoints and export models',
          required=True
          )
  parser.add_argument(
          '--job-dir',
          help='this model ignores this field, but it is required by gcloud',
          default='junk'
          )
  parser.add_argument(
          '--eval_delay_secs',
          help='How long to wait before running first evaluation',
          default=10,
          type=int
          )
  parser.add_argument(
          '--min_eval_frequency',
          help='Minimum number of training steps between evaluations',
          default=1,
          type=int
          )

  # Hyper parameters.
  parser.add_argument(
          '--convs',
          help=('Convolutional layer configuration: '
               '"[[kernel1, stride1, filters1], ...]'),
          default='[[10, 4, 32], [5, 4, 64]]',
          type=str
          )
  parser.add_argument(
          '--hidden',
          help='Units in hidden layers.',
          default=[256],
          nargs='+',
          type=int
          )

  args = parser.parse_args()
  arguments = args.__dict__

  # unused args provided by service
  arguments.pop('job_dir', None)
  arguments.pop('job-dir', None)

  output_dir = arguments.pop('output_dir')

  # Run the training job
  tf.contrib.learn.learn_runner.run(
      generate_experiment_fn(**arguments), output_dir)

