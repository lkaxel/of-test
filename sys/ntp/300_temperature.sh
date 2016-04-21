#!/bin/bash
ts=`date +%s`
host=$HOSTNAME
core_total=(`sensors | grep Core | awk -F '[+°]' '{print $2}'`)
#echo ${core_total[*]}
let x=${#core_total[*]}-1
echo -e "[\c"
for ((i=0;i<x;i++))
do
echo -e "{\"metric\": \"cpu-tempetature-$i\", \"endpoint\": \"$host\", \"timestamp\": $ts,\"step\": 300,\"value\": ${core_total[$i]},\"counterType\": \"GAUGE\",\"tags\": \"\"}, \c"
done
i=$x
echo -e "{\"metric\": \"cpu-tempetature-$i\", \"endpoint\": \"$host\", \"timestamp\": $ts,\"step\": 300,\"value\": ${core_total[$i]},\"counterType\": \"GAUGE\",\"tags\": \"\"}]"



