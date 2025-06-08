import {objects} from '/js/game/store.js';
import {planets, sizes} from '/js/gfx/icons.js';

let canvas, ctx;
let view = 'top_down';

export function init_gfx() {
  $("#app-map").innerHTML = "<button id='view_switch' class='btn btn-brand'>Side view</button><canvas id='canvas'></canvas>";

  $("#view_switch").onclick = function() {
    if (view == 'top_down') {
      view = 'side';
      $("#view_switch").innerHTML = 'Orbital view';
    } else {
      view = 'top_down';
      $("#view_switch").innerHTML = 'Side view';
    }

    update_model();
    draw();
  }

  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");

  window.addEventListener('resize', resize, false);
  resize();
}

function update_model() {

  const max_r = objects.reduce(function(prev, current) {
    return (prev.r > current.r) ? prev : current
  }).r;
  const min_r = 0; // sun (or mercury?)

  // scaler: 90% of width / height
  const S = 0.9 * Math.min(canvas.width, canvas.height)/2;
  const RN = (1/max_r) * 1000;

  for (let object of objects) {
    // apply log scale for radius
    let R = Math.log(object.r*RN - min_r) / Math.log(max_r*RN - min_r);

    if (R < 0)
      R = 0;

    // we ignore latitude, as it's a top-down view!
    object.or = R*S;

    if (view == 'top_down') {
      // ox, oy = polar(x, R)
      object.ox = object.or * Math.cos(object.x) * Math.cos(object.y);
      object.oy = object.or * Math.sin(object.x) * Math.cos(object.y);
    } else {
      // ox, y = polar(y, R);
      object.ox = object.or * Math.sin(object.x) * Math.cos(object.y);
      object.oy = object.or                      * Math.sin(object.y);
      //object.oy = object.or * Math.sin(object.x) * Math.cos(object.y);
    }
  }
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  ctx.setLineDash([5, 15]);
  ctx.strokeStyle = 'white';

  // draw orbital paths
  for (let object of objects) {
    if (object.name == "Sun")
      continue;

    let cx = canvas.width /2;
    let cy = canvas.height/2;

    if (view == 'top_down') {
      // top-down view orbitals
      ctx.beginPath();
      ctx.arc(cx, cy, object.or, 0, 2*Math.PI);
      ctx.closePath();
      ctx.stroke();
    } else {
      // side view orbitals
      //ctx.moveTo(cx-object.ox, cy-object.oy);
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx+object.ox, cy+object.oy);
      ctx.closePath();
      ctx.stroke();
    }
  }

  // draw planet images
  for (let object of objects) {
    let img = planets[object.name];
    let PLS = sizes[object.name];

    let cx = canvas.width /2 - PLS*img.width /2;
    let cy = canvas.height/2 - PLS*img.height/2;

    ctx.drawImage(img,
      0,0,img.width,img.height,
      cx+object.ox,cy+object.oy, PLS*img.width,PLS*img.height
    );
  }
}

export function resize() {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;

  update_model();
  draw();
}

