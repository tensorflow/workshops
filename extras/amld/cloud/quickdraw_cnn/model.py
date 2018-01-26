"""Includes model files from workshop notebook directory."""

import os

import tensorflow as tf
import numpy as np

_DERIVED_FMT = os.path.join(os.path.dirname(__file__), '%s.py') 

# make_input_fn_stroke()
execfile(_DERIVED_FMT % '4_input_fn_img', globals(), locals())

# get_logits()
execfile(_DERIVED_FMT % '4_get_logits_img', globals(), locals())
# make_model_fn()
execfile(_DERIVED_FMT % '4_make_model_fn', globals(), locals())


def build_estimator(model_dir, n_classes, params, config):
  model_fn = make_model_fn(get_logits_fn=get_logits_img, n_classes=n_classes)
  return tf.estimator.Estimator(model_fn=model_fn, model_dir=model_dir,
                                config=config)


def serving_input_fn():
  inputs = {'img_64': tf.placeholder(tf.float32, [None, 64, 64])}
  return tf.estimator.export.ServingInputReceiver(inputs, inputs)

