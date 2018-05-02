var util = require('util');
var events = require('events');

function ThrowErrorAndCatch() {
  events.EventEmitter.call(this);
}

util.inherits(ThrowErrorAndCatch, events.EventEmitter);

ThrowErrorAndCatch.prototype.command = function(cb) {
  var self = this;

  console.log(`Number of errors: ${this.client.results.errors}`);
  // This does not work. The test still pass
  this.client.results.errors += 1;
  console.log(`Number of errors: ${this.client.results.errors}`);
  this.perform(function() {
    if (cb) {
      cb.call(self.client.api);
    }
    self.emit('complete');
    console.log(`Called complete`);
  });
  return this.client.api;
};

module.exports = ThrowErrorAndCatch;


