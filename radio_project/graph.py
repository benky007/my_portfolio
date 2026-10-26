import matplotlib.pyplot as plt

# Data for plotting
t = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
print(t)
s = [0, 10, 40, 20, 0, 0, 0, 0, 50, 40, 70, 10, 0]
print(s)

fig, ax = plt.subplots()
print(fig, ax)
ax.plot(t, s)

ax.set(xlabel='Distance (m)', ylabel='Logs (no.)',
       title='Distance graph')
ax.grid()

plt.show()
