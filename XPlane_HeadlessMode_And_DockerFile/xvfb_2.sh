#!/bin/bash                                                                     
pathToXplaneExecutableFile="$1"
xvfb-run --server-args=':1 -screen 0, 1024x768x16' "$pathToXplaneExecutableFile" > /dev/null &
