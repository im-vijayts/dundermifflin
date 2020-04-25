$('button').click(function() {
    $.ajax({
        type: 'GET',
        url: '/getHelp',
        success: function(response) {
            $('#quote').text(response.dialogue);
        }
    })
});