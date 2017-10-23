def maker(N):
	def action(x):
		return x**N
	return action

