#!/bin/bash

#run: head -50 tags.tsv | xargs -n 1 ./doall.sh

tag=$1
echo $tag

echo $tag > current_tag.tmp
python prepare_vw_input.py 

~/vowpal_wabbit-6.1/vw -d current_vw_data.tmp -f model_$tag.vw --loss_function logistic -b 26 --initial_weight 0.0 #-l $learningrate
#cat current_vw_data.tmp | ~/vowpal_wabbit-6.1/vw -t -i model_$tag.vw -p vw_output_$tag.tmp

#python prepare_vw_output.py 
#python evaluate_vw_output.py 
