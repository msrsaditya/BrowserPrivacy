#!/bin/bash
base_url="https://privacytests.org"
files=("index" "private" "ios" "android" "nightly" "nightly-private")
for file in "${files[@]}"; do
    aria2c "$base_url/$file.json"
done
mv /Users/shashank/Movies/*.json /Users/shashank/
