#!/usr/bin/env bash

# Give it a chance to connect before checking
printf "Waiting for 15s before connection check...\n"
sleep 15

export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

# Choose a condition for running WiFi Connect according to your use case:

# 1. Is there a default gateway?
# ip route | grep default

# 2. Is there Internet connectivity?
# nmcli -t g | grep full

# 3. Is there Internet connectivity via a google ping?
# wget --spider http://google.com 2>&1

# 4. Is there an active WiFi connection?
iwgetid -r

if [ $? -eq 0 ]; then
    printf "Skipping WiFi Connect, active WiFi connection found\n"
else
    printf "Starting WiFi Connect, no active WiFi connection found\n"
    ./wifi-connect
fi

# Start your application here.
sleep infinity
