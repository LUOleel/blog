$(function () {

    let $img = $(".form-item .captcha-graph-img img");//这里不同的类之间有个空格
    genre();
    $img.click(genre);
    function genre() {
        let sImageCodeId = generateUUID()
        let imageCodeurl = '/image_code/'+sImageCodeId+'/';
        $img.attr('src',imageCodeurl)
    }

    // 生成图片UUID验证码
    function generateUUID() {
    let d = new Date().getTime();
    if (window.performance && typeof window.performance.now === "function") {
        d += performance.now(); //use high-precision timer if available
    }
    let uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        let r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
  }

})