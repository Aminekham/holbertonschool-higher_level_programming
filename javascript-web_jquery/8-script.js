$(document).ready(function() {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    all = data.results;
    for(let i = 0; i < all.length; i++) {
      $('UL#list_movies').append('<li>' + all[i].title + '</li>');
    }
  })
})
