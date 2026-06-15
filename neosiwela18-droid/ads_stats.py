#This is the data of the users for each week from monday to sunday.
week1_users= [600, 250, 538, 736, 668, 6859, 457]
week2_users= [700, 300, 3467, 780, 120, 3011, 534]
week3_users= [740, 624, 220, 4556, 240, 534, 664]
week4_users= [872, 460, 260, 150, 5150, 3332, 560]


#These are the totals of each weeks users form  monday to sunday.
sum_week1= sum(week1_users)
sum_week2= sum(week2_users)
sum_week3= sum(week3_users)
sum_week4= sum(week4_users)


print("Week 1 was the highest with a total of: ", sum_week1, "users for the week of april. \n")

#These is the total amount of user for the month.
month_april= (sum_week1 + sum_week2 + sum_week3 + sum_week4)


#These are the Highest users for each week from monday to sunday.
high_week1= max(week1_users)
high_week2= max(week2_users)
high_week3= max(week3_users)
high_week4= max(week4_users)


#These are the average users for each week from monday to sunday.
avg_week1= (sum_week1) // len(week1_users)
avg_week2= (sum_week2) // len(week2_users)
avg_week3= (sum_week3) // len(week3_users)
avg_week4= (sum_week4) // len(week4_users)


#These are the print statements for the totals, averages and highest users for each week from monday to sunday.
print("==== Average daily users for each week from monday to sunday. ==== \n")
print(f"Average daily users for Week 1: {avg_week1}")
print(f"Average daily users for Week 2: {avg_week2}")
print(f"Average daily users for Week 3: {avg_week3}")
print(f"Average daily users for Week 4: {avg_week4} \n")


#These are the print statements for the totals, averages and highest users for each week from monday to sunday.
print("==== Highest accumulation of users in a day within each week. ==== \n")
print(f"Highest day users for Week 1: {high_week1}")
print(f"Highest day users for Week 2: {high_week2}")
print(f"Highest day users for Week 3: {high_week3}")
print(f"Highest day users for Week 4: {high_week4} \n")


#Note that week 1 and week 4 we ran youtube ads and week 2 and week 3 we ran facebook ads. Our goal now is to determine which platform is better for our ads.
print("==== Note that week 1 and week 4 we ran youtube ads and week 2 and week 3 we ran facebook ads. ==== \n")
print(" YOUTUBE ADS: ")
print(" So considering the total of week 1 and week 4 we can see that youtube ads had a total of: ",sum_week1 + sum_week4, "users for the month of april.\n")
print(" FACEBOOK ADS: ")
print(" And considering the total of week 2 and week 3 we can see that facebook ads had a total of: ",sum_week2 + sum_week3, "users for the month of april. \n")

# Claculation for the pecentage of users for youtube and facebook ads.
youtube_percantage= ((sum_week1 + sum_week4) / month_april) * 100
facebook_percentage= ((sum_week2 + sum_week3) / month_april) * 100

print(" CONCLUSION: ")
print(f" Youttube ads represented {youtube_percantage:.2f}% of the total users for the month of april.")
print(f" Facebook ads represented {facebook_percentage:.2f}% of the total users for the month of april. \n")


# Deciding wich was more effective at getting us users for the month of april.
print(" Therefore, we can conclude that: ")
if youtube_percantage > facebook_percentage:
    print(" Youtube ads were more effective in attracting users for the month of april. ")
else: 
    print(" Facebook ads were more effective in attracting users for the month of april. ")
