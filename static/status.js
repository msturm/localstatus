function refreshStatus() {
    var oldStatus = {};
    var statusField = $('#counter');
    var logField = $('#log');

    return function() { 
        $.getJSON('/status', function(statusJson) {
            var status_green = 'static/img/green-on-128.png'
            var status_red = 'static/img/red-on-128.png'

            var result = '<table>';
            for (var i = 0; i < statusJson.length; i++) {
                var service = statusJson[i];
                var serviceName = service.service;
                var status = status_green;

                if (service.status !== 'RUNNING') {
                    status = status_red;
                }
                
                if (oldStatus[serviceName] !== undefined && oldStatus[serviceName] !== service.status) {
                    notify(serviceName, service.status);
                    logField.append('<div>' + new Date().toLocaleTimeString() + " - " + serviceName + ' changed from ' + oldStatus[serviceName] + ' to ' + service.status + '</div>');   
                }
                oldStatus[serviceName] = service.status;
                result += '<tr><td>' + serviceName + '</td><td><img src="' + status + '" height="12"></td></tr>' 
            }
            result += '</table>'; 
            statusField.empty();
            statusField.append(result); 
        });
    }
}

function notify(serviceName, status) {
    var title;
    var message;
    if (status !== "RUNNING") {
        title = serviceName + " is not running anymore"; 
        message = serviceName + " is not running anymore, status is " + status;
    } else {
        title = serviceName + " is now running"; 
        message = serviceName + " is running";
    }
    notification = window.webkitNotifications.createNotification("", title, message);
    notification.show();
}

function requestNotificationPermission() {
    window.webkitNotifications.requestPermission();
}

$('#show-notifications').bind('click', requestNotificationPermission);
window.setInterval(refreshStatus(), 1000);

