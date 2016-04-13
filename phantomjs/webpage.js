var pageUrl= 'http://www.zngirls.com/g/18214/'
var page = require('webpage').create();
page.open(pageUrl, function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        page.render('example2.png');
    }
    phantom.exit();
});