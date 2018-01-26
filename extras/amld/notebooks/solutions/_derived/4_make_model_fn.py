# (Written into separate file for sharing with clode code.)

# Warning : Boilerplate code cell...

# This cell defines a function that connects the "get_logits_fn"
# to the estimator interface and adds some useful output for our problem.
# By specifying different parameters, the same function can be reused
# in section 5 where we use a recurrent neural network to compute the
# logits.

def make_model_fn(get_logits_fn, n_classes):
    """Creates a model_fn.

    Args:
      get_logits_fn: Function that computes logits from features.
      n_classes: Number of classes.

    Returns:
      A model_fn to be used with an estimator.
    """

    def model_fn(features, labels, mode, params):
        """The model_fn is passed as an argument to the estimator.

        Args:
          features: Dictionary mapping feature names to feature tensors.
          labels: Optional labels (`None` during inference).
          mode: A `tf.estimator.ModeKeys`.
          params: Optional dictionary of hyper parameters.

        Returns:
          A `tf.estimator.EstimatorSpec`.
        """

        # Create logits from features using RNN.
        logits = get_logits_fn(features, n_classes=n_classes, mode=mode,
                               params=params)

        # Convert logits to probabilities.
        probabilities = tf.nn.softmax(logits)
        # Extract class with highest probability.
        predictions = tf.argmax(probabilities, axis=1)

        onehot_labels = loss = train_op = eval_metric_ops = None
        if labels is not None:
            onehot_labels = tf.one_hot(tf.squeeze(labels), n_classes)
            loss = tf.losses.softmax_cross_entropy(onehot_labels, logits)

        if mode == tf.estimator.ModeKeys.TRAIN:
            # Compute loss.
            global_step = tf.train.get_global_step()
            # Minimize.
            train_op = tf.train.AdamOptimizer().minimize(loss, global_step=global_step)
            tf.summary.scalar('loss', loss)
            # Output number of parameters for educational purposes.
            trainable_params = 0
            for var in tf.trainable_variables():
                tf.logging.info('Variable "%s" : %s.', var.name,
                                var.get_shape().as_list())
                trainable_params += np.prod(var.get_shape().as_list())
            tf.logging.info('Total params : %d.', trainable_params)

        if mode == tf.estimator.ModeKeys.EVAL:
            # Report accuracy when evaluating.
            eval_metric_ops = {
                'accuracy': tf.metrics.accuracy(labels, predictions),
            }

        return tf.estimator.EstimatorSpec(
            loss=loss,
            mode=mode,
            predictions={
                'probabilities': probabilities,
                'predictions': predictions,
            },
            export_outputs={
                'prediction': tf.estimator.export.PredictOutput(outputs={
                    'probabilities': probabilities,
                    'predictions': predictions,
                }),
            },
            train_op=train_op,
            eval_metric_ops=eval_metric_ops,
        )

    return model_fn