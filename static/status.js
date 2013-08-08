function refreshStatus() {
    var statusField = $('#counter')
    $.getJSON('/status', function(statusJson) {
        var result = '<table>';
        for (var i = 0; i < statusJson.length; i++) {
            var service = statusJson[i];
            result += '<tr><td>' + service.service + '</td><td>' + service.status + '</td></tr>' 
        }
        result += '</table>'; 
        statusField.empty();
        statusField.append(result); 
    });
}

window.setInterval(refreshStatus, 500);
