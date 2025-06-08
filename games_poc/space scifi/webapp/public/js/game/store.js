import {load} from '/js/game/loader.js';

/**
 * Store
 *
 */
export let objects = {};

load(function() {
  fetch('/json/objects.json', {cache: 'force-cache'}).then((resp) => {
    return resp.json();
  }).then((resp) => {
    objects = resp;

    this.loaded();
  });
});
