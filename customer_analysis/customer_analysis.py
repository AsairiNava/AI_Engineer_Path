# Customer data

customers = [
    {
        "name": "Laura",
        "score": 76,
        "balance": 18500,
        "debt": 7000,
        "active": True
    },
    {
        "name": "Carlos",
        "score": 85,
        "balance": 25000,
        "debt": 5000,
        "active": True
    },
    {
        "name": "Ana",
        "score": 55,
        "balance": 9000,
        "debt": 18000,
        "active": True
    },
    {
        "name": "Pedro",
        "score": 91,
        "balance": 32000,
        "debt": 4000,
        "active": False
    },
    {
        "name": "Sofia",
        "score": 68,
        "balance": 15000,
        "debt": 12000,
        "active": True
    }
]


# Business rules

def calculate_segment(score, balance, active):
    if not active:
        segment = "Inactive"
    elif score >= 80 and balance >= 20000:
        segment = "Premium"
    elif score >= 60 and balance >= 10000:
        segment = "Preferred"
    else:
        segment = "Standard"

    return segment


def calculate_risk(score, debt):
    if score >= 80 and debt < 10000:
        risk = "Low"
    elif score >= 60 and debt < 15000:
        risk = "Medium"
    else:
        risk = "High"

    return risk


def evaluate_eligibility(score, debt, active):
    if not active:
        eligibility = "Not Eligible"
    elif score >= 75 and debt < 10000:
        eligibility = "Eligible"
    elif score >= 60 and debt < 15000:
        eligibility = "Review"
    else:
        eligibility = "Not Eligible"

    return eligibility


# Customer processing

for customer in customers:
    customer["segment"] = calculate_segment(
        customer["score"],
        customer["balance"],
        customer["active"]
    )

    customer["risk"] = calculate_risk(
        customer["score"],
        customer["debt"]
    )

    customer["eligibility"] = evaluate_eligibility(
        customer["score"],
        customer["debt"],
        customer["active"]
    )


# Portfolio summary

premium = 0
preferred = 0
standard = 0
inactive = 0

for customer in customers:
    if customer["segment"] == "Premium":
        premium += 1
    elif customer["segment"] == "Preferred":
        preferred += 1
    elif customer["segment"] == "Standard":
        standard += 1
    elif customer["segment"] == "Inactive":
        inactive += 1


eligible = 0
review = 0
not_eligible = 0

for customer in customers:
    if customer["eligibility"] == "Eligible":
        eligible += 1
    elif customer["eligibility"] == "Review":
        review += 1
    elif customer["eligibility"] == "Not Eligible":
        not_eligible += 1


# Report

print("=== CUSTOMER RISK & SEGMENTATION REPORT ===")
print()

print("Total Customers:", len(customers))
print()

print("SEGMENTS")
print("Premium:", premium)
print("Preferred:", preferred)
print("Standard:", standard)
print("Inactive:", inactive)
print()

print("ELIGIBILITY")
print("Eligible:", eligible)
print("Review:", review)
print("Not Eligible:", not_eligible)