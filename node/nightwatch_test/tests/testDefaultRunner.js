module.exports = {
  'Demo test' : function (browser) {
    browser.windowHandles(function(result) {
      var handle = result.value[999];
      console.log('Switching to window');
      browser.switchWindow(handle);
      console.log('Switched window!');
    });
  }
};
