$(function() {
    const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
    $("div#character").load(url, function(jsonString, status, xhr) {
        $("div#character").text(JSON.parse(jsonString).name)
    })
})