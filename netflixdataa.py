import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('netflix_titles.csv.zip')
df=pd.DataFrame(data)

# data cleaning
df.drop(['description','cast','listed_in'], axis=1, inplace=True)
df.dropna(subset=['type','release_year'], inplace=True)

#data sorting
#1 top 10 countries 
countries_and_production=df['country'].value_counts().sort_values(ascending=False).head(10)

#diffrence btw movies and shows 
Types_of_production=df['type'].value_counts().sort_values()

#release years 
Release_years=df['release_year'].value_counts().sort_index().tail(15)

#rating
High_ratings=df['rating'].value_counts().sort_values().tail(5)


#subplots
plt, ax= plt.subplots(2,2, figsize=(12,9))
plt.suptitle('netflix data analysis ', fontsize=16, color='darkred')

ax[0][0].barh(countries_and_production.index[::-1], countries_and_production.values[::-1], color='lightblue',label='top countries in production')
ax[0][0].set_title('Number of shows produced by top countries ', fontsize=10)
ax[0][0].legend()
ax[0][0].set_xlabel('Number of production')
ax[0][0].set_ylabel('Country')
print(f"Contries's contribution to netflix: {country.index[0]} has the most number of movies and shows on Netflix. This might be because it's an English-speaking country and has a big film industry.")


ax[0][1].bar(Types_of_production.index, Types_of_production.values, color=['#f28e2b','#4e79a7'], label=['TV shows','Movies'])
ax[0][1].set_title('Number of content published', fontsize=10)
ax[0][1].set_xlabel('Types')
ax[0][1].set_ylabel('Quantity of published type')
ax[0][1].legend()
print(f"Types of content: {show.index[1]}s are more than {show.index[0]}s on Netflix. Maybe people prefer watching movies more, or they are easier to produce.")


ax[1][0].plot(Release_years.index, Release_years.values, marker='o')
ax[1][0].set_title('Content published since 2008 to 2020', fontsize=10)
ax[1][0].set_xlabel('Years')
ax[1][0].set_ylabel('Content published')
ax[1][0].grid(axis='x', color='lightgrey')
max_year = year[year == year.values.max()].index[0]
print(f"Published content per year: The highest number of shows and movies were added in {max_year}. After that, it started decreasing. Maybe because of COVID or other reasons.")


ax[1][1].pie(High_ratings.values, labels=rating.index , autopct='%1.1f%%',colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
ax[1][1].set_title('Top 5 ratings distribution', fontsize=10)
top_rating = rating.idxmax()
print(f"Rating: The most common rating in the top 5 is '{top_rating}'. That means Netflix has a lot of content for older audiences.")


plt.tight_layout()
plt.savefig('Netflix_data_insights.png',dpi=500,bbox_inches='tight')
plt.show()
