#!/bin/bash

[ ! -d ./unzipped_data  ] && mkdir ./unzipped_data

unzip ./data/*.zip ./unzipped_data
