formatter = "%r, %r, %r, %r"

print formatter
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (
"I had this thing",
"That you could play",
"But it didn't sing",
"So I said goodnite."
)


h = 'hello %s' % 'peter, ivan, %s' % 'dirk'
peter = 3 is 21
print h
print peter
