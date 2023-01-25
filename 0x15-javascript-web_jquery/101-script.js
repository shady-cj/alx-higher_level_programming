$(function() {

    const addItem = $("div#add_item");
    const removeItem = $("div#remove_item");
    const emptyItems = $("div#clear_list");
    const listItems = $("ul.my_list");
    $(addItem).click(function() {
        $(listItems).append("<li>Item</li>")

    })
    $(removeItem).click(function() {
        let last = $(listItems).find("li:last-child");
        $(last).remove()
    })
    $(emptyItems).click(function() {
        $(listItems).empty()
    })
})