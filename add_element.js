const cheerio = require('cheerio');
const request = require('request');

request({
    method: 'GET',
    url: 'http://localhost:8000'
}, (err, res, body) => {

    if (err) return console.error(err);

    let $ = cheerio.load(body);

    let ulEl = $('ul');

    ulEl.append('<li>Travel</li>');

    let lis = $('ul').html();
    let items = lis.split('\n');

    items.forEach((e) => {
        if (e) {
            console.log(e.replace(/(\s+)/g, ''));
        }
    });
});