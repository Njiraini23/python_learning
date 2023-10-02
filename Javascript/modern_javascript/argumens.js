function registerUser(user) {
	if (!user) {
		user = 'Bot';
	}
	return user + ' is registered';
}
console.log(registerUser())
