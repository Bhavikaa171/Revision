#plot
plt.plot(x,y, color='', marker='', markersize='', linestyle='', linewidth='', label='', alpha='') 
plt.scatter(x,y)
plt.bar(xlist, ylist, hatch = 'pattern')
plt.hist(data, bins='number or list of bins range', color='', edgecolor='')
plt.pie([list],labels=['',''], autopct= '%.2f %%', pctdistance='',explode=['',''])
plt.boxplot([list])
plt.axhline(y, slope='')
plt.axvline(x)
-alpha --> opacity, 0=< alpha <= 1
-for different patterns in each bar in bar chart: bar[i].set_hatch('pattern')
-pctdistance --> distance of percentage text from centre
-for 3d graph --> plt.scatter(x,y,z)


#title
plt.title('title', fontname='', fontsize='')
plt.title('title', fontdict={'fontname':'comic_sans', 'fontsize':'23'})


#xlabel/ ylabel
plt.xlabel('x_label',fontdict={'fontname':'comic_sans', 'fontsize':'23'})
plt.ylabel('x_label',fontdict={'fontname':'comic_sans', 'fontsize':'23'})


#xticks/ yticks
plt.xticks([0.5,1,1.5,2.0,2.5,3,4])        #values on x axis
plt.yticks([1,2,3,4,5,6])                  #values on y axis


#must
plt.legend(title='')       # title is optional
plt.show()


#USE SHORTHAND NOTATION 
# fmt= '[color],[marker],[line]'
plt.plot(x,y,'yo--')


#for figure
plt.figure(figsize=(3,), dpi= 300)
plt.savefig("Matplot_graph.png", dpi= 300)
-dpi --> to determine pixel per inch, keep this value high or it gives pixelated image


#add grid
plt.grid(axis='', alpha='')

#concept of subplots
fig, axs = plt.subplot(3,4)          --[rows, columns]
axs[1,1].scatter()
axs[1,2].plot()
axs[2,1].plot()
axs[2,2].plot()

