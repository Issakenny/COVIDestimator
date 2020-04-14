import math
def estimator(data):

  return data

data = {'name': 'Africa', 'avg_age': 19.7, 'avg_daily_income': 5, 'avg_daily_income_population': 0.71,
                'period_type': 'daily', 'time_to_elapse': 58, 'reported_cases': 674, 'population': 66622705,
                'total_hospital_beds': 1380614 }


impact_currentlyInfected = ((data.get('reported_cases')) * 10)
severeImpact_currentlyInfected = ((data.get('reported_cases')) * 50)

# No of infected people in 30 days
impact_infectionsByRequestedTime = (impact_currentlyInfected * 512)
severeImpact_infectionsByRequestedTime = (severeImpact_currentlyInfected * 512)

# Challenge 2 begins here
# Estimated number of severe positive cases that require hospitalization
impact_severeCasesByRequestedTime = math.trunc(impact_infectionsByRequestedTime * 0.15)
severeImpact_severeCasesByRequestedTime = math.trunc(severeImpact_infectionsByRequestedTime * 0.15)

# Hospital beds by requested time given that only 35% of the bed space is available
impact_hospitalBedsByRequestedTime = (483215 - impact_severeCasesByRequestedTime)
severeImpact_hospitalBedsByRequestedTime = (483215 - severeImpact_severeCasesByRequestedTime)

# Challenge 3 : Cases require ICU Care
impact_casesForICUByRequestedTime = math.trunc(impact_infectionsByRequestedTime * 0.05)
severeImpact_casesForICUByRequestedTime = math.trunc(severeImpact_infectionsByRequestedTime * 0.05)

# Cases require ventilator
impact_caseForVentilatorByRequestedTime = math.trunc(impact_infectionsByRequestedTime * 0.02)
severeImpact_casesForVentilatorByRequestedTime = math.trunc(severeImpact_infectionsByRequestedTime * 0.02)

# Challenge 3: Dollar in flight
impact_dollarsInFlight = math.trunc((impact_infectionsByRequestedTime * 0.65 * 1.5)/30)
severeImpact_dollarsInFlight = math.trunc((severeImpact_infectionsByRequestedTime * 0.65 * 1.5)/30)



print("data:", (data))
print("impact :", impact_currentlyInfected)
print("severeImpact :" , severeImpact_currentlyInfected)
print("impact (InfectionsByRequestedTime):", impact_infectionsByRequestedTime)
print("severeImpact (InfectionsByRequestedTime):", severeImpact_infectionsByRequestedTime)
print("impact (SevereCasesByRequestedTime):", impact_severeCasesByRequestedTime)
print("severeImpact(severeCasesByRequestedTime):", severeImpact_severeCasesByRequestedTime)
print("impact (HospitalBedsByRequestedTime):", impact_hospitalBedsByRequestedTime)
print("severeImpact (HospitalBedsByRequestedTime):", severeImpact_hospitalBedsByRequestedTime)
print("impact (casesForICUByRequestedTime):", impact_casesForICUByRequestedTime)
print("severeImpact (casesForICUByRequestedTime):", severeImpact_casesForICUByRequestedTime)
print("impact (casesForVentilatorByRequestedTime):", impact_caseForVentilatorByRequestedTime)
print("severeImpact (caseForVentilatorByRequestedTime):", severeImpact_casesForVentilatorByRequestedTime)
print("impact (dollarsInFlight):", impact_dollarsInFlight)
print("severeImpact (dollarsInFlight):", severeImpact_dollarsInFlight)


