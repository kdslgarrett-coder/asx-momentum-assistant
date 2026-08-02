"""
MomentumHQ Opportunity Engine
Version 2.5.3

Central opportunity evaluation engine.
"""

from score import calculate_opportunity_score, get_rating, calculate_confidence, calculate_timing

def evaluate_opportunity(
    technical_score:int,
    announcement_score:int,
    volume_score:int=0,
    risk_score:int=0,
    confirmations:int=3,
    minutes_since_signal:int=30,
):
    score=calculate_opportunity_score(
        technical_score=technical_score,
        announcement_score=announcement_score,
        volume_score=volume_score,
        risk_score=risk_score,
    )

    strengths=[]
    risks=[]

    if technical_score>=30:
        strengths.append("Strong technical trend")
    if announcement_score>=20:
        strengths.append("Positive announcement")
    if volume_score>=7:
        strengths.append("High relative volume")
    if risk_score<=3:
        strengths.append("Low risk profile")
    else:
        risks.append("Elevated risk")

    return {
        "score":score,
        "rating":get_rating(score),
        "technical_score":technical_score,
        "announcement_score":announcement_score,
        "volume_score":volume_score,
        "risk_score":risk_score,
        "confidence":calculate_confidence(confirmations),
        "timing":calculate_timing(minutes_since_signal),
        "strengths":strengths,
        "risks":risks,
        "action":"Investigate Today" if score>=70 else ("Add to Watchlist" if score>=40 else "No Action"),
    }