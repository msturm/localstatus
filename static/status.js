function refreshStatus() {
    var statusField = $('#counter')


    $.getJSON('/status', function(statusJson) {
        var result = '<table>';
        var status_green = 'static/img/green-on-128.png'
        var status_red = 'static/img/red-on-128.png'
        
        for (var i = 0; i < statusJson.length; i++) {
            var service = statusJson[i];
            var status = status_green;
            if (service.status != 'RUNNING') {
                status = status_red;
            }
            result += '<tr><td>' + service.service + '</td><td><img src="' + status + '" height="12"></td></tr>' 
        }
        result += '</table>'; 
        statusField.empty();
        statusField.append(result); 
    });
}

window.setInterval(refreshStatus, 2000);
