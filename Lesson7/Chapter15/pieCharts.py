import matplotlib.pyplot as plt

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
used = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('green','blue','yellow','orange', 'purple')

fig1, ax1 = plt.subplots()
ax1.pie(used, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Most popular image files")

plt.show()