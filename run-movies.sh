dataset=movies
sup_source=keywords # keywords, docs
model=cnn #cnn, rnn

export CUDA_VISIBLE_DEVICES=0

python3 main.py --dataset ${dataset} --sup_source ${sup_source} --model ${model} --with_evaluation False
