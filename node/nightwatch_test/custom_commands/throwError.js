exports.command = function() {
  console.log('throwError command');
  // This does not fail the test: https://github.com/nightwatchjs/nightwatch/issues/1527
  nonExisting;
  console.log('throwError command ended');
};
