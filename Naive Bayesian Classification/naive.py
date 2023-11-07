import pandas as pd
df=pd.read_csv("/content/play_tennis.csv")
df.head(14)
num_yes_classes = df[df['play'] == 'Yes'].shape[0]
num_no_classes = df[df['play'] == 'No'].shape[0]
pc_yes=num_yes_classes/len(df)
pc_no=num_no_classes/len(df)
x=['Rain','Hot','Normal','Strong']
count_outlook_no = len(df[(df['outlook'] == x[0]) & (df['play'] == 'No')])/pc_no
count_outlook_yes = len(df[(df['outlook'] == x[0]) & (df['play'] == 'Yes')])/pc_yes
count_temp_no = len(df[(df['temp'] == x[1]) & (df['play'] == 'No')])/pc_no
count_temp_yes = len(df[(df['temp'] == x[1]) & (df['play'] == 'Yes')])/pc_yes
count_humidity_no = len(df[(df['humidity'] == x[2]) & (df['play'] == 'No')])/pc_no
count_humidity_yes = len(df[(df['humidity'] == x[2]) & (df['play'] == 'Yes')])/pc_yes
count_wind_no = len(df[(df['wind'] == x[3]) & (df['play'] == 'No')])/pc_no
count_wind_yes = len(df[(df['wind'] == x[3]) & (df['play'] == 'Yes')])/pc_yes
no=count_outlook_no*count_temp_no*count_humidity_no*count_wind_no*pc_no
yes=count_outlook_yes*count_temp_yes*count_humidity_yes*count_wind_yes*pc_yes

class_label="Yes" if(yes>no) else "No"
print(class_label)
