$(function() {
    const url = "https://swapi-api.alx-tools.com/api/films/?format=json"
    $("ul#list_movies").load(url, function(jsonString, status, xhr) {
        $("ul#list_movies").text("")
        const results = JSON.parse(jsonString).results;
        $.each(results, function(index, result) {
            $("ul#list_movies").append(`<li>${result.title}</li>`)
        })

    })
})