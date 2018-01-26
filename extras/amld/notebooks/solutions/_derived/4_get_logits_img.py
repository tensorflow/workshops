# (Written into separate file for sharing with clode code.)

# Define a function that computes "logits" from features.
# The "logits" are unbound numbers that will be used as the
# input to the softmax function (which is basically a sigmoid
# function extended to more than two classes). The more positive
# a logit, the closer to one the corresponding probability that
# is the output of the softmax.
# https://en.wikipedia.org/wiki/Softmax_function

def get_logits_img(features, n_classes, mode, params):
    """Computes logits for provided features.

    Args:
      features: A dictionary of tensors that are the features
          and whose first dimension is batch (as returned by input_fn).
      n_classes: Number of classes from which to predict (i.e. the number
          of different values in the "labels" tensor returned by the
          input_fn).
      mode: A tf.estimator.ModeKeys.
      params: Hyper parameters: "convs" specifying the configuration of the
          convolutions, and "hidden" specifying the configuration of the
          dense layers after the convolutions.

    Returns:
      The logits tensor with shape=[batch, n_classes].
    """
    # The parameter "convs" specifies (kernel, stride, filters)
    # of successive convolution layers.
    convs = params.get('convs', ((10, 4, 32), (5, 4, 64)))
    # The parameter "hidden" specifies the number of neurons of
    # successive fully connected layers (after convolution).
    hidden = params.get('hidden', (256,))
    # The function tf.layers.conv2d expects the tensor to have format
    # [batch, height, width, channels] -- since our "img_64" tensor
    # has format [batch, height, width], we need to expand the tensor
    # to get [batch, height, width, channels=1].
    last_layer = tf.expand_dims(features['img_64'], axis=3)
    # We start with dims=width=height=64 and filters=channels=1 and then
    # successively reduce the number of dimensions while increasing the
    # number of filters in every convolutional/maxpooling layer.
    dim = 64
    filters = 1
    for kernel, stride, filters in convs:
        conv = tf.layers.conv2d(
            inputs=last_layer, filters=filters, kernel_size=[kernel, kernel],
            padding='same', activation=tf.nn.relu)
        last_layer = tf.layers.max_pooling2d(
            inputs=conv, pool_size=[stride, stride], strides=stride)
        dim /= stride
    # "Flatten" the last layer to get shape [batch, *]
    last_layer = tf.reshape(last_layer, [-1, filters * dim * dim])
    # Add some fully connected layers.
    for units in hidden:
        dense = tf.layers.dense(inputs=last_layer, units=units,
                                activation=tf.nn.relu)
        # Regularize using dropout.
        training = mode == tf.estimator.ModeKeys.TRAIN
        last_layer = tf.layers.dropout(inputs=dense, rate=0.4,
                                       training=training)
    # Finally return logits that is activation of neurons in last layer.
    return tf.layers.dense(inputs=last_layer, units=n_classes)