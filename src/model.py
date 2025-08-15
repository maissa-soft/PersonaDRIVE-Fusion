import pandas as pd

# Exemple données cliniques fictives
data = {
    "patient_id": [1, 2, 3],
    "age": [65, 54, 71],
    "gender": ["M", "F", "M"],
    "marker_value": [2.5, 3.1, 4.0]
}
df = pd.DataFrame(data)
print(df)
