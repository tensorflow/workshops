# Cloud Models

The packages in this directory wrap the code from the workshop notebooks so they
can be run via `tf.estimator.train_and_evaluate()`.


Running model locally (execute below commands in this directory after
generating data; see `../notebooks/solutions/1_qd_data.py`):

```bash
DATASET='../notebooks/data/dataset_img'
PYTHONPATH=. python -m trainer_cnn.task \
           --job-dir=/tmp/models/cnn1 \
           --n-classes=10 \
           --train-files="${DATASET}/train-*" \
           --eval-files="${DATASET}/eval-*"

DATASET='../notebooks/data/dataset_stroke'
PYTHONPATH=. python -m trainer_rnn.task \
           --job-dir=/tmp/models/rnn1 \
           --n-classes=10 \
           --train-files="${DATASET}/train-*" \
           --eval-files="${DATASET}/eval-*"
```

Running code on Cloud ML : see `../notebooks/solutions/5_qd_cloud.ipynb`.

