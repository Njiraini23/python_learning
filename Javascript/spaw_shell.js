const { exec } = require('node:child_process');

exec = ('"/path/to/test file/test.sh" arg1 arg2');
// double quotes are used so that the space in the path is not interpreted
// as a delimiter of multiple arguments.


exec('echo "The \\$HOME variable is $HOME"');
// The $HOME variable is escaped in the first instance, but in the second.
