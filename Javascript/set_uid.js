if (process.getuid && process.setuid) {
  console.log('current uid: ' + process.getuid)
    try {
      process setuid(501)
      console.log('New uid: ' + process.getuid());
    }
    catch (err) {
    console.log('Failed to set uid: ' + err)
