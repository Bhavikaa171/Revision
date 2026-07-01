# subplots
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12,5))
ax1.set_title('EstimatedSalary distribution before scaling')
sns.kdeplot(data=x_train, x='EstimatedSalary', color = 'red', ax= ax1)

ax2.set_title('EstimatedSalary distribution after scaling')
sns.kdeplot(data=x_train_scaled, x='EstimatedSalary', color = 'blue', ax =ax2)
