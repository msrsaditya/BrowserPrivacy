#!/bin/bash
base_url="https://privacytests.org"
files=("index" "private" "ios" "android" "nightly" "nightly-private")
mkdir -p ~/JSON
for file in "${files[@]}"; do
    curl -s -o ~/JSON/"$file.json" "$base_url/$file.json"
done
