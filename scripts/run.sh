#!/bin/bash

docker run -it --name curlup-dev-container -v .:/backend -p 8000:8000 curlup-dev