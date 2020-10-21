var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/dnx9bh2s2sga8j6am1wa4cpnqgerjjjfvht7gw1qogx4qxzi/tinymce/5/tinymce.min.js";
script.referrerPolicy = "origin";
document.head.appendChild(script);

script.onload = function () {
  tinymce.init({
    selector: '#id_text'
  });
}