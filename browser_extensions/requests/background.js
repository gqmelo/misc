function logURL(requestDetails) {
    console.log('Loading: ' + requestDetails.url);
    console.log(requestDetails);
    const startTime = performance.now();
    // Simulate a delay of 1s
    while ((performance.now() - startTime) < 1000) {
    }
}

// browser.webRequest.onBeforeRequest.addListener(
//     logURL,
//     { urls: ['<all_urls>'], types:['image'] },
//     ['blocking']
// );


function changeResponse(details) {
    let filter = browser.webRequest.filterResponseData(details.requestId);
    let decoder = new TextDecoder('utf-8');
    let encoder = new TextEncoder();

    filter.ondata = event => {
        let str = decoder.decode(event.data, { stream: true });
        console.log('CHANGING RESPONSE');
        console.log(str);
        //   str = str.replace(/Example/g, 'WebExtension Example');
        //   filter.write(encoder.encode(str));
        filter.write(encoder.encode('throw new Error('BLABLA')'));
        filter.disconnect();
    }

    return {};
}


browser.webRequest.onBeforeRequest.addListener(
    changeResponse,
    { urls: ['<all_urls>'], types: ['script'] },
    ['blocking']
);


function setStatusCode(e) {
    console.log('SETTING STATUS CODE');
    console.log(e);
    // IT DOESN'T WORK
    e.statusCode = 200;
    e.statusLine = 'HTTP/1.1 200 OK';
    return { responseHeaders: e.responseHeaders };
}

// browser.webRequest.onHeadersReceived.addListener(
//     setStatusCode,
//     { urls: ['<all_urls>'], types: ['script'] },
//     ['blocking', 'responseHeaders']
// );
