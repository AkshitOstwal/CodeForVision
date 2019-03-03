

function areasolid() {
  let a = document.getElementById('t1').classList;
  let b = document.getElementById('t2').classList;
  let x = document.getElementById('solid');
  let y = document.getElementById('powder');
  x.style.display = "block";
  y.style.display = "none";
  if (b.contains("bottom-border")) {

    b.remove("bottom-border");

  }

  a.toggle("bottom-border");

}

function areapowder() {
  let a = document.getElementById('t1').classList;
  let b = document.getElementById('t2').classList;
  let x = document.getElementById('solid');
  let y = document.getElementById('powder');
  y.style.display = "block";
  x.style.display = "none";
  if (a.contains("bottom-border")) {
   
    a.remove("bottom-border");
    
  }

  b.toggle("bottom-border");
}

function areacuboidal() {
  let a = document.getElementById('s1').classList;
  let b = document.getElementById('s2').classList;
  let x = document.getElementById('cuboidal');
  let y = document.getElementById('circular');
  x.style.display = "block";
  y.style.display = "none";
  if (b.contains("bottom-border2")) {
   
    b.remove("bottom-border2");
    
  }

  a.toggle("bottom-border2");
}

function areacircular() {
  let a = document.getElementById('s1').classList;
  let b = document.getElementById('s2').classList;
  let x = document.getElementById('cuboidal');
  let y = document.getElementById('circular');
  y.style.display = "block";
  x.style.display = "none";
  if (a.contains("bottom-border2")) {
   
    a.remove("bottom-border2");
    
  }

  b.toggle("bottom-border2");
}

function forphysical() {
  let x = document.getElementById('extendphysical');
  if(x.style.display==="block"){
    x.style.display = "none";
  }
  else{
    x.style.display = "block";
  }
}

function forchemical() {
  let x = document.getElementById('extendchemical');
  if(x.style.display==="block"){
    x.style.display = "none";
  }
  else{
    x.style.display = "block";
  }
}

