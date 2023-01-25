$(function() {
    const url = "https://fourtonfish.com/hellosalut/?lang=fr"
    $.get(url, function(result) {
        $("div#hello").text(result.hello)
    })
})