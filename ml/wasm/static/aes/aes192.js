import wasmModule from './wasm/aes.wasm';
import glue from './glue.js';

export default glue(wasmModule, 192);