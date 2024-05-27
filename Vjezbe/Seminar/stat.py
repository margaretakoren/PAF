#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('double_pendulum_data.csv')


# In[3]:


def set_plot_style():
    plt.style.use('seaborn-darkgrid')
    plt.rcParams.update({
        'axes.titlesize': 16,
        'axes.labelsize': 14,
        'lines.linewidth': 2,
        'lines.markersize': 8,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'legend.fontsize': 12 })


# In[4]:


set_plot_style()

palette = sns.color_palette(["#FF69B4", "#BA55D3", "#9370DB", "#87CEFA", "#FFB6C1", "#FF6347"])

fig, axes = plt.subplots(1, 3, figsize=(24, 6))
sns.lineplot(x=df['t'], y=df['theta1'], label=r'$\theta_1$', ax=axes[0], color=palette[0])
sns.lineplot(x=df['t'], y=df['theta2'], label=r'$\theta_2$', ax=axes[0], color=palette[1])
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Angle (rad)')
axes[0].set_title('Angles Over Time')
axes[0].legend()
axes[0].grid(True)
sns.histplot(df['theta1'], bins=30, kde=True, color=palette[2], ax=axes[1], label=r'$\theta_1$', alpha=0.6)
sns.histplot(df['theta2'], bins=30, kde=True, color=palette[3], ax=axes[1], label=r'$\theta_2$', alpha=0.6)
axes[1].set_xlabel('Angle (rad)')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Histogram of Angles')
axes[1].legend()
axes[1].grid(True)
sns.boxplot(data=df[['theta1', 'theta2']], ax=axes[2], palette=[palette[4], palette[5]])
axes[2].set_xlabel('Angle (rad)')
axes[2].set_ylabel('Values')
axes[2].set_title('Box Plot of Angles')
axes[2].grid(True)
plt.tight_layout()
plt.savefig('combined_angles_analysis.png')
plt.show()


# In[5]:


fig, axes = plt.subplots(1, 3, figsize=(24, 6))
sns.lineplot(x=df['t'], y=df['omega1'], label=r'$\omega_1$', ax=axes[0], color=palette[0])
sns.lineplot(x=df['t'], y=df['omega2'], label=r'$\omega_2$', ax=axes[0], color=palette[1])
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Angular Velocity (rad/s)')
axes[0].set_title('Angular Velocities Over Time')
axes[0].legend()
axes[0].grid(True)
sns.histplot(df['omega1'], bins=30, kde=True, color=palette[2], ax=axes[1], label=r'$\omega_1$', alpha=0.6)
sns.histplot(df['omega2'], bins=30, kde=True, color=palette[3], ax=axes[1], label=r'$\omega_2$', alpha=0.6)
axes[1].set_xlabel('Angular Velocity (rad/s)')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Histogram of Angular Velocities')
axes[1].legend()
axes[1].grid(True)
sns.boxplot(data=df[['omega1', 'omega2']], ax=axes[2], palette=[palette[4], palette[5]])
axes[2].set_xlabel('Angular Velocity (rad/s)')
axes[2].set_ylabel('Values')
axes[2].set_title('Box Plot of Angular Velocities')
axes[2].grid(True)
plt.suptitle('Analysis of Angular Velocities', y=1.02)
plt.tight_layout()
plt.savefig('combined_angular_velocities_analysis.png')
plt.show()


# In[6]:


corr_matrix = df[['theta1', 'omega1', 'theta2', 'omega2']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.savefig('correlation_matrix.png')
plt.show()

