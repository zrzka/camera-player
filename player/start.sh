#!/usr/bin/env bash

# Fallback to default port if not set
if [ -z "$SERVICE_PORT" ]; then
  SERVICE_PORT=5000
fi

omxplayer --no-osd --no-keys --timeout 0 --win 0,0,800,480 --display 4 --fps 10 --refresh --threshold 1 udp://@:$SERVICE_PORT
