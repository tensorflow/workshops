# (Written into separate file for sharing between notebooks.)

# Convert stroke coordinates into normalized relative coordinates,
# one single list, and add a "third dimension" that indicates when
# a new stroke starts.

def json_to_stroke(d):
    norm = lambda x: (x - x.min()) / max(1, (x.max() - x.min()))
    xy = np.concatenate([np.array(s, dtype=np.float32) for s in d['drawing']], axis=1)
    z = np.zeros(xy.shape[1])
    if len(d['drawing']) > 1:
        z[np.cumsum(np.array(map(lambda x: x.shape[1], d['drawing'][:-1])))] = 1
    dxy = np.diff(norm(xy))
    return np.concatenate([dxy, z.reshape((1, -1))[:, 1:]])