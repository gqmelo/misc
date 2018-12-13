module.exports = {
  'Demo test' : function (browser) {
    browser.classCommandWithoutEmitWithArchiver();
    browser.waitForElementPresent('something', 1000);
  }
};
