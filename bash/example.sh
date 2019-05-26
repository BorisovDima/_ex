#!/bin/bash

echo $0 $1 $2  # script name and args command line

echo $$  #pid

exit_code=$?  # exit code
echo $exit_code


#condition operators

#if ls; then
if [ $exit_code = 1 ] || [ 1 -lt 0 ]; then # любая комана, проверяется только exit code
    echo 'ERROR'
elif [ $exit_code = 0 ] && [ 1 -gt 0 ]; then
    echo 'OK'
else
    echo 'Unexpected'
fi #close condition

# Циклы
for var in $(ls /); do
    echo $var
done

count=0

while [ $count -lt 5 ]; do
let count=$count+1
echo $count
done



exit 1 # exit with code 1
