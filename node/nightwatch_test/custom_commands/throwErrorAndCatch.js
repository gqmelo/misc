var wrapper = function(fn) {
  return function() {
    try {
      fn();
    } catch(err) {
      console.log(`Caught error: ${err}\n\n${err.stack}`);
      this.end(function() {
        throw Error('Caught error inside a custom command');
      }.bind(this));
    }
  }
}

exports.command = wrapper(function() {
  console.log('ThrowErrorAndCatch command');
  // This would not make the test fail: https://github.com/nightwatchjs/nightwatch/issues/1527
  // but the wrapper should catch and then make it fail.
  nonExisting;
  console.log('ThrowErrorAndCatch command ended');
});
