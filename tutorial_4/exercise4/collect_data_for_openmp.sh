#!/bin/bash

prblm_size=200
block_size=16
num_th=1
while [ "$num_th" -lt 35 ]
do
   export OMP_NUM_THREADS=$num_th
   ./parallelize.out $prblm_size $block_size
   num_th=`expr $num_th "*" 2 `
   prblm_size=`expr $prblm_size "*" 2 `
done
