#!/usr/bin/env bash

# Runs the dunamic experiments for LTG, PUG-long, PUG-Lookback
#
# This supposedly shows the complexity of the temporal aspect of the planning.

. ./common.bash

config() {
  file=$1
  cutoff=$2
  scale=$3

  set_kv ${file} risk-violation "${AZURE_COST}"
  set_kv ${file} criteria-time "cutoff-at-${!cutoff}"
  set_kv ${file} concurrent-switch-failure 0
  set_kv ${file} concurrent-switch-probability 0.001
  set_bw ${file} $(mult_int $(get_bw $file) $scale)

  echo -e "${cutoff}\t${cost}"
}

planners() {
  echo "ltg pug-long pug-lookback"
}

export -f planners
export -f config

parallel --eta --progress \
  executor experiments/02-paper-dynamic-traffic.ini\
  config planners\
  ::: NONE_TIME FIXED_TIME DEADLINE_TIME CRITICAL_TIME\
  ::: 0.8 0.9 1 1.1 1.2\
  column -t | sort -k1,1 -nk2,2 -nk3,3 | tee data/04-cost-time.log
