dataset=news
sup_source=keywords # keywords, docs, labels
model=cnn # rnn, cnn

export CUDA_VISIBLE_DEVICES=0

python3 main.py --dataset ${dataset} --sup_source ${sup_source} --model ${model} --with_evaluation False
