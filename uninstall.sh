#!/bin/bash

sudo python setup.py install --record files.txt
cat files.txt | xargs sudo rm -rf
rm files.txt
