import matplotlib.pyplot as plt

x = input("Enter the fruits:")
f = []
f.append(x)
y = input("Enter the vegetables:")
v = []
v.append(y)
print("The fruits are:",f)
print("The vegetables are:",v)
a =int(input("Enter the number of fruits and vegetables:"))
if(a <= 10):
    b = int(input("Enter the number of fruits:"))
    c = int(input("Enter the number of vegetables:"))
    fr = b*10
    veg = c*10
else:
    print("Enter the sum equal to or less than 10")
    

labels = [v,f]
size = [veg,fr]
colors = ['Pink','Yellow']

plt.pie(size,labels=labels,colors=colors)
plt.axis('Equal')
plt.title('PiePlot')
plt.show()
