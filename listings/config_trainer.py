from trl import SFTConfig, SFTTrainer

args = SFTConfig(
    eval_strategy="steps",
    eval_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    neftune_noise_alpha=15,
    warmup_steps=15,
    num_train_epochs=2,
    learning_rate=5e-5,
    optim="adamw_8bit",
    lr_scheduler_type="cosine",
    max_seq_length=20000,
)