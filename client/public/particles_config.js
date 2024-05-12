var i=0; // counter
var xamp = window.innerWidth; // x-amplitude
var yamp = window.innerHeight; // y-amplitude
var numps = xamp * 0.2; // number of particles
var maxd = 200; // max distance between node connections
var particles = []; // particles container
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
startMove();
function startMove(){
  document.getElementById("myCanvas").width = window.innerWidth;
  document.getElementById("myCanvas").height = window.innerHeight;
  for (i=0; i<numps; i++) {
    particles.push(new Particle());
  }
  var interval = window.setInterval(function(){mover();}, 15);
}
function mover(){
  i++;
  ctx.clearRect(0,0, c.width, c.height);

  for (p=0; p+1 <numps; p++)
  {
    particles[p].xp = particles[p].origx + Math.sin(i*particles[p].xt+particles[p].origx)*xamp;
    particles[p].yp = particles[p].origy + Math.sin(i*particles[p].yt+particles[p].origy)*yamp;
    for (y=0; y+1 < numps; y++)
    {
      if (distance(particles[p], particles[y]) < maxd)
        connect(particles[p], particles[y], distance(particles[p], particles[y]));
    }
  }
}

function connect(p1, p2, d)
{
  ctx.beginPath();
  ctx.moveTo(p1.xp, p1.yp);
  ctx.lineTo(p2.xp, p2.yp);
  ctx.globalAlpha = (maxd-d)/(maxd*1.1);
  ctx.stroke();
}

function distance(v1, v2)
{
  var dist = (v1.xp-v2.xp)*(v1.xp-v2.xp) + (v1.yp-v2.yp)*(v1.yp-v2.yp);
  return Math.sqrt(dist);
}

function Particle()
{
  this.xp = 0;
  this.yp = 0;
  this.origx= Math.random()*80 + window.innerWidth/2.3;
  this.origy= Math.random()*60 + window.innerHeight/2.3;
  this.xt = Math.random()/300; // x speed
  this.yt = Math.random()/300; // y speed
}
