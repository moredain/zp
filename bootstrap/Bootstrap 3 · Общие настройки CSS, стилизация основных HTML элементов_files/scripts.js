$(document).ready(function(){ 
	randomBannerItem('.banners-nav');
	randomBannerItem('.banners-top');
	randomBannerItem('.banners-bottom');
	if (readCookie("adsShown1") == null) {
	    $("#adsModal").modal({show:true});
	    createCookie("adsShown1", "1", 365);
	}
});	

function createCookie(name, value, days) {
    var expires;

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}

function randomBannerItem(name){
	var max = $(name + ' .item').length - 1;
	var rand = Math.floor(Math.random() * (max + 1));
	$(name + ' .item').eq(rand).addClass('active');
}