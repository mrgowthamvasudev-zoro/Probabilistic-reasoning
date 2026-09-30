
total_days = 20

rain_days = 8
not_rain_days = 12

cloudy_rain_days = 7
cloudy_not_rain_days = 3

# Step 1: Calculate Prior Probabilities
p_rain = rain_days / total_days
p_not_rain = not_rain_days / total_days

# Step 2: Calculate Conditional Probabilities
p_cloudy_given_rain = cloudy_rain_days / rain_days
p_cloudy_given_not_rain = cloudy_not_rain_days / not_rain_days

# Probability of Cloudy
p_cloudy = (
    p_cloudy_given_rain * p_rain
    + p_cloudy_given_not_rain * p_not_rain
)

# Step 3: Apply Bayes' Theorem
p_rain_given_cloudy = (
    p_cloudy_given_rain * p_rain
) / p_cloudy

p_not_rain_given_cloudy = (
    p_cloudy_given_not_rain * p_not_rain
) / p_cloudy

# Step 4: Compare probabilities
if p_rain_given_cloudy > p_not_rain_given_cloudy:
    prediction = "Rain"
else:
    prediction = "Not Rain"

# Display results
print("----- WEATHER PREDICTION -----")

print("P(Rain) =", round(p_rain, 2))
print("P(Not Rain) =", round(p_not_rain, 2))

print("P(Cloudy | Rain) =", round(p_cloudy_given_rain, 2))
print("P(Cloudy | Not Rain) =", round(p_cloudy_given_not_rain, 2))

print("P(Rain | Cloudy) =", round(p_rain_given_cloudy, 2))
print("P(Not Rain | Cloudy) =", round(p_not_rain_given_cloudy, 2))

print("Predicted Weather =", prediction)