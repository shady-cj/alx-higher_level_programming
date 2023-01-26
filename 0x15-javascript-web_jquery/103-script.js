$(function() {
    url = "https://www.fourtonfish.com/hellosalut/hello/"
    const btn = $("INPUT#btn_translate");
    const code = $("INPUT#language_code");
    const result = $("DIV#hello");
    $(btn).click(function() {
        $.ajax({
            url: url,
            type: "GET",
            data: { "lang": $(code).val() },
            dataType: "jsonp",
            crossDomain: true,
            success: function(data) {
                $(result).text(data.hello)
            }
        })
    })
    $(code).keyup(function(e) {
        if (e.keyCode == 13) {
            $.ajax({
                url: url,
                type: "GET",
                data: { "lang": $(code).val() },
                dataType: "jsonp",
                crossDomain: true,
                success: function(data) {
                    $(result).text(data.hello)
                }
            })
        }
    })
})