#!/bin/bash

[ ! -d ./unzipped_data  ] && mkdir ./unzipped_data

unzip ./data/Test.zip ./unzipped_data
unzip ./data/Train.zip ./unzipped_data

