import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('AQI_Analysis_Seasonal_Trends.csv')

# Menu 
while True:
    print("\n--- AQI Data Analysis Menu ---")
    print("1. Data Analysis:")
    print("2. Data Manipulation:")
    print("3. Data Visualization:")
    print("4. Exit:")
    choice=input("Enter your choice: ")
    if choice == '1':
        print("1. Read Complete CSV File")
        print("2. Display Data in DataFrame Format")
        print("3. Display Top Records")
        print("4. Display Bottom Records")
        print("5. Display Unique Cities")
        print("6. Filter by City")
        print("7. Filter by Season")
        print("8. Calculate Average AQI by City")
        print("9. Sort by AQI")
        print("10. Display Summary Statistics")
        print("11. Display Correlation Matrix")
        print("12. Find Maximum AQI")
        da=input("Enter option : ")
        if da == '1':
          print(df)
        elif da == '2':
          print(df.head())
        elif da == '3':
          print(df.head(int(input("Enter number of top records to display: "))))
        elif da == '4':
            print(df.tail(int(input("Enter number of bottom records to display: "))))
        elif da == '5':
            print(df['City'].unique())
        elif da == '6':
            city = input("Enter city name: ")
            print(df[df['City'] == city])
        elif da == '7':
            season = input("Enter season: ")
            print(df[df['Season'] == season])
        elif da == '8':
            print(df.groupby('City')['AQI'].mean())
        elif da == '9':
            order = input("Enter 'asc' for ascending or 'desc' for descending: ")
            print(df.sort_values('AQI', ascending=(order == 'asc')))    
        elif da == '10':
            print(df.describe())
        elif da == '11':
            correlation = df.corr()
            sns.heatmap(correlation, annot=True, cmap='coolwarm')
            plt.title('Correlation Matrix')
            plt.show()
        elif da == '12':
            max_aqi = df['AQI'].max()
            max_record = df[df['AQI'] == max_aqi]
            print("Maximum AQI Record:\n", max_record)
    if choice == '2':
      print("1. Add a Column")
      print("2. Add a Row")
      print("3. Export Filtered Data to CSV")
      dm=input("Enter option : ")
      if dm == '1':
        df['New_Column'] = ''
        print("New column added.")
      elif dm == '2':
          new_row = {'City': 'Example City', 'Season': 'Winter', 'Month': 1, 'AQI': 50,
                    'Main_Pollutant': 'PM2.5', 'Temperature_C': 10, 'Humidity_%': 50,
                    'Wind_Speed_kph': 10, 'AQI_Category': 'Good'}
          df.loc[len(df)] = new_row 
          print("New row added.")
      elif dm == '3':
        city_name = input("Enter city name for filtered data: ")
        filtered_df = df[df['City'] == city_name]
        filtered_df.to_csv(f"{city_name}_AQI_data.csv", index=False)
        print(f"Filtered data saved to {city_name}_AQI_data.csv")
    if choice == '3':
      print("1. Visualize AQI Distribution")
      print("2. Seasonal AQI Trend Line")
      print("3. City-Wise AQI Comparison")
      print("4. AQI Category Pie Chart")
      print("5. Heatmap of AQI by Month and City")
      dv=input("Enter option : ")
      if dv == '1':
        plt.hist(df['AQI'], bins=30, color='skyblue')
        plt.xlabel('AQI')
        plt.ylabel('Frequency')
        plt.title('AQI Distribution')
        plt.show()
      elif dv == '2':
          df.groupby('Season')['AQI'].mean().plot(kind='line', marker='o', color='purple')
          plt.xlabel('Season')
          plt.ylabel('Average AQI')
          plt.title('Seasonal AQI Trend')
          plt.show()
      elif dv == '3':
          df.groupby('City')['AQI'].mean().plot(kind='bar', color='orange')
          plt.xlabel('City')
          plt.ylabel('Average AQI')
          plt.title('City-Wise AQI Comparison')
          plt.show()
      elif dv == '4':
          df['AQI_Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['green', 'yellow', 'red'])
          plt.title('AQI Categories')
          plt.show()
      elif dv == '5':
          pivot_table = df.pivot_table(values='AQI', index='Month', columns='City')
          sns.heatmap(pivot_table, cmap='coolwarm', annot=True)
          plt.title('Heatmap of AQI by Month and City')
          plt.show()

    if choice == '4':
      break
    else:
        print("Invalid choice. Please enter a number between 1 and 21.")
