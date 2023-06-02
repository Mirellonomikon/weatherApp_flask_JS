var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

// Listen for the search button being clicked
document.getElementById("search_button").addEventListener("click", function() {
    // Fetch the location from the search bar
    var location = document.getElementById("search_bar").value;

    // Emit a location event to the server
    socket.emit('location', {data: location});
});