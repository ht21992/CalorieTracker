from django import template

register = template.Library()

@register.simple_tag
def calculate_value(value, total_cal, nut_name, daily_intake=2000):
    nutritions = {"fat": 9, "carbohydrate": 4, "protein": 4}

    try:
        print(f"  calorie_percentage = ({value} * {nutritions[nut_name]}) / {total_cal} * 100")
        calorie_percentage = (value * nutritions[nut_name]) / total_cal * 100
        print(f"   for_intake = round(({daily_intake} * {calorie_percentage}) / {nutritions[nut_name]}, 2)")
        for_intake = round((daily_intake * calorie_percentage) / nutritions[nut_name], 2)

        return f"{for_intake}g"
    except (ValueError, TypeError):
        return 'NAN'