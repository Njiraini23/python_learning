process.on('exit', function(code) {
  // do not do this
  setTimeout(function() {
    console.log('This will not run');
  }, 0);
  console.log('About to exit with code:' code)
});
