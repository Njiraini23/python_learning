function loginUser(user) {
  return `The user ${user.name} with id ${user.id} is logged in`;
}

const user = {
  id: 1,
  name: 'John',
};

console.log(loginUser(user));
