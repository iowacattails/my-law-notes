<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Law Notes Publisher</title>
<style>
  body{font-family:Arial;background:#111;color:#fff;margin:0;padding:10px 8px}
  .version{font-size:14px;color:#d4af37;text-align:center;margin-bottom:8px}
  .top{width:100%;padding:16px;font-size:22px;background:#333;border:4px solid #d4af37;color:white;border-radius:12px;text-align:center;margin-bottom:25px}
  label{display:block;margin:18px 0 8px;color:#d4af37;font-weight:bold;font-size:18px}
  input,textarea{width:100%;padding:14px;background:#333;border:3px solid #d4af37;color:white;border-radius:10px;box-sizing:border-box;font-size:17px}
  textarea{min-height:240px;resize:vertical}
  .tags{display:flex;flex-wrap:wrap;gap:12px;margin:15px 0 20px}
  .tag-btn{background:#444;padding:9px 16px;border-radius:25px;cursor:pointer;font-size:15px}
  .tag-btn.selected{background:#d4af37;color:#000;font-weight:bold}
  .header-box{width:100%;padding:12px;background:#333;border:3px solid #d4af37;color:#d4af37;border-radius:10px;font-size:18px;text-align:center;margin:20px 0}
  button{background:#d4af37;color:#000;font-weight:bold;padding:18px 36px;border:none;border-radius:12px;cursor:pointer;font-size:22px;margin:15px 6px}
  button:hover{background:gold}
  #preview{margin:30px -8px 0;padding:35px;background:#ffffe0;color:#000;border:4px solid #d4af37;border-radius:15px;display:block;font-size:18px;line-height:1.6}
  .stripe{background:repeating-linear-gradient(90deg,transparent,transparent 49px,#d4af37 49px,#d4af37 50px);padding:30px;border-radius:12px;margin:20px 0}
  .section{margin-top:50px;padding-top:30px;border-top:3px dashed #d4af37}
  .back{text-align:center;margin:60px 0 20px;font-size:20px}
  .back a{color:#d4af37;text-decoration:underline}
  .img-prev{max-width:100%;border-radius:12px;margin:20px 0;display:block}
</style>
</head>
<body>

<div class="version">VERSION 8.0 — FINAL + ALL v4.1 FEATURES (Dec 6 2025)</div>

<input type="text" id="page-title" class="top" placeholder="Page Title">

<div id="sections"></div>

<div style="text-align:center;margin:40px 0">
  <button onclick="addSection()">+ Add Another Section</button>
  <button onclick="publishAll()" style="background:gold;font-size:28px;padding:22px 70px">
    Publish All (Images + Note + Index)
  </button>
</div>

<div id="preview"></div>

<div class="back"><a href="index.html">Back to All Law Notes</a></div>

<script>
let sectionCount = 0;
const tagsList = ["Common Law","Trial by Jury","Natural Rights","Due Process","Magna Carta","Abrogation","Vattel","Locke"];

function addSection() {
  sectionCount++;
  const d = document.createElement('div');
  d.className = 'section';
  d.innerHTML = `
    <h2 style="color:#d4af37;text-align:center;margin-bottom:30px">Note Section ${sectionCount}</h2>
    <label>Tags (tap to select)</label>
    <div class="tags" id="tags${sectionCount}"></div>
    <input type="text" class="custom-tags" placeholder="Add custom tags, comma-separated">
    <div class="header-box" contenteditable="true">Section Header / Context</div>
    <label>Body of Note</label>
    <textarea class="content" placeholder="Write your full note here..."></textarea>
    <label>Add Image (auto-uploaded)</label>
    <input type="file" class="image" accept="image/*">
    <img class="img-prev" style="display:none">
    <label>Source (link or book)</label>
    <input type="text" class="source">
    <label>Citation (quote/reference)</label>
    <input type="text" class="citation">
  `;
  document.getElementById('sections').appendChild(d);

  const tagBox = d.querySelector(`#tags${sectionCount}`);
  tagsList.forEach(tag => {
    const btn = document.createElement('span');
    btn.className = 'tag-btn';
    btn.textContent = tag;
    btn.onclick = () => { btn.classList.toggle('selected'); previewAll(); };
    tagBox.appendChild(btn);
  });

  d.querySelectorAll('input, textarea, .header-box').forEach(el => el.oninput = previewAll);
  d.querySelector('.image').onchange = e => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = ev => {
        const prev = e.target.parentElement.querySelector('.img-prev');
        prev.src = ev.target.result;
        prev.style.display = 'block';
      };
      reader.readAsDataURL(file);
    }
    previewAll();
  };
}

function previewAll() {
  const title = document.getElementById('page-title').value.trim() || "Preview Note";
  let html = `<h1 style="text-align:center;color:#b8860b;text-shadow:0 0 12px gold;font-size:32px">${title}</h1>`;
  document.querySelectorAll('.section').forEach(sec => {
    const selected = Array.from(sec.querySelectorAll('.tag-btn.selected')).map(b => b.textContent);
    const custom = sec.querySelector('.custom-tags').value.split(',').map(t => t.trim()).filter(Boolean);
    const tags = [...selected, ...custom].join(' · ');
    const header = sec.querySelector('.header-box').innerText.trim();
    const body = sec.querySelector('.content').value.replace(/\n/g,'<br>');
    const img = sec.querySelector('.img-prev').style.display === 'block' ? sec.querySelector('.img-prev').outerHTML : '';
    const source = sec.querySelector('.source').value.trim();
    const citation = sec.querySelector('.citation').value.trim();

    if (tags) html += `<p style="text-align:center;color:#b8860b"><strong>${tags}</strong></p>`;
    if (header) html += `<h2 style="text-align:center;color:#d4af37">${header}</h2>`;
    html += `<div class="stripe">${body}${img}</div>`;
    if (source) html += `<p style="text-align:center">Source: <a href="${source}">${source}</a></p>`;
    if (citation) html += `<p style="text-align:center;font-style:italic">${citation}</p>`;
    html += '<hr style="border:1px dashed #d4af37">';
  });
  document.getElementById('preview').innerHTML = html;
}

document.addEventListener('input', previewAll);
document.addEventListener('change', previewAll);

addSection();
previewAll();
</script>
</body>
</html>
