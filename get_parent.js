const cheerio = require('cheerio');
const request = require('request');

request({
    method: 'GET',
    url: 'http://localhost:8000'
}, (err, res, body) => {

    if (err) return console.error(err);

    let $ = cheerio.load(body);

    let h1El = $('h1');

    let parentEl = h1El.parent();

    console.log(parentEl.get(0).tagName)
});