exports.command = function() {
  const client = this;
  console.log('goToGoogle command');
  client
    .url('http://google.com')
    .expect.element('body').to.be.present.before(5000);
};
