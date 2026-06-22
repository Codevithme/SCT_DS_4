# Task 4: Traffic Accident Data Analysis

## Overview

This project analyzes traffic accident data to identify patterns related to weather conditions, time of day, and geographical locations. Various visualizations are used to uncover accident hotspots and contributing factors.

## Dataset

- Dataset: US Accidents Dataset
- Total Records: 7.7 Million+
- Selected Features:
  - Severity
  - Start_Time
  - Start_Lat
  - Start_Lng
  - Temperature(F)
  - Visibility(mi)
  - Wind_Speed(mph)
  - Weather_Condition
  - State
  - Sunrise_Sunset

## Objectives

- Analyze accident severity distribution.
- Identify weather conditions associated with accidents.
- Study accident frequency by time of day.
- Find states with the highest number of accidents.
- Visualize accident hotspots using geographical coordinates.

## Tools and Libraries

- Python
- Pandas
- Matplotlib

## Data Preprocessing

- Loaded only the required columns to reduce memory usage.
- Converted Start_Time into datetime format.
- Extracted the hour from Start_Time for time-based analysis.
- Handled invalid datetime values using error coercion.

## Visualizations

### 1. Severity Distribution
Bar chart showing the frequency of different accident severity levels.

### 2. Weather Conditions
Bar chart of the top 10 weather conditions associated with accidents.

### 3. Accidents by Time of Day
Line plot showing accident occurrences across different hours.

### 4. Top States by Accidents
Bar chart representing states with the highest number of accidents.

### 5. Accident Hotspots
Scatter plot using latitude and longitude coordinates to identify accident-prone regions.

## Observations

- Moderate severity accidents are the most common.
- Certain weather conditions contribute to increased accident frequency.
- Accidents occur more frequently during specific hours of the day.
- Some states have significantly higher accident counts.
- Accident hotspots are concentrated in densely populated and high-traffic areas.

## Files Generated

- severity_distribution.png
- weather_conditions.png
- hourly_accidents.png
- state_accidents.png
- accident_hotspots.png

## Conclusion

Traffic accident patterns are influenced by weather conditions, time of day, and location. Identifying these factors can help improve road safety and support better traffic management strategies.
