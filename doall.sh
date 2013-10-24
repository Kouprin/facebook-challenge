#!/bin/bash

x=100
for line in $(cat ./data/tags.tsv)
do
    if [ $x -eq 0 ];
    then
        exit
    fi
    #line="content"
    echo "processing $line tag:"

    echo " -- preparing train data..."
    python prepare_vw_input.py $line ./data/Train.csv ./tmp/current_vw_data.tmp
    echo " -- training model..."
    ~/vowpal_wabbit-6.1/vw -d ./tmp/current_vw_data.tmp -f ./models/model_$line.vw --loss_function logistic -b 26 --initial_weight 0.0 #-l $learningrate

    #echo " -- testing model..."
    #cat ./tmp/current_vw_data.tmp | ~/vowpal_wabbit-6.1/vw -t -i ./models/model_$line.vw -p ./tmp/vw_output.tmp
    #python evaluate_vw_output.py $line ./data/Train.csv tmp/vw_output.tmp

    echo " -- preparing test data..."
    python prepare_vw_input.py $line ./data/Test.csv ./tmp/current_vw_data.tmp
    echo " -- generating results..."
    cat ./tmp/current_vw_data.tmp | ~/vowpal_wabbit-6.1/vw -t -i ./models/model_$line.vw -p ./tmp/vw_output.tmp
    python prepare_vw_output.py $(awk -F "\t" ' { if ($1 == "'$line'") print $3 } ' ./data/tags_popularity.tsv) ./tmp/vw_output.tmp ./predictions/$line.pred

    let "x = x - 1"
done
