n = 42
f = 7.03
s = 'string cheese'

#---------------------------- the OLD methods ----------------------------#

print('%d %f %s' % (n, f, s))

# width is 10 and in right defaut
print('%10d %10f %10s' % (n, f, s))

# width is 10 and in left
print('%-10d %-10f %-10s' % (n, f, s))

# width is 10 and in left and has 4 bit after dot('.')
print('%-10.4d %-10.4f %-10.4s' % (n, f, s))

# the parameter of format set in the last
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))

#---------------------------- the OLD methods ----------------------------#



#---------------------------- the NEW methods ----------------------------#

print('{} {} {}'.format(n, f, s))

# set the parameter position
print('{2} {0} {1}'.format(n, f, s))

# use the name of parameter
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))

# use a dict
d = { 'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))

print('{0:d} {1:f} {2:s}'.format(n, f, s))


print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))

# width is 10 
print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))

#  in right
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))

# in left
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

# in center
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))

# four precision and int has no precision
print('{0:^10d} {1:^10.4f} {2:^10.4s}'.format(n, f, s))

# fill characters and pay attention to the position of '!'
print('{0:!^20s}'.format('BIG SALE'))

#---------------------------- the NEW methods ----------------------------#
