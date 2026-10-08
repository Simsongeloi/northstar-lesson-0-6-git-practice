weekly_sales = {
    "North":   14200,
    "South":    9100,
    "East":    16700,
    "West":    10800,
    "Central": 12400,
}

total_sales = sum(weekly_sales.values())
print("total_sales:", total_sales)

region_count = len(weekly_sales)
print("len:", region_count)

max_sales = max(weekly_sales.values())
print("max_sales:", max_sales)

min_sales = min(weekly_sales.values())
print("min_sales:", min_sales)

average_sales = total_sales / region_count

for region, sales in weekly_sales.items():
    is_above_average = sales > average_sales
    print("above_average:", is_above_average)

print("Regional Sales Summary report")   
print("================================")


for region, sales in weekly_sales.items():
    is_above_average = sales > average_sales

    if is_above_average:
        status = "Above_Average"

    else:
        status = "Below_Average"

    print(f"\nRegion: {region}")
    print(f"Sales: {sales:,.2f}")
    print(f"Status: {status}")

    print("\nOverall Summary Statistics")
    print('===========================')
    print(f"Total Sales:, ${total_sales:,.2f}")
    print(f"Average Sales:, ${average_sales:,.2f}")
    print(f"Maximum Sales:, ${max_sales:,.2f}") 
    print(f"Minimum Sales:, ${min_sales:,.2f}")         