# regional_summary.py
# a simple analyst script that summerizes the regional sales

sales_by_region ={
    "North": 12000,
    "South": 8500,
    "East": 15400,
    "West": 9800,
    "Central": 11200,
}

def calculate_total(sales_dict):
    total = 0
    for revenue in sales_dict.values():
        total = total + revenue
    return total

def calculate_average(sales_dict):
    total = calculate_total(sales_dict)
    count = len(sales_dict)
    average = total / count
    return average

print("Regional Sales Summary")

print("total:", calculate_total(sales_by_region))

print("average:", calculate_average(sales_by_region))
