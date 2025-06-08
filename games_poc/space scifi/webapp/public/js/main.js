import {init_gfx} from '/js/gfx/render2D.js';
import {load, onload} from '/js/game/loader.js';
//import {client} from '/js/game/client.js';
//import {rules,countries,units, match} from '/js/game/store.js';


export function init_app(debug, ws_address, user, token) {

  onload((ctx)=>{
    init_gfx();
  });

  if (debug) {
    //window.map = map;
    //window.client = client;
  }

//  load(function() {
//    fetch('/client/load').then((resp)=>{
//      return resp.json();
//    }).then((resp)=>{
//      this.ctx.iso = resp.iso;
//      this.ctx.world = resp.world;
//
//      this.loaded();
//   });
//  });
//
//  onload((ctx) => {
//    console.info("Game loaded");
//
//    init_game(ctx);
//    init_features(ctx);
//    init_test();
//  });
}