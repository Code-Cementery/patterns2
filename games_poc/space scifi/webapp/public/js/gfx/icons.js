import {load} from '/js/game/loader.js';

const planet_list = ['earth', 'venus', 'mars', 'saturn', 'mercury', 'jupiter', 'neptune', 'uranus', 'sun']

export const planets = {};

// Load icons
for (let planet of planet_list) {
  let plImg = new Image;
  planets[planet.title()] = plImg;
  plImg.src = `/img/planet/${planet}.png`;

  load(function() {
    plImg.onload = () => {
      this.loaded();
    };
  });
}

let S = 0.65;
let BS = 0.25;
let MS = 0.35;

export const sizes = {
  Sun: 12.0 *BS*S,
  Jupiter:  11.20  *BS*S,
  Saturn:  9.45 *BS*S,

  Uranus:  4.00 *MS*S,
  Neptune:  3.88 *MS*S,

  Earth:  1.00*S,
  Venus:  0.95*S,
  Mars:  0.53*S,
  Mercury:  0.38*S,
};