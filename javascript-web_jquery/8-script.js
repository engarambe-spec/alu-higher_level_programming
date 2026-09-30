$.get('https://swapi-api.alx-tools.com/api/films/', function (data) {
  data.results.forEach(function (movie) {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  });
});
