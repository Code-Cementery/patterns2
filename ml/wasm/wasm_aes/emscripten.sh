#!/bin/sh

cd /d/programs/emsdk/
./emsdk activate latest
source ./emsdk_env.sh

cd /d/dev/lauren/_dev/spikes/wasm/wasm_aes/

rm -rf src
mkdir src

#    -s SIDE_MODULE=1 \

emcc ./c/aes.c \
    -s WASM=1 \
    -O2 \
    -s "EXPORTED_FUNCTIONS=['_aes_setkey_dec', '_aes_setkey_enc', '_aes_crypt_cbc', '_aes_crypt_ctr']" \
    -o ../static/aes/wasm/aes.js
