"""Includes model files from workshop notebook directory."""

import os

import numpy as np
import tensorflow as tf


_DERIVED_FMT = os.path.join(os.path.dirname(__file__), '%s.py') 

# convert_sparse() -- needed by make_input_fn_stroke()
execfile(_DERIVED_FMT % '4_convert_sparse', globals(), locals())
# make_input_fn_stroke()
execfile(_DERIVED_FMT % '4_input_fn_stroke', globals(), locals())

# get_nth() -- needed by get_logits_stroke()
execfile(_DERIVED_FMT % '4_get_nth', globals(), locals())
# get_logits_stroke()
execfile(_DERIVED_FMT % '4_get_logits_stroke', globals(), locals())
# make_model_fn()
execfile(_DERIVED_FMT % '4_make_model_fn', globals(), locals())


def build_estimator(model_dir, n_classes, params, config):
  model_fn = make_model_fn(get_logits_fn=get_logits_stroke, n_classes=n_classes)
  return tf.estimator.Estimator(model_fn=model_fn, model_dir=model_dir,
                                config=config)


def serving_input_fn():
  inputs = {
    'stroke': tf.placeholder(tf.float32, [None, 3, MAX_LEN]),
    'stroke_len': tf.placeholder(tf.int64, [None]),
  }
  return tf.estimator.export.ServingInputReceiver(inputs, inputs)

