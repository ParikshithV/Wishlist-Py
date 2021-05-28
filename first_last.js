const cheerio = require('cheerio');
const request = require('request');

request({
    method: 'GET',
    url: 'http://localhost:8000'
}, (err, res, body) => {

    if (err) return console.error(err);

    let $ = cheerio.load(body);

    let main = $('main');

    let fel = main.children().first();
    let lel = main.children().last();

    console.log(fel.get(0).tagName);
    console.log(lel.get(0).tagName);
});