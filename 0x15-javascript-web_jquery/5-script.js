$(function() {
    const addItem = $("div#add_item");
    $(addItem).on("click", function() {
        let newLi = $("<li>");
        $(newLi).text("item")
        $("ul.my_list").append(newLi)
    })
})