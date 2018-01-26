# (Written into separate file for sharing with clode code.)

# This function creates creates the logits fro the stroke features.
def get_logits_stroke(features, n_classes, mode, params):
    """Computes logits for provided features.

    Args:
      features: A dictionary of tensors that are the features
          and whose first dimension is batch (as returned by input_fn).
      n_classes: Number of classes from which to predict (i.e. the number
          of different values in the "labels" tensor returned by the
          input_fn).
      mode: A tf.estimator.ModeKeys.
      params: Hyper parameters: "cell_size" specifying the state size of
          the LSTM cells, and "hidden" specifying the configuration of the
          dense layers after recurrent network.

    Returns:
      The logits tensor with shape=[batch, n_classes].
    """

    cell_size = params.get('cell_size', 256)
    hidden = params.get('hidden', ())
    
    # First we convert our data from "coords major" to "time major",
    # as required by the dynamic_rnn API.
    # [batch, coords, time] -> [batch, time, coords]
    stroke = tf.transpose(features['stroke'], perm=[0, 2, 1])
    stroke_len = features['stroke_len']

    # Construct a bi-directional dynamic recurrent NN with LSTM
    # cells.
    outputs, states = tf.nn.bidirectional_dynamic_rnn(
            cell_fw=tf.nn.rnn_cell.LSTMCell(cell_size),
            cell_bw=tf.nn.rnn_cell.LSTMCell(cell_size),
            inputs=stroke,
            sequence_length=stroke_len,
            dtype=tf.float32,
    )
    # Use helper function from last cell to extract RNN output values.
    outputs = tf.concat((get_nth(outputs[0], stroke_len, last_dim=cell_size),
                         get_nth(outputs[1], stroke_len, last_dim=cell_size)),
                        axis=1)

    # Add fully connected layers on top.
    for units in hidden:
        outputs = tf.layers.dense(inputs=outputs, units=units,
                                  activation=tf.nn.relu)

    # Logits are activations of last fully connected layer.
    return tf.layers.dense(inputs=outputs, units=n_classes)