const cheerio = require('cheerio');
const request = require('request');

request({
    method: 'GET',
    url: 'http://localhost:8000'
}, (err, res, body) => {

    if (err) return console.error(err);

    let $ = cheerio.load(body);

    let fpEl = $('h1 + p');
    let attrs = fpEl.attr();

    console.log(attrs);
});