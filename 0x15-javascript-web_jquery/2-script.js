$(
    function() {
        const redHeader = $("#red_header");
        $(redHeader).click(function() {
            $("header").css(
                "color",
                "red"
            )
        })
    }
)