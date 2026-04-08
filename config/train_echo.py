# WhiteRock - Optimized for small dataset

out_dir = 'out-whiterock'
eval_interval = 250
eval_iters = 200
log_interval = 10

always_save_checkpoint = False
wandb_log = False
wandb_project = 'whiterock'
wandb_run_name = 'whiterock-v1'

dataset = 'echo'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 128

# WhiteRock architecture (smaller = better for this data)
n_layer = 4
n_head = 4
n_embd = 256
dropout = 0.1

learning_rate = 5e-4
max_iters = 3000
lr_decay_iters = 3000
min_lr = 5e-5
beta2 = 0.99
warmup_iters = 100
