$(function() {
    const toggleHeader = $("#toggle_header");
    $(toggleHeader).click(function() {
        const $header = $("header")
        if ($header.hasClass('green')) {
            $header.removeClass("green")
            $header.addClass("red")
        } else if ($header.hasClass("red")) {
            $header.removeClass("red")
            $header.addClass("green")
        } else {
            $header.addClass("green")
        }
    })
})