$.get('https://swapi-api.alx-tools.com/api/people/5/', function (data) {
  $('#character').text(data.name);
});
