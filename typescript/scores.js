const puppeteer = require('puppeteer');

async function startArray(page){
    await page.evaluate(() => {
        const starts = [];
        const startList = document.querySelectorAll("table.teams > td.yjSt");
        console.log(startList);
        startList.forEach(_start => {
            info = _start.innerText;
            if (info != "予告先発" && info != "戦評")
            starts.push(info);
        })
        return starts;
    });
}

(async() => {
    const browser = await puppeteer.launch({
        args: [
          '--no-sandbox',
          '--disable-setuid-sandbox'
        ]
    });
    const page = await browser.newPage();
    await page.goto('http://baseball.yahoo.co.jp/npb/schedule/');

    const starts = await startArray(page);
    starts.forEach(_start => {
        console.log(_start);
    })

    browser.close();
})();