#!/usr/local/bin/bash
SD=$(dirname $0)
HOST_PORT="localhost 8080"
jython server.py $HOST_PORT &
echo Waiting for server to start...
until kill -0 $(cat $SD/pid) 2>/dev/null
do
    sleep 1
done    
echo Server started...
function kill_server() {
    kill $(cat $SD/pid)
    rm $SD/pid
}
trap kill_server INT
trap kill_server EXIT
python client.py $HOST_PORT