#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

DIRS="cosmos cosmos_proto terra gogoproto google ibc tendermint"

for dir in $DIRS; do
  rm -rf "$dir"
  cp -R "./build/$dir" ./
done