# (Written into separate file for sharing with clode code.)

# Read input data from sharded files using 1.4 API.
# This is copied and slightly simplified from tf_snippets.ipynb

# Note that this cell simply defines the functions but does not yet call
# them. The functions are executed in the next cell within a tf.Graph()
# context.

# This dictionary specifies what "features" we want to extract from the
# tf.train.Example protos (i.e. what they look like on disk). We only
# need the image data "img_64" and the "label". Both features are tensors
# with a fixed length.
# You need to specify the correct "shape" and "dtype" parameters for
# these features...
feature_spec = {
    # Single label per example => shape=[1] (we could also use shape=() and
    # then do a transformation in the input_fn).
    'label': tf.FixedLenFeature(shape=[1], dtype=tf.int64),
    # The bytes_list data is parsed into tf.string.
    'img_64': tf.FixedLenFeature(shape=[64, 64], dtype=tf.int64),
}

def parse_example(serialized_example):
    # Convert string to tf.train.Example and then extract features/label.
    features = tf.parse_single_example(serialized_example, feature_spec)
    # Important step: remove "label" from features!
    # Otherwise our classifier would simply learn to predict
    # label=features['label']...
    label = features.pop('label')
    # Convert int64 [0..255] to float [0..1]
    features['img_64'] = tf.cast(features['img_64'], tf.float32) / 255.
    return features, label

# Common Tensorflow pattern : wrap function to specify parameters.
# The estimator interface expects a "input_fn" as a parameter, and not the
# tensors (features, labels) so it can re-create the tensors in different
# graphs later on.
def make_input_fn(files_pattern, batch_size=100):
    def input_fn():
        # Signature input_fn: () -> features=Dict[str, Tensor], labels=Tensor
        ds = tf.data.TFRecordDataset(tf.gfile.Glob(files_pattern))
        ds = ds.map(parse_example).batch(batch_size)
        ds = ds.shuffle(buffer_size=5*batch_size).repeat()
        features, labels = ds.make_one_shot_iterator().get_next()
        return features, labels
    return input_fn