let dropArea = document.getElementById('drop-area')

;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
}

;['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false)
})

;['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false)
})

function highlight(e) {
  dropArea.classList.add('highlight')
}

function unhighlight(e) {
  dropArea.classList.remove('highlight')
}

dropArea.addEventListener('drop', handleDrop, false)

function handleDrop(e) {
  let dt = e.dataTransfer
  let files = dt.files

  handleFiles(files)
}

function handleFiles(files) {
  files = [...files]
  files.forEach(uploadFile)
  files.forEach(previewFile)
}


function uploadFile(file) {
  let url = 'fileshare.py'
  let formData = new FormData()

  formData.append('file', file)

  fetch(url, {
    method: 'POST',
    body: formData
  })
  .then(() => { console.log("upload done"); })
  .catch(() => { console.log("upload failed"); })
}


function previewFile(file) {
  let reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onloadend = function() {
    let img = document.createElement('img')
    img.src = reader.result
    document.getElementById('gallery').appendChild(img)
  }
}

function areasolid() {
    let x = document.getElementById('solid');
    let y = document.getElementById('powder');
    let z = document.getElementById('liquid');
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";
}

function areapowder() {
    let x = document.getElementById('solid');
    let y = document.getElementById('powder');
    let z = document.getElementById('liquid');
    y.style.display = "block";
    x.style.display = "none";
    z.style.display = "none";
}

function arealiquid() {
    let x = document.getElementById('solid');
    let y = document.getElementById('powder');
    let z = document.getElementById('liquid');
    z.style.display = "block";
    y.style.display = "none";
    x.style.display = "none";
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

function forpowder() {
    let x = document.getElementById('extendpowder');
    if(x.style.display==="block"){
      x.style.display = "none";
    }
    else{
    x.style.display = "block";
  }
}

function forliquid() {
    let x = document.getElementById('extendliquid');
    if(x.style.display==="block"){
      x.style.display = "none";
    }
    else{
    x.style.display = "block";
  }
}
