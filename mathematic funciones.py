import matplotlib.pyplot as plt
import numpy as np 
x=np.linspace(0,2,100)
plt.plot(x,x,label= 'Γραμμική Συνάρτηση')
plt.plot(x,x**2,label='Τετραγωνική Συνάρτηση')
plt.plot(x,x**3,label='Κυβική Συνάρτηση')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Μαθηματικές Συναρτήσεις')
plt.legend()
plt.show()