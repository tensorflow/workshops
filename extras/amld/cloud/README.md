# Cloud Models

The packages in this directory wrap the code from the workshop notebooks into
an experiment for training on Cloud ML.


Running model locally (execute below commands in this directory after
generating data; see `../notebooks/solutions/1_qd_data.py`):

```bash
PYTHONPATH=quickdraw_rnn python -m task \
    --output_dir=/tmp/quickdraw_rnn_$(date +%Y%m%d_%H%M) \
    --data_dir=../notebooks/data/dataset_stroke \
    --train_steps=1 \
    --eval_steps=1

PYTHONPATH=quickdraw_cnn python -m task \
    --output_dir=/tmp/quickdraw_cnn_$(date +%Y%m%d_%H%M) \
    --data_dir=../notebooks/data/dataset_img \
    --train_steps=1 \
    --eval_steps=1
```

Running code on Cloud ML : see `../notebooks/solutions/5_qd_cloud.ipynb`.

