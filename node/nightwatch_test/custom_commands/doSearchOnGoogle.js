exports.command = function() {
  const client = this;
  console.log('doSearchOnGoogle command');

  client.setValue('input[type=text]', ['nightwatch', client.Keys.ENTER])
    .waitForElementPresent('#main')
    .assert.containsText('#main', 'Night Watch');
};
