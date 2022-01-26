function doCapture() {
    html2canvas(document.getElementById("generatedimg")).then(function (canvas){console.log(canvas.toDataURL("image/jpg"),0.99);
});
}