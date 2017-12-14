#!/bin/bash


#$ -N CYANG
#$ -j y
#$ -t 1-2

echo $SGE_TASK_ID
./helloworld.exe $SGE_TASK_ID
##sed -n ${SGE_TASK_ID}p input_argument.txt
