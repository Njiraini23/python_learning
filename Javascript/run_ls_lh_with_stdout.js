const { spawn } = require('node:child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.err(`stderr: ${err}`);
});

ls.on('close', (code) => {
  console.log(`The child process exited with code ${code}`);
});
