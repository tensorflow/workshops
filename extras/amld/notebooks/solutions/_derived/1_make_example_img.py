# (Written into separate file for sharing between notebooks.)

# Convert drawing tf.train.Example proto.
# Uses json_to_img() from previous cell to create raster image.

def make_example_img(label, drawing):
    example = tf.train.Example()
    example.features.feature['label'].int64_list.value.append(label)
    img_64 = np.asarray(json_to_img(drawing, img_sz=64, lw=4, maximize=True)).reshape(-1)
    example.features.feature['img_64'].int64_list.value.extend(img_64)
    example.features.feature['countrycode'].bytes_list.value.append(drawing['countrycode'].encode())
    example.features.feature['recognized'].int64_list.value.append(drawing['recognized'])
    example.features.feature['word'].bytes_list.value.append(drawing['word'].encode())
    ts = drawing['timestamp']
    ts = time.mktime(time.strptime(ts[:ts.index('.')], '%Y-%m-%d %H:%M:%S'))
    example.features.feature['timestamp'].int64_list.value.append(long(ts))
    example.features.feature['key_id'].int64_list.value.append(long(drawing['key_id']))
    return example