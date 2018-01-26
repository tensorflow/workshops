# (Written into separate file for sharing with clode code.)

# Because the data is stored in a different format (strokes instead of pixels)
# we need a new input_fn.

# Maximum number of points in concatenated strokes.
MAX_LEN = 256

# Because every drawing has a different number of points, we use "VarLenFeature"
# and not "FixedLenFeature" for the stroke data. This will create
# "SparseTensor".
feature_spec = {
    'stroke_x': tf.VarLenFeature(dtype=tf.float32),
    'stroke_y': tf.VarLenFeature(dtype=tf.float32),
    'stroke_z': tf.VarLenFeature(dtype=tf.float32),
    'stroke_len': tf.FixedLenFeature([], tf.int64),
    'label': tf.FixedLenFeature([], tf.int64),
}

def parse_example_stroke(serialized_example):
    features = tf.parse_single_example(serialized_example, feature_spec)
    label = features.pop('label')

    # The we create a 'stroke' tensor with shape [3, MAX_LEN] where the first
    # dimension indicates whether the values are X, Y, or Z coordinates.
    stroke = tf.stack([
        convert_sparse(features['stroke_x'], max_len=MAX_LEN),
        convert_sparse(features['stroke_y'], max_len=MAX_LEN),
        convert_sparse(features['stroke_z'], max_len=MAX_LEN),
    ])

    # Also truncate the "stroke_len" to MAX_LEN if needed.
    stroke_len = tf.minimum(tf.cast(MAX_LEN, tf.int64), features['stroke_len'])

    return dict(stroke=stroke, stroke_len=stroke_len), label

# Copied from above Section "1.2 Reading the data using Tensorflow"
def make_input_fn_stroke(files_pattern, batch_size=100):
    def input_fn():
        dataset = tf.data.TFRecordDataset(tf.gfile.Glob(files_pattern))
        dataset = dataset.map(parse_example_stroke).batch(batch_size)
        dataset = dataset.shuffle(buffer_size=5*batch_size).repeat()
        features, labels = dataset.make_one_shot_iterator().get_next()
        return features, labels
    return input_fn