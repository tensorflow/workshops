# (Written into separate file for sharing with clode code.)

# Another helper function: This function will return the "nth element"
# with different "n" for every element in the batch.
# We will later need this function to get the prediction in the output
# of the dynamic_rnn.

def get_nth(tensor, ns, last_dim):
    """Tensor has shape [batch_size, max_len, last_dim]."""
    shape = tf.shape(tensor)
    batch_size, max_len = shape[0], shape[1]
    # Flatten first two dimensions.
    tensor = tf.reshape(tensor, [-1, last_dim])
    # Calculate indices within flattened tensor.
    idxs = tf.range(0, batch_size) * max_len + (tf.cast(ns, tf.int32) - 1)
    # Return nth elements.
    # TODO get rid of error UserWarning : https://stackoverflow.com/questions/35892412
    return tf.gather(tensor, idxs)