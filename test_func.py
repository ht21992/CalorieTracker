def calculate_value(value, total_cal, nut_name, daily_intake=2000):
    nutritions = {"fat": 9, "carbohydrate": 4, "protein": 4}

    try:
        calorie_percentage = (value * nutritions[nut_name]) / total_cal * 100
        for_intake = round((daily_intake * calorie_percentage) / nutritions[nut_name], 2)

        return f"{for_intake}g"
    except (ValueError, TypeError):
        return 'NAN'


value = 0.1  # Total Fat in grams per 100g serving
total_cal = 15.3  # Total Calories per 100g serving
nut_name = "fat"  # Nutrient name
daily_intake = 2000  # Daily calorie intake for calculation

total_fat_intake = calculate_value(value, total_cal, nut_name, daily_intake)
print(total_fat_intake)