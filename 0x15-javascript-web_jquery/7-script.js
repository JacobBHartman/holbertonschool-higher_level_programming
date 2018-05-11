$(function() {
  $.get('https://swapi.co/api/people/5/?format=json', function(data) {
    $('#character').append(data['name'])
  });
});
