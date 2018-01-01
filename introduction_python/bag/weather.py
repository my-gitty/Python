from source import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outkook in enumerate(weekly.forecast(), 1):
	print(number, outkook)

