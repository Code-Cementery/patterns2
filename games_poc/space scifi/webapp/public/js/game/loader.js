
let to_load = 0;
let n_loaded = 0;
let _preload = [], _postload = [];

const ctx_obj = {

};

let loader_obj = {
  loaded: function() {
    n_loaded++;

    if (n_loaded >= to_load) {
      // pre onload
      for (let l of _preload)
        l(ctx_obj);

      // onload
      for (let l of _postload)
        l(ctx_obj);

      // clear loader's cache
      for (let key in ctx_obj)
        delete ctx_obj[key]
    }
  },

  before_loadend: function(fun) {
    _preload.push(fun);
  },

  after_loadend: function(fun) {
    _postload.push(fun);
  },

  ctx: ctx_obj
}

export function load(fun) {
  to_load++;

  fun.call(loader_obj);
};

export function onload(fun) {
  _postload.push(fun);
};

export function preload(fun) {
  _preload.push(fun);
};