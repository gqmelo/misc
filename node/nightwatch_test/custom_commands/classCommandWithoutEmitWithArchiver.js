const util = require('util');
const events = require('events');
const archiver = require('archiver');

function classCommandWithoutEmitWithArchiver () { 
  events.EventEmitter.call(this); 
}
util.inherits(classCommandWithoutEmitWithArchiver, events.EventEmitter);

classCommandWithoutEmitWithArchiver.prototype.command = function uploadLocalFile () {
  console.log('classCommandWithoutEmitWithArchiver start');
  const createArchive = () => {
    console.log('Creating archive');
    let zip = archiver('zip');
    zip
      .on('finish', () => {
        console.log('finish');
        this.emit('complete');
      });
    zip.file('missing_file', { name: 'filename' });
    zip.finalize();
  }

  createArchive();

  console.log('classCommandWithoutEmitWithArchiver end');
  return this;
}

module.exports = classCommandWithoutEmitWithArchiver;
