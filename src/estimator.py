def estimator(data):

  return data

data = {'name': 'Africa', 'avg_age': 19.7, 'avg_daily_income': 5, 'avg_daily_income_population': 0.71,
                'period_type': 'daily', 'time_to_elapse': 58, 'reported_cases': 674, 'population': 66622705,
                'total_hospital_beds': 1380614 }


impact_currentlyInfected = ((data.get('reported_cases')) * 10)
severeImpact_currentlyInfected = ((data.get('reported_cases')) * 50)

# No of infected people in 30 days
impact_infectionsByRequestedTime = (impact_currentlyInfected * 1024)
severeImpact_infectionsByRequestedTime = (severeImpact_currentlyInfected * 1024)

print("Data:", (data))
print("Impact :", impact_currentlyInfected)
print("Severe impact :" , severeImpact_currentlyInfected)
print("Impact (InfectionsByRequestedTime):", impact_infectionsByRequestedTime)
print("Severe impact (InfectionsByRequestedTime):", severeImpact_infectionsByRequestedTime)

