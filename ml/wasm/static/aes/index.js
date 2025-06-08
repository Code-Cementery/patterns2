// export { default as aes128 } from './aes128.js';
// export { default as aes192 } from './aes192.js';
// export { default as aes256 } from './aes256.js';


import {glue, createEnv} from './glue.js';

let wasmBinaryFile = '/get_wasm';
let TOTAL_STACK = 5242880;
let TOTAL_MEMORY = 16777216;
let WASM_PAGE_SIZE = 65536;
let ASMJS_PAGE_SIZE = 16777216;


import {coerceArray as a} from "./utils.js";
export let coerceArray = a;

export function load_aes(callback) {

  // todo: temporal code
  fetch(wasmBinaryFile, {
    credentials: "same-origin"
  }).then(response => 
    response.arrayBuffer()
  ).then(bytes => 
    WebAssembly.compile(bytes)
  ).then(function(mod) {

    // console.log("Imports required:");    
    // for (let imp of WebAssembly.Module.imports(mod)) {
    //   console.log(imp)
    // }

    const env = {
      //memoryBase: 0,
      __memory_base: 0,
      memory: new WebAssembly.Memory({
        initial: 256,
        maximum: 256
      }),
      // tableBase: 0,
      // table: new WebAssembly.Table({
      //   initial: 0, element: 'anyfunc'
      // }),

      _memset: function(a,b,c) {
        console.log(a,b,c,this);
        a = 1;
      },
    };

    let imps = {
      'env': env

      // {
      //   "a": 0,
      //   "memory": new WebAssembly.Memory({
      //     "initial": TOTAL_MEMORY / WASM_PAGE_SIZE,
      //     "maximum": TOTAL_MEMORY / WASM_PAGE_SIZE
      //   }),
      // },
    };

    WebAssembly.instantiate(mod, imps).then(function(instance){

      // console.log(instance.exports);

      // let instance2 = {
      //   exports: {
      //     _aes_setkey_enc: function(){console.log('_aes_setkey_enc')},//instance.exports.b,
      //     _aes_setkey_dec: function(){console.log('_aes_setkey_dec')},//instance.exports.c,
      //     _aes_crypt_cbc: function(){console.log('_aes_crypt_cbc')},//instance.exports.d,
      //     _aes_crypt_ctr: function(){console.log('_aes_crypt_ctr')},//instance.exports.e,
      //   }
      // };

      callback(glue(instance, 256));
    });

  });
  
};

// WebAssembly.instantiateStreaming(fetch(file))
// .then(output => {
  
//   //console.log(output.instance.exports.a(72, -30));

//   console.log(output)
  
//   //let src = glue(wasmModule, 256);

// });



// todo: export key size & iv & generators
