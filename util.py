import json
import districts

''' Module with important calculations '''

# Constants of the SARS-CoV-2-Rapid Antigen Tests from Roche, Germany
TRUE_POSITIVE = 0.9652      # sensitivity
TRUE_NEGATIVE = 0.9968      # sensibility
FALSE_POSITIVE = 1 - TRUE_POSITIVE
FALSE_NEGATIVE = 1 - TRUE_NEGATIVE

# Probability of being infected in given district
def infection_prob(distr: districts.District):
    print(distr.incidence / 100000)
    return distr.incidence / 100000

# Probability of actually being infected after a positive test
def positive_predictive_value(distr: districts.District):
    return (TRUE_POSITIVE * infection_prob(distr)) / \
        (TRUE_POSITIVE * infection_prob(distr) + FALSE_POSITIVE * (1 - infection_prob(distr)))

# Probability of actually being infected after a negative test
def negative_predictive_value(distr: districts.District):
    return (TRUE_NEGATIVE * infection_prob(distr)) / \
        (TRUE_NEGATIVE * infection_prob(distr) + FALSE_NEGATIVE * (1 - infection_prob(distr)))