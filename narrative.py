"""
MomentumHQ Narrative Engine
Version 3.3.0-dev

Converts structured analysis into natural language
used throughout MomentumHQ.

The Narrative Engine provides the Analyst's voice.
"""


def generate_summary(analysis: dict) -> str:
    """
    Generate a concise analyst summary for the
    Morning Brief.
    """

    rating = analysis["rating"]
    category = analysis["announcement_category"]

    score = analysis["opportunity_score"]

    #
    # High confidence
    #

    if rating == "Strong Buy":

        return (
            f"A {category.lower()} announcement has strengthened "
            f"the investment case. Momentum remains positive with "
            f"an Opportunity Score of {score}."
        )

    #
    # Watch
    #

    if rating == "Watch":

        return (
            f"A {category.lower()} announcement has been identified. "
            "The opportunity warrants further monitoring while "
            "awaiting stronger confirmation."
        )

    #
    # Avoid
    #

    if rating == "Avoid":

        return (
            "Recent market activity does not currently support "
            "a compelling investment opportunity."
        )

    #
    # Fallback
    #

    return (
        f"The latest {category.lower()} announcement has been "
        "reviewed by the Analyst."
    )


def generate_headline(analysis: dict) -> str:
    """
    Generate a short headline.
    """

    category = analysis["announcement_category"]

    return f"{category} announcement identified."