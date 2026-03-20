def build_weekly_readiness(
    base_readiness: str,
    recovery: int
):
    """
    Returns readiness per day for a 7-day week.
    """

    week = {}

    if base_readiness == "recover" or recovery < 40:
        for d in range(7):
            week[d] = "recover"
        return week

    if base_readiness == "push":
        pattern = ["push", "maintain", "maintain", "recover", "push", "maintain", "recover"]
    else:
        pattern = ["maintain", "maintain", "recover", "maintain", "maintain", "recover", "recover"]

    for i in range(7):
        week[i] = pattern[i]

    return week
