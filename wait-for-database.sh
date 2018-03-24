#!/bin/sh
set -e

host="$1"
shift
cmd="$@"

end="$((SECONDS+10))"
while true; do
    [[ "200" = "$(curl --silent --write-out %{http_code} --output /dev/null $host:7474)" ]] && break
    >&2 echo "$host not ready, waiting..."
    sleep 2
done
>&2 echo "$host is up"
exec $cmd