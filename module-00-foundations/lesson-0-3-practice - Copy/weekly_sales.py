

weekly_sales = {
    "Week1": 7500,
    "Week2": 16500,
    "Week3": 15000,
    "Week4": 10000,
    "Week5": 1000
}

def calculate_total(weekly_sales):
    return sum(weekly_sales.values())
print(weekly_sales)


def classify_week(sales, average):
    if sales >= average:
        return "Above average"
    else:
        return "Below average"

print("LineLane Weekly Sales report")

for week, sales in weekly_sales.items():
    average = calculate_total(weekly_sales) / len(weekly_sales)
    classification = classify_week(sales, average)
    print(week, sales, classification)

total = calculate_total(weekly_sales)
average = total / len(weekly_sales)

highest = max(weekly_sales.values())
lowest = min(weekly_sales.values())

print("\n Summary")

print("Total:", total)

print("Average:", average)

print("Highest:", highest)

print("Lowest:", lowest)
        
       
        
        
            
        