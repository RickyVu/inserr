#!/bin/bash

# Check if roscore is running
roscore_running=$(rosnode list | grep "/rosout" | wc -l)
if [ "$roscore_running" -eq 0 ]; then
    echo "roscore is not running"
    exit 1
fi

# Check if rosbridge_server is running
rosbridge_running=$(rosnode list | grep "/rosbridge_websocket" | wc -l)
if [ "$rosbridge_running" -eq 0 ]; then
    echo "rosbridge_server is not running"
    exit 1
fi

# If both are running, exit successfully
exit 0