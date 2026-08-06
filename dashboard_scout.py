"""
MomentumHQ Scout Diagnostics
Version 4.0.0-dev

Scout diagnostics workspace.

Provides visibility into the MomentumHQ Scout
Engine for development and testing.

Presentation layer only.
"""

from collections import Counter

import streamlit as st

import scout


def render() -> None:
    """
    Render the Scout Diagnostics workspace.
    """

    st.subheader("🔍 Scout Diagnostics")

    st.caption(
        "Development view of the MomentumHQ Scout Engine."
    )

    st.divider()

    #
    # Retrieve current Scout results.
    #

    candidates = scout.scan()

    signal_counter = Counter()

    total_signals = 0

    for candidate in candidates:

        total_signals += candidate.signal_count

        for signal in candidate.signals:

            signal_counter[signal.scout] += 1

    #
    # Summary
    #

    st.markdown("### Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Candidates",
        len(candidates),
    )

    c2.metric(
        "Signals",
        total_signals,
    )

    c3.metric(
        "Scout Types",
        len(signal_counter),
    )

    st.divider()

    #
    # Scout activity
    #

    st.markdown("### Scout Activity")

    if signal_counter:

        for scout_name in sorted(signal_counter):

            st.metric(
                scout_name,
                signal_counter[scout_name],
            )

    else:

        st.info(
            "No Scout activity detected."
        )

    st.divider()

    #
    # Candidate diagnostics
    #

    st.markdown("### Candidates")

    if not candidates:

        st.info(
            "No candidates were produced."
        )

        return

    for candidate in candidates:

        with st.expander(
            candidate.summary(),
            expanded=False,
        ):

            st.write(
                f"**Company:** {candidate.name}"
            )

            st.write(
                f"**Sector:** {candidate.sector}"
            )

            st.write(
                f"**Priority:** {candidate.priority}"
            )

            st.write(
                f"**Signals:** {candidate.signal_count}"
            )

            st.markdown("#### Evidence")

            for signal in candidate.signals:

                st.markdown(
                    f"- **{signal.scout}**"
                )

                if hasattr(signal, "summary"):

                    st.caption(
                        signal.summary()
                    )