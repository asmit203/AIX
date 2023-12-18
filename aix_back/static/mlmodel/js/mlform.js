$(document).ready(function() {
    $('#predictButton').click(function() {
        $('#predictionForm').submit();
    });
    $('#predictionForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '',
            data: formData,
            dataType: 'json',
            success: function(response) {
                $('#predictionResult').html('<p>The predicted value is: ' + response.prediction + '</p>');
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});