#!/bin/bash
export OMP_NUM_THREADS=1
export KMP_AFFINITY="granularity=core,explicit,proclist=[0],verbose"
./stream_omp_l1_cache.o
./stream_omp_l2_cache.o
./stream_omp_l3_cache.o
