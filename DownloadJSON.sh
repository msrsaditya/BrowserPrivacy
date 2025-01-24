#!/bin/bash
base_url="https://privacytests.org"
files=("index" "private" "ios" "android" "nightly" "nightly-private")
for file in "${files[@]}"; do
    curl -O "$base_url/$file.json"
done
mkdir -p /Users/shashank/JSON
mv /Users/shashank/*.json /Users/shashank/JSON/
