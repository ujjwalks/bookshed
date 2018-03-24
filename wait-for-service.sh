#!/bin/sh
set -e

host="$1"
port="$2"
shift
shift
cmd="$@"

until nc $host $port; do
  >&2 echo "$host not up sleeping..."
  sleep 2
done
>&2 echo "$host is up"
exec $cmd