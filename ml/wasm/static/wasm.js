

function load_wasm(file) {


  WebAssembly.instantiateStreaming(fetch(file))
  .then(output => {
    
    console.log(output.instance.exports.a(72, -30));
    
  });

}