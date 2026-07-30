import feedparser

ASX_RSS = "https://www.asx.com.au/asx/rss/asx-announcements.xml"


def get_announcements(limit=10):

    feed = feedparser.parse(ASX_RSS)

    announcements = []

    if getattr(feed, "entries", None):

        for entry in feed.entries[:limit]:

            title = entry.title

            announcements.append(
                {
                    "title": title,
                    "link": getattr(entry, "link", ""),
                    "published": getattr(entry, "published", ""),
                    "category": classify(title),
                }
            )

        return announcements

    # Fallback if ASX feed unavailable

    return [
        {
            "title": "Major Contract Awarded",
            "published": "Today",
            "category": "Major Contract",
            "link": "",
        },
        {
            "title": "Quarterly Activities Report",
            "published": "Yesterday",
            "category": "Quarterly",
            "link": "",
        },
        {
            "title": "Trading Halt",
            "published": "2 days ago",
            "category": "Trading Halt",
            "link": "",
        },
    ]


def classify(title):

    t = title.lower()

    if "trading halt" in t:
        return "Trading Halt"

    if "contract" in t:
        return "Major Contract"

    if "quarterly" in t or "appendix 4c" in t:
        return "Quarterly"

    if "resource" in t:
        return "Resource Upgrade"

    if "drill" in t:
        return "Drill Results"

    if "capital raising" in t or "placement" in t:
        return "Capital Raising"

    if "director" in t:
        return "Director Selling"

    return "Other"