#!/bin/bash
docker build -t wellness-api . && docker run -d --restart unless-stopped -p 8000:8000 wellness-api
