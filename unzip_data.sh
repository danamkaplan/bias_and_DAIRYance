#!/bin/bash

[ ! -d ./unzipped_data  ] && mkdir ./unzipped_data

unzip ./data/Test.zip -d ./unzipped_data
unzip ./data/Train.zip -d ./unzipped_data

