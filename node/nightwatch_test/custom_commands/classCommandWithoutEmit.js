const util = require('util');
const events = require('events');

function classCommandWithoutEmit () { 
  events.EventEmitter.call(this); 
}
util.inherits(classCommandWithoutEmit, events.EventEmitter);

classCommandWithoutEmit.prototype.command = function uploadLocalFile () {
  const self = this;
  console.log('classCommandWithoutEmit start');
  // setTimeout(function() {self.emit('complete');}, 10);
  console.log('classCommandWithoutEmit end');
  return self;
}

module.exports = classCommandWithoutEmit;
