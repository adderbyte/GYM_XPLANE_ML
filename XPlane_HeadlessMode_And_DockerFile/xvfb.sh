#!/bin/bash
xvfb-run --server-args=':1 -screen 0, 1024x768x16' ./X-Plane-x86_64 > /dev/null &
