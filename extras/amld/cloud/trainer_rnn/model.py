"""Includes model files from workshop notebook directory."""

import os

import numpy as np
import tensorflow as tf


_DERIVED_FMT = os.path.join(os.path.dirname(__file__), '%s.py') 

# convert_sparse() -- needed by make_input_fn_stroke()
exec(open(_DERIVED_FMT % '4_convert_sparse').read(), globals(), locals())
# make_input_fn_stroke()
exec(open(_DERIVED_FMT % '4_input_fn_stroke').read(), globals(), locals())

# get_nth() -- needed by get_logits_stroke()
exec(open(_DERIVED_FMT % '4_get_nth').read(), globals(), locals())
# get_logits_stroke()
exec(open(_DERIVED_FMT % '4_get_logits_stroke').read(), globals(), locals())
# make_model_fn()
exec(open(_DERIVED_FMT % '4_make_model_fn').read(), globals(), locals())


def create_estimator(config, params):
  model_fn = make_model_fn(
      get_logits_fn=get_logits_stroke, n_classes=params.n_classes)
  return tf.estimator.Estimator(model_fn=model_fn, model_dir=config.model_dir,
      config=config)


def serving_input_fn():
  inputs = {
      'stroke': tf.placeholder(tf.float32, [None, 3, MAX_LEN]),
      'stroke_len': tf.placeholder(tf.int64, [None]),
      }
  return tf.estimator.export.ServingInputReceiver(inputs, inputs)

