# (Written into separate file for sharing between notebooks.)

# Convert drawing tf.train.Example proto.
# Uses json_to_stroke() from previous cell to create raster image.

def make_example_stroke(label, drawing):
    example = tf.train.Example()
    example.features.feature['label'].int64_list.value.append(label)
    stroke = json_to_stroke(drawing)
    example.features.feature['stroke_x'].float_list.value.extend(stroke[0, :])
    example.features.feature['stroke_y'].float_list.value.extend(stroke[1, :])
    example.features.feature['stroke_z'].float_list.value.extend(stroke[2, :])
    example.features.feature['stroke_len'].int64_list.value.append(stroke.shape[1])
    example.features.feature['countrycode'].bytes_list.value.append(drawing['countrycode'].encode())
    example.features.feature['recognized'].int64_list.value.append(drawing['recognized'])
    example.features.feature['word'].bytes_list.value.append(drawing['word'].encode())
    ts = drawing['timestamp']
    ts = time.mktime(time.strptime(ts[:ts.index('.')], '%Y-%m-%d %H:%M:%S'))
    example.features.feature['timestamp'].int64_list.value.append(long(ts))
    example.features.feature['key_id'].int64_list.value.append(long(drawing['key_id']))
    return example