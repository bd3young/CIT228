import matplotlib.pyplot as plt

cubed=[]
raised=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num) 
    raised.append(num**2)


# Plot 1
ax1 = plt.subplot(1,2,1)
ax1.plot (inputVal, cubed, marker= 'o', c= 'purple', lw= '2.0', ls= ':')
plt.grid()
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")


# Plot 2
ax2 = plt.subplot(1,2,2)
plt.style.use("seaborn-poster")
ax2.plot(inputVal,raised, marker= 'o', c='green', lw= '2.0', ls= ':')
plt.grid()
plt.title("Numbers Raised")
plt.ylabel("Second Power")
plt.xlabel("Numbers Raised")


plt.suptitle('Fun with Numbers', c='blue', fontfamily='Comic Sans MS', fontsize= '25')
plt.subplots_adjust(top= .8, wspace= 1.5)
plt.show()