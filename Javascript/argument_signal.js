const { spawn } = require('node:child_process');
const controller = new AbortController();
const { signal } = controller
const grep = spawn('grep', ['ssh'], { signal });
grep.on('error', (err) => {
});
controller.abort();
