# Write a function calculate_severity(cvss_score) that categorizes risk. Test multiple inputs.
def calculate_severity(cvss_score):
    if cvss_score == 0.0:
        return "NONE"
    elif cvss_score >= 0.1 and cvss_score <= 3.9:
        return "LOW"
    elif cvss_score >= 4.0 and cvss_score <= 6.9:
        return "MEDIUM"
    elif cvss_score >= 7.0 and cvss_score <= 8.9:
        return "HIGH"
    else:
        return "CRITICAL"


cvss_scores = [0.0, 2.5, 3.9, 4.0, 5.5, 6.9, 7.0, 8.5, 8.9, 9.0, 9.8, 10.0]

for x in cvss_scores:
    print(f"{x} - {calculate_severity(x)}")
