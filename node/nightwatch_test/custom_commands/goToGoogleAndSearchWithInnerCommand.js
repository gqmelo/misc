exports.command = function() {
  const client = this;
  console.log('goToGoogleAndSearchWithInnerCommand command');
  client
    .url('http://google.com')
    .expect.element('body').to.be.present.before(5000);

  client.doSearchOnGoogle();
};
