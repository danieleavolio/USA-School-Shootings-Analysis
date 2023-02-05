import pandas as pd

# Define the data for the "incident" table
data = {'surr_id': [0.0] * 18,
        'incident_id': [0.0] * 18,
        'quarter': [0.0] * 18,
        'school': [0.0] * 18,
        'city': [0.0] * 18,
        'state': [0.0] * 18,
        'school_level': [0.0] * 18,
        'location': [0.0] * 18,
        'situation': [0.0] * 18,
        'targets': [0.0] * 18,
        'barricade': [0.0] * 18,
        'officer_involved': [0.0] * 18,
        'bullied': [0.0] * 18,
        'domestic_violence': [0.0] * 18,
        'gang_related': [0.0] * 18,
        'preplanned': [0.0] * 18,
        'shots_fired': [0.0] * 18,
        'active_shooter_fbi': [0.0] * 18,
        'first_shot': [0.0] * 18}

# Create a Pandas dataframe from the data
incident_df = pd.DataFrame(data)

# Define the data for the "shooter" table
data = {'surr_id': [0.0] * 10,
        'shooterid': [0.0] * 10,
        'incident_id': [0.0] * 10,
        'gender': [0.0] * 10,
        'race': [0.0] * 10,
        'schoolaffiliation': [0.0] * 10,
        'shooteroutcome': [0.0] * 10,
        'shooterdied': [0.0] * 10,
        'injury': [0.0] * 10,
        'age': [0.0] * 10}

# Create a Pandas dataframe from the data
shooter_df = pd.DataFrame(data)

# Define the data for the "victim" table
data = {'surr_id': [0.0] * 8,
        'victimid': [0.0] * 8,
        'incident_id': [0.0] * 8,
        'schoolaffiliation': [0.0] * 8,
        'age': [0.0] * 8,
        'gender': [0.0] * 8,
        'injury': [0.0] * 8,
        'race': [0.0] * 8}

# Create a Pandas dataframe from the data
victim_df = pd.DataFrame(data)

# Save the dataframes to CSV files
incident_df.to_csv("incident.csv", index=False)
shooter_df.to_csv("shooter.csv", index=False)
victim_df.to_csv("victim.csv", index=False)
