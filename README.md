# factorial-digits

## About

This repository contains everything needed to build a docker container. The container once built will run a python3 script taking in a natural number. This script will calculate the factorial of that number and then print out the sum of the digits of the result.

## Build

To build this container navigate to the folder containing the dockerfile and factorial-digits.py and run:

### docker build -t factorial-digits .

## Run 

Once the build is complete run the container using:

### docker run --rm factorial-digits \<int\>  
  
  where \<int\> is a positive number to be inputted

## Dependencies
  
This script was written in python 3.9.0 and uses Numpy 1.21.0
