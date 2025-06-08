import glue from './glue.js';
import wasmModule from './wasm/aes.wasm';

export default glue(wasmModule, 128);