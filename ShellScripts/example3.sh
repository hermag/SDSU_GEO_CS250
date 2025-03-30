#!/bin/bash
echo "Provide the value of the first integer number - x"
read x
echo "Provide the value of the second integer number - y"
read y
if [ $x -gt $y ]
then
echo x is greater than y
elif [ $x -lt $y ]
then
echo x is less than y
elif [ $x -eq $y ]
then
echo x is equal to y
else
echo very strange situation
fi
