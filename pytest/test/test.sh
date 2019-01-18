#!/bin/bash
echo "Holle World"
for file in `ls /etc`
do
    echo "print the file_name ${file} in /etc"
done

for file in $(ls /var)
do
    echo "print the file name ${file} in /etc"
done
