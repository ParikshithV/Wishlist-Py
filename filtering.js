const cheerio = require('cheerio');
const request = require('request');

request({
    method: 'GET',
    url: 'http://localhost:8000'
}, (err, res, body) => {

    if (err) return console.error(err);

    let $ = cheerio.load(body);

    let allEls = $('*');

    let filteredEls = allEls.filter(function (i, el) {
        // this === el
        return $(this).children().length > 3;
    });

    let items = filteredEls.get();

    items.forEach(e => {
        console.log(e.name);
    });

});