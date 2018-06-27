"""Includes model files from workshop notebook directory."""

import os

import tensorflow as tf
import numpy as np

_DERIVED_FMT = os.path.join(os.path.dirname(__file__), '%s.py') 

# make_input_fn_stroke()
exec(open(_DERIVED_FMT % '4_input_fn_img').read(), globals(), locals())

# get_logits_img()
exec(open(_DERIVED_FMT % '4_get_logits_img').read(), globals(), locals())
# make_model_fn()
exec(open(_DERIVED_FMT % '4_make_model_fn').read(), globals(), locals())


feature_columns = [
    # Add a feature column of numeric type and correct shape for the "img_64" feature.
    tf.feature_column.numeric_column('img_64', shape=(64, 64), dtype=tf.int64)
]


def create_estimator(config, params):
  model_fn = make_model_fn(
      get_logits_fn=get_logits_img, n_classes=params.n_classes)
  return tf.estimator.Estimator(model_fn=model_fn, model_dir=config.model_dir,
      config=config)

