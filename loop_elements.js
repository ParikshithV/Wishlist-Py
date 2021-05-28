const cheerio = require('cheerio');
const request = require('request');

request({
    method: 'GET',
    url: 'http://localhost:8000'
}, (err, res, body) => {

    if (err) return console.error(err);

    let $ = cheerio.load(body);

    let hobbies = [];

    $('li').each(function (i, e) {
        hobbies[i] = $(this).text();
    });

    console.log(hobbies);
});