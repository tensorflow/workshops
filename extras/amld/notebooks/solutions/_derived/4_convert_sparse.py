# (Written into separate file for sharing with clode code.)

# Now let's define a helper function that limits variable length
# sparse tensors to a maximum length and converts them to dense
# tensors. We need to convert sparse tensors to dense tensors before
# we can use them as input in the recurrent neural network.

def convert_sparse(sparse, max_len):
    """Converts batched sparse tensor to dense tensor with specified size.
    
    Args:
      sparse: tf.SparseTensor instance of shape=[n].
      max_len: Truncates / zero-pads the dense tensor the specified max_len.
    """
    # Convert to dense tensor.
    dense = tf.sparse_to_dense(sparse.indices, sparse.dense_shape,
                               sparse.values)
    # Discard values above max_len.
    dense = dense[:max_len]
    # Zero-pad if length < max_len.
    dense = tf.pad(dense, [[0, max_len - tf.shape(dense)[0]]])
    return dense