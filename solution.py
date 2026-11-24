def busiest_window(deliveries: list[int], k: int) -> int:
    """Return the largest total number of deliveries over any k consecutive days.

    deliveries is a list of daily delivery counts in date order, and k is the
    window length. Bounds: 1 <= k <= len(deliveries) <= 10^5 and
    0 <= deliveries[i] <= 10^4.
    """
    current = sum(deliveries[i] for i in range(k))
    best = current

    for i in range(k, len(deliveries)):
        current += deliveries[i] - deliveries[i-k]
        if current>best:
            best = current

    return best
