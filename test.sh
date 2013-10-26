#!/bin/bash

x=10000
for line in $(cat ./data/tags.tsv)
do
    if [ $x -eq 0 ];
    then
        exit
    fi
    echo "processing $line tag:"

    echo " -- preparing train data..."
    python prepare_vw_input.py $line ./data/train1.tsv ./tmp/current_vw_data.tmp
    echo " -- training model..."
    ~/vowpal_wabbit-6.1/vw -d ./tmp/current_vw_data.tmp -f ./models/model_$line.vw --loss_function logistic -b 26 --initial_weight 0.0 --quiet #-l $learningrate

    echo " -- testing model..."
    cat ./tmp/current_vw_data.tmp | ~/vowpal_wabbit-6.1/vw -t -i ./models/model_$line.vw -p ./tmp/vw_input.tmp --quiet
    echo " -- calculating border..."
    border=$(python evaluate_vw_output.py $line ./data/train1.tsv tmp/vw_input.tmp)

    echo " -- preparing test data..."
    python prepare_vw_input.py $line ./data/train2.tsv ./tmp/current_vw_data.tmp
    echo " -- generating results..."
    cat ./tmp/current_vw_data.tmp | ~/vowpal_wabbit-6.1/vw -t -i ./models/model_$line.vw -p ./tmp/vw_output.tmp --quiet
    python prepare_vw_output.py $border ./tmp/vw_output.tmp ./predictions/$line.pred

    let "x = x - 1"

    echo " -- calculating answer..."
    python test_answer.py ./data/train2.tsv
done
