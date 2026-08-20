import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Healthcare & Life Expectancy",
    page_icon="🌍",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

germany_scenarios = pd.read_csv(
    "data/germany_scenarios_2050.csv"
)

india_scenarios = pd.read_csv(
    "data/india_scenarios_2050.csv"
)

germany_indicators = pd.read_csv(
    "data/germany_indicators.csv"
)

india_indicators = pd.read_csv(
    "data/india_indicators.csv"
)


# ============================================================
# TITLE
# ============================================================

st.title("🌍 Healthcare Systems & Life Expectancy")

st.write(
    """
    Comparative analysis of healthcare indicators and
    projected life expectancy for Germany and India.
    """
)

st.caption(
    "Scenario estimates represent statistical associations "
    "under specified indicator trajectories and should not "
    "be interpreted as causal predictions."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

country = st.sidebar.selectbox(
    "Select country",
    ["Germany", "India"]
)

# IMPORTANT:
# This must be called "section", not "ssection"

section = st.sidebar.selectbox(
    "Select analysis",
    [
        "Overview",
        "Historical Trends",
        "2050 Forecast",
        "Healthcare Indicators",
        "Scenario Analysis",
        "🏥 Build a Healthcare Future"
    ]
)


# ============================================================
# SELECT COUNTRY DATA
# ============================================================

if country == "Germany":

    scenario_data = germany_scenarios
    indicator_data = germany_indicators

else:

    scenario_data = india_scenarios
    indicator_data = india_indicators


# ============================================================
# COUNTRY PROFILE
# ============================================================

if country == "Germany":

    country_flag = "🇩🇪"

    country_image = (
        "https://upload.wikimedia.org/"
        "wikipedia/commons/b/ba/"
        "Flag_of_Germany.svg"
    )

    country_summary = """
    Germany is a European country with a comprehensive
    healthcare system and high life expectancy.

    In this study, Germany is examined as one of the two
    countries in a comparative analysis of healthcare
    indicators and life expectancy.
    """

    country_facts = {
        "Region": "Europe",
        "Capital": "Berlin",
        "Population": "Approximately 83 million"
    }

    world_bank_url = (
        "https://data.worldbank.org/country/germany"
    )

else:

    country_flag = "🇮🇳"

    country_image = (
        "https://upload.wikimedia.org/"
        "wikipedia/commons/4/41/"
        "Flag_of_India.svg"
    )

    country_summary = """
    India is a large and diverse country with substantial
    variation in healthcare access, healthcare resources
    and health outcomes.

    In this study, India is examined alongside Germany to
    compare healthcare indicators and their statistical
    relationship with life expectancy.
    """

    country_facts = {
        "Region": "South Asia",
        "Capital": "New Delhi",
        "Population": "Approximately 1.4 billion"
    }

    world_bank_url = (
        "https://data.worldbank.org/country/india"
    )


# ============================================================
# HELPER FUNCTION — GET BASELINE
# ============================================================

def get_baseline(data):

    baseline_rows = data[
        data["Scenario"].astype(str).str.strip()
        == "ARIMA Baseline"
    ]

    if baseline_rows.empty:
        return None

    return baseline_rows[
        "Life_Expectancy_2050"
    ].iloc[0]


# ============================================================
# OVERVIEW
# ============================================================

if section == "Overview":

    st.header(
        f"{country_flag} {country} — Country Profile"
    )

    # --------------------------------------------------------
    # COUNTRY PROFILE
    # --------------------------------------------------------

    profile_col1, profile_col2 = st.columns([1, 3])

    with profile_col1:

        st.image(
            country_image,
            width=220
        )

    with profile_col2:

        st.subheader(
            f"About {country}"
        )

        st.write(
            country_summary
        )

        st.link_button(
            "🌐 Explore World Bank Country Data",
            world_bank_url
        )

    # --------------------------------------------------------
    # COUNTRY INFORMATION
    # --------------------------------------------------------

    st.subheader(
        "📌 Country Information"
    )

    fact_col1, fact_col2, fact_col3 = st.columns(3)

    with fact_col1:

        st.metric(
            "Region",
            country_facts["Region"]
        )

    with fact_col2:

        st.metric(
            "Capital",
            country_facts["Capital"]
        )

    with fact_col3:

        st.metric(
            "Population",
            country_facts["Population"]
        )

    st.divider()

    # --------------------------------------------------------
    # STUDY RESULTS
    # --------------------------------------------------------

    st.header(
        "📊 Findings from This Study"
    )

    baseline = get_baseline(scenario_data)

    best = scenario_data.loc[
        scenario_data[
            "Life_Expectancy_2050"
        ].idxmax()
    ]

    best_name = best["Scenario"]

    best_value = best[
        "Life_Expectancy_2050"
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        if baseline is not None:

            st.metric(
                "2050 ARIMA Baseline",
                f"{baseline:.2f} years"
            )

        else:

            st.metric(
                "2050 ARIMA Baseline",
                "Not available"
            )

    with col2:

        st.metric(
            "Highest Modelled Scenario",
            f"{best_value:.2f} years"
        )

    with col3:

        if baseline is not None:

            st.metric(
                "Modelled Difference",
                f"{best_value - baseline:+.2f} years"
            )

        else:

            st.metric(
                "Modelled Difference",
                "N/A"
            )

    # --------------------------------------------------------
    # WHAT DOES IT MEAN?
    # --------------------------------------------------------

    st.subheader(
        "🔎 What does this mean?"
    )

    if baseline is not None:

        st.write(
            f"""
            Under the scenarios examined in this study, the
            highest projected 2050 life expectancy for
            **{country}** is associated with:

            **{best_name}**

            with a projected value of approximately
            **{best_value:.2f} years**.

            The ARIMA baseline gives a projected 2050 life
            expectancy of approximately **{baseline:.2f} years**.
            """
        )

    else:

        st.write(
            f"""
            The highest modelled 2050 life expectancy for
            **{country}** is associated with:

            **{best_name}**

            with a projected value of approximately
            **{best_value:.2f} years**.
            """
        )

    st.warning(
        """
        Important: These scenario results represent statistical
        associations under specified indicator trajectories.
        They should not be interpreted as causal predictions.
        """
    )

    # ========================================================
    # HISTORICAL LIFE EXPECTANCY + COVID
    # ========================================================

    st.divider()

    st.header(
        f"📈 {country}: Historical Life Expectancy"
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        indicator_data["Year"],
        indicator_data["Life_Expectancy"],
        linewidth=2,
        marker="o",
        markersize=3
    )

    # --------------------------------------------------------
    # COVID PERIOD
    # --------------------------------------------------------

    covid_data = indicator_data[
        indicator_data["Year"].between(2019, 2021)
    ]

    if not covid_data.empty:

        covid_min = covid_data[
            "Life_Expectancy"
        ].min()

        covid_max = covid_data[
            "Life_Expectancy"
        ].max()

        ax.axvspan(
            2019,
            2021,
            alpha=0.15
        )

        ax.annotate(
            "COVID-19 pandemic\nperiod",
            xy=(
                2020,
                (covid_min + covid_max) / 2
            ),
            xytext=(
                2016,
                covid_min - 0.5
            ),
            arrowprops=dict(
                arrowstyle="->"
            ),
            fontsize=10
        )

    ax.set_xlabel("Year")

    ax.set_ylabel(
        "Life Expectancy (years)"
    )

    ax.set_title(
        f"{country}: Historical Life Expectancy "
        "and COVID-19 Period"
    )

    ax.grid(True)

    plt.tight_layout()

    st.pyplot(fig)

    # --------------------------------------------------------
    # COVID EXPLANATION
    # --------------------------------------------------------

    st.subheader(
        "🦠 COVID-19 and the observed life-expectancy disruption"
    )

    st.write(
        f"""
        The historical data can show a temporary disruption
        in life expectancy around the COVID-19 pandemic period.

        The pandemic caused substantial excess mortality in
        many countries. Because life expectancy is calculated
        from mortality patterns, a sudden increase in deaths
        can result in a temporary decline in life expectancy.

        This is an important example of why long-term forecasting
        should be interpreted carefully: major external events
        can create changes that are difficult for a statistical
        model to anticipate in advance.

        The shaded period on the graph marks **2019–2021** as
        the approximate COVID-19 disruption period.
        """
    )

    st.info(
        """
        The COVID-19 period is shown as an observed historical
        disruption. It is NOT treated as a future scenario or
        artificially inserted into the dataset.
        """
    )

    # --------------------------------------------------------
    # DATASET
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "📋 Research Dataset"
    )

    st.dataframe(
        indicator_data,
        use_container_width=True
    )


# ============================================================
# HISTORICAL TRENDS
# ============================================================

elif section == "Historical Trends":

    st.header(
        f"{country} — Historical Life Expectancy"
    )

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    ax.plot(
        indicator_data["Year"],
        indicator_data["Life_Expectancy"],
        linewidth=2,
        marker="o",
        markersize=3
    )

    covid_data = indicator_data[
        indicator_data["Year"].between(2019, 2021)
    ]

    if not covid_data.empty:

        ax.axvspan(
            2019,
            2021,
            alpha=0.15
        )

        covid_mid = covid_data[
            "Life_Expectancy"
        ].mean()

        ax.annotate(
            "COVID-19\nperiod",
            xy=(2020, covid_mid),
            xytext=(2016, covid_mid - 0.5),
            arrowprops=dict(
                arrowstyle="->"
            )
        )

    ax.set_xlabel("Year")

    ax.set_ylabel(
        "Life Expectancy (years)"
    )

    ax.set_title(
        f"{country}: Historical Life Expectancy"
    )

    ax.grid(True)

    plt.tight_layout()

    st.pyplot(fig)

    st.subheader(
        "Historical Data"
    )

    st.dataframe(
        indicator_data[
            [
                "Year",
                "Life_Expectancy"
            ]
        ],
        use_container_width=True
    )

    st.info(
        """
        Historical changes reflect observed population-level
        outcomes. Events such as pandemics, economic shocks,
        policy changes and changes in healthcare systems can
        influence life expectancy.
        """
    )


# ============================================================
# 2050 FORECAST
# ============================================================

elif section == "2050 Forecast":

    st.header(
        f"{country} — Projected Life Expectancy in 2050"
    )

    st.subheader(
        "Alternative 2050 Scenarios"
    )

    st.dataframe(
        scenario_data,
        use_container_width=True
    )

    fig, ax = plt.subplots(
        figsize=(11, 6)
    )

    ax.barh(
        scenario_data["Scenario"],
        scenario_data[
            "Life_Expectancy_2050"
        ]
    )

    ax.set_xlabel(
        "Projected Life Expectancy in 2050 (years)"
    )

    ax.set_ylabel(
        "Scenario"
    )

    ax.set_title(
        f"{country}: Projected Life Expectancy Under "
        "Alternative Scenarios"
    )

    ax.grid(
        axis="x"
    )

    plt.tight_layout()

    st.pyplot(fig)

    # --------------------------------------------------------
    # BASELINE VS BEST
    # --------------------------------------------------------

    baseline = get_baseline(scenario_data)

    best = scenario_data.loc[
        scenario_data[
            "Life_Expectancy_2050"
        ].idxmax()
    ]

    if baseline is not None:

        st.subheader(
            "Baseline vs Highest Scenario"
        )

        comparison = pd.DataFrame({

            "Scenario": [
                "ARIMA Baseline",
                best["Scenario"]
            ],

            "Life Expectancy": [
                baseline,
                best["Life_Expectancy_2050"]
            ]
        })

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        ax.bar(
            comparison["Scenario"],
            comparison["Life Expectancy"]
        )

        ax.set_ylabel(
            "Life Expectancy in 2050 (years)"
        )

        ax.set_title(
            f"{country}: Baseline vs Highest Scenario"
        )

        ax.grid(
            axis="y"
        )

        plt.xticks(
            rotation=20
        )

        plt.tight_layout()

        st.pyplot(fig)

    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    st.subheader(
        "📈 How should the 2050 forecast be interpreted?"
    )

    st.markdown(
        """
        The 2050 estimates represent extrapolations from
        historical patterns and specified hypothetical
        healthcare-indicator trajectories.

        The forecast is therefore best interpreted as:

        **“What would the statistical model estimate under
        these assumptions?”**

        rather than:

        **“What will definitely happen in 2050?”**
        """
    )


# ============================================================
# HEALTHCARE INDICATORS
# ============================================================

elif section == "Healthcare Indicators":

    st.header(
        f"{country} — Healthcare Indicators"
    )

    indicator_names = {

        "Physician_Density":
            "Physician Density",

        "Hospital_Beds_Per_1000":
            "Hospital Beds per 1,000",

        "Health_Expenditure_y":
            "Health Expenditure",

        "Out_of_Pocket":
            "Out-of-Pocket Expenditure",

        "UHC_Coverage_Index":
            "UHC Coverage Index"
    }

    available_indicators = [
        x
        for x in indicator_names.keys()
        if x in indicator_data.columns
    ]

    if not available_indicators:

        st.error(
            "No healthcare indicators are available "
            "for this country's dataset."
        )

    else:

        selected_indicator = st.selectbox(
            "Choose a healthcare indicator",
            available_indicators,
            format_func=lambda x:
                indicator_names[x]
        )

        display_name = indicator_names[
            selected_indicator
        ]

        st.subheader(
            f"{country}: {display_name}"
        )

        fig, ax = plt.subplots(
            figsize=(12, 6)
        )

        ax.plot(
            indicator_data["Year"],
            indicator_data[
                selected_indicator
            ],
            linewidth=2,
            marker="o",
            markersize=3
        )

        ax.set_xlabel("Year")

        ax.set_ylabel(
            display_name
        )

        ax.set_title(
            f"{country}: {display_name} Over Time"
        )

        ax.grid(True)

        plt.tight_layout()

        st.pyplot(fig)

        st.subheader(
            "Healthcare Indicator and Life Expectancy"
        )

        comparison = indicator_data[
            [
                "Year",
                "Life_Expectancy",
                selected_indicator
            ]
        ].dropna()

        st.dataframe(
            comparison,
            use_container_width=True
        )

        st.info(
            """
            A visible relationship between an indicator and
            life expectancy does not automatically mean that
            the indicator causes changes in life expectancy.

            Other healthcare, demographic, socioeconomic and
            environmental factors may influence both variables.
            """
        )


# ============================================================
# SCENARIO ANALYSIS
# ============================================================

elif section == "Scenario Analysis":

    st.header(
        f"{country} — 2050 Scenario Analysis"
    )

    scenario = st.selectbox(
        "Choose a scenario",
        scenario_data[
            "Scenario"
        ].tolist()
    )

    selected = scenario_data[
        scenario_data[
            "Scenario"
        ] == scenario
    ].iloc[0]

    baseline = get_baseline(scenario_data)

    value = selected[
        "Life_Expectancy_2050"
    ]

    if baseline is None:

        st.error(
            "ARIMA Baseline was not found in this dataset."
        )

    else:

        difference = (
            value
            - baseline
        )

        # ----------------------------------------------------
        # KEY METRICS
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "2050 Projection",
                f"{value:.2f} years"
            )

        with col2:

            st.metric(
                "Modelled Difference",
                f"{difference:+.2f} years"
            )

        with col3:

            st.metric(
                "ARIMA Baseline",
                f"{baseline:.2f} years"
            )

        st.subheader(
            scenario
        )

        # ----------------------------------------------------
        # GRAPH
        # ----------------------------------------------------

        comparison_data = pd.DataFrame({

            "Scenario": [
                "ARIMA Baseline",
                scenario
            ],

            "Life Expectancy": [
                baseline,
                value
            ]
        })

        fig, ax = plt.subplots(
            figsize=(10, 5)
        )

        ax.bar(
            comparison_data[
                "Scenario"
            ],
            comparison_data[
                "Life Expectancy"
            ]
        )

        ax.set_ylabel(
            "Life Expectancy in 2050 (years)"
        )

        ax.set_title(
            f"{country}: {scenario} vs ARIMA Baseline"
        )

        ax.grid(
            axis="y"
        )

        plt.xticks(
            rotation=20
        )

        plt.tight_layout()

        st.pyplot(fig)

        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.subheader(
            "🔎 Interpretation of the Scenario"
        )

        if difference > 0:

            st.success(
                f"""
                Under this simulated scenario, projected life
                expectancy in {country} increases by approximately
                **{difference:.2f} years** compared with the
                ARIMA baseline.

                This represents a more favourable modelled outcome
                under the selected indicator trajectory.
                """
            )

        elif difference < 0:

            st.warning(
                f"""
                Under this simulated scenario, projected life
                expectancy in {country} decreases by approximately
                **{abs(difference):.2f} years** compared with the
                ARIMA baseline.

                This represents a less favourable modelled outcome
                under the selected indicator trajectory.
                """
            )

        else:

            st.info(
                """
                This scenario produces approximately the same
                projected life expectancy as the ARIMA baseline.
                """
            )

        # ----------------------------------------------------
        # BENEFICIAL / HARMFUL MECHANISMS
        # ----------------------------------------------------

        st.subheader(
            "🏥 Why could life expectancy increase or decrease?"
        )

        if difference > 0:

            st.markdown(
                """
                ### Potentially beneficial mechanisms

                An improvement in a healthcare indicator may be
                associated with better population health through:

                - Greater availability of healthcare professionals
                - Improved access to treatment
                - Earlier diagnosis
                - Better disease management
                - Greater access to preventive healthcare
                - Reduced avoidable mortality
                - Improved continuity of care

                However, the model does **not** prove that changing
                the indicator alone will directly increase life
                expectancy.
                """
            )

        elif difference < 0:

            st.markdown(
                """
                ### Potentially harmful mechanisms

                A deterioration in a healthcare indicator may be
                associated with poorer population health through:

                - Reduced healthcare access
                - Longer waiting times
                - Delayed diagnosis
                - Reduced treatment availability
                - Reduced preventive care
                - Greater financial barriers
                - Reduced healthcare capacity

                However, the model does **not** establish that the
                selected indicator itself directly causes the change.
                """
            )

        # ----------------------------------------------------
        # COMPUTER SIMULATION
        # ----------------------------------------------------

        st.subheader(
            "💻 How does the computer simulation work?"
        )

        st.markdown(
            """
            The scenario analysis is a **computer-based
            what-if simulation**.

            The model uses historical observations to estimate
            statistical relationships and then applies a specified
            future trajectory to the selected indicator.

            Conceptually:

            **Historical data**

            Healthcare indicator → Life expectancy

            ↓

            **Statistical relationship**

            ↓

            **Hypothetical future indicator trajectory**

            ↓

            **Simulated 2050 life expectancy**

            This allows different possible futures to be compared
            under controlled assumptions.
            """
        )

        # ----------------------------------------------------
        # MODEL LIMITATIONS
        # ----------------------------------------------------

        st.subheader(
            "🧮 Why can a computer simulation differ from reality?"
        )

        st.markdown(
            """
            A statistical simulation is a simplified representation
            of a much more complicated healthcare system.

            In reality, life expectancy is influenced by many
            interacting factors simultaneously, including:

            - Healthcare access
            - Healthcare expenditure
            - Physician availability
            - Hospital capacity
            - Disease prevalence
            - Lifestyle
            - Socioeconomic conditions
            - Education
            - Environmental conditions
            - Demographic changes
            - Public health policies
            - Medical technology

            A scenario may change one selected indicator while
            other factors remain comparatively controlled.

            Real populations do not behave this way.

            Therefore, the scenario should be interpreted as a
            **controlled what-if experiment**, rather than a precise
            prediction of the future.
            """
        )

        # ----------------------------------------------------
        # DIFFERENT MODELS
        # ----------------------------------------------------

        st.subheader(
            "📊 Why can different models produce different results?"
        )

        st.markdown(
            """
            The same historical dataset can produce different
            forecasts depending on the statistical model and
            its assumptions.

            **Trend-based models**

            Emphasise the long-term direction of the data.

            **ARIMA**

            Models patterns in the time series, including changes
            between observations and autocorrelation.

            **Scenario models**

            Allow hypothetical changes in selected indicators
            to be examined.

            **Data limitations**

            Results can also be affected by:

            - Missing observations
            - Changes in data collection
            - Revisions to historical statistics
            - Different definitions of indicators
            - Measurement differences between countries
            - Short historical series

            Therefore, different reasonable modelling approaches
            can produce different trajectories.
            """
        )

        # ----------------------------------------------------
        # COVID
        # ----------------------------------------------------

        st.subheader(
            "🦠 COVID-19: An example of model limitation"
        )

        st.markdown(
            """
            The COVID-19 pandemic demonstrates why forecasting
            healthcare outcomes is difficult.

            Before the pandemic, a model trained on historical
            observations would have had no direct information
            about the unprecedented mortality shock that occurred
            in 2020–2021.

            The pandemic affected:

            - Mortality
            - Healthcare utilisation
            - Hospital capacity
            - Access to routine healthcare
            - Chronic disease management
            - Mental and social wellbeing

            Because life expectancy is derived from mortality
            patterns, an unusually large increase in mortality
            can produce a temporary **dip in life expectancy**.

            The historical graph therefore provides an important
            real-world example of a disruption that a purely
            historical forecasting model may not anticipate.
            """
        )

        st.info(
            """
            The COVID-19 period is treated as an observed
            historical disruption in this application. It is
            not artificially inserted into the forecasting
            scenarios.
            """
        )

        # ----------------------------------------------------
        # OVERALL INTERPRETATION
        # ----------------------------------------------------

        st.subheader(
            "🧠 Overall interpretation"
        )

        st.info(
            """
            The scenario analysis should be interpreted as a
            **what-if analysis**.

            The central question is:

            “If the selected healthcare indicator follows this
            hypothetical trajectory, what life-expectancy outcome
            would the statistical model produce?”

            It does not claim:

            “Changing this indicator will definitely cause life
            expectancy to change by this amount.”

            Healthcare systems are complex and involve multiple
            interacting factors. The scenarios therefore provide
            insight into possible trajectories rather than
            deterministic predictions.
            """
        )


# ============================================================
# BUILD A HEALTHCARE FUTURE
# ============================================================

elif section == "🏥 Build a Healthcare Future":

    st.header(
        f"🏥 Build a Healthcare Future — {country}"
    )

    st.markdown(
        """
        ### What happens if the healthcare system changes?

        This interactive section allows you to explore a
        **what-if healthcare scenario**.

        You can adjust selected healthcare indicators and
        examine how a more favourable or less favourable
        healthcare trajectory could compare with the modelled
        baseline for 2050.

        The purpose is not to predict exactly what will happen.
        Instead, it demonstrates how statistical modelling can
        be used to explore **possible futures under different
        assumptions**.
        """
    )

    st.warning(
        """
        ⚠️ **Important:** This is a statistical simulation,
        not a causal prediction. Changing an indicator in the
        simulator does not mean that the change alone will
        cause the displayed change in life expectancy.
        """
    )

    st.divider()

    # ========================================================
    # BASELINE
    # ========================================================

    baseline_2050 = get_baseline(
        scenario_data
    )

    if baseline_2050 is None:

        st.error(
            "ARIMA Baseline was not found in the scenario dataset."
        )

    else:

        st.subheader(
            "🎯 Step 1 — Choose your healthcare direction"
        )

        direction = st.radio(
            "How would you like to change the healthcare system?",
            [
                "Maintain current trajectory",
                "Healthcare improvement",
                "Healthcare deterioration"
            ],
            horizontal=True
        )

        st.divider()

        # ====================================================
        # INDICATOR DEFINITIONS
        # ====================================================

        indicator_info = {

            "Physician_Density": {
                "name": "Physician Density",
                "description":
                    "Number of physicians available relative "
                    "to the population.",
                "higher_better": True
            },

            "Hospital_Beds_Per_1000": {
                "name": "Hospital Beds per 1,000",
                "description":
                    "Hospital bed availability relative to "
                    "population.",
                "higher_better": True
            },

            "Health_Expenditure_y": {
                "name": "Health Expenditure",
                "description":
                    "Healthcare spending relative to the "
                    "selected dataset's measurement.",
                "higher_better": True
            },

            "Out_of_Pocket": {
                "name": "Out-of-Pocket Expenditure",
                "description":
                    "Healthcare costs paid directly by "
                    "individuals and households.",
                "higher_better": False
            },

            "UHC_Coverage_Index": {
                "name": "UHC Coverage Index",
                "description":
                    "Indicator representing the extent of "
                    "universal health coverage.",
                "higher_better": True
            }
        }

        # ====================================================
        # AVAILABLE INDICATORS
        # ====================================================

        available_simulators = [
            key
            for key in indicator_info.keys()
            if key in indicator_data.columns
        ]

        if not available_simulators:

            st.error(
                "No healthcare indicators are available "
                "for this country."
            )

        else:

            st.subheader(
                "🎛️ Step 2 — Adjust healthcare indicators"
            )

            st.write(
                """
                Move the sliders to explore different
                healthcare futures.
                """
            )

            user_values = {}

            for indicator in available_simulators:

                series = (
                    indicator_data[indicator]
                    .dropna()
                )

                if series.empty:
                    continue

                latest_value = float(
                    series.iloc[-1]
                )

                minimum_value = float(
                    series.min()
                )

                maximum_value = float(
                    series.max()
                )

                historical_range = (
                    maximum_value
                    - minimum_value
                )

                if historical_range == 0:

                    historical_range = (
                        abs(latest_value) * 0.2
                        if latest_value != 0
                        else 1
                    )

                slider_min = max(
                    0,
                    minimum_value
                    - historical_range * 0.25
                )

                slider_max = (
                    maximum_value
                    + historical_range * 0.25
                )

                step = (
                    historical_range / 100
                )

                if step <= 0:
                    step = 0.01

                user_values[indicator] = st.slider(

                    indicator_info[
                        indicator
                    ]["name"],

                    min_value=float(
                        slider_min
                    ),

                    max_value=float(
                        slider_max
                    ),

                    value=float(
                        latest_value
                    ),

                    step=float(step),

                    help=indicator_info[
                        indicator
                    ]["description"]
                )

                st.caption(
                    f"Latest observed value: "
                    f"{latest_value:.3f}"
                )

            st.divider()

            # =================================================
            # CALCULATE RELATIVE CHANGES
            # =================================================

            changes = {}

            for indicator in available_simulators:

                series = (
                    indicator_data[
                        indicator
                    ].dropna()
                )

                if series.empty:
                    continue

                latest_value = float(
                    series.iloc[-1]
                )

                if latest_value != 0:

                    percentage_change = (
                        (
                            user_values[
                                indicator
                            ]
                            - latest_value
                        )
                        / abs(latest_value)
                    ) * 100

                else:

                    percentage_change = 0

                changes[indicator] = (
                    percentage_change
                )

            # =================================================
            # APPLY DIRECTION
            # =================================================

            # Make the three radio options actually matter.
            #
            # Improvement:
            # Move each indicator in a beneficial direction.
            #
            # Deterioration:
            # Move each indicator in an unfavourable direction.
            #
            # Maintain:
            # Use the user's current values.

            if direction == "Healthcare improvement":

                for indicator in available_simulators:

                    series = indicator_data[
                        indicator
                    ].dropna()

                    if series.empty:
                        continue

                    latest_value = float(
                        series.iloc[-1]
                    )

                    if indicator_info[
                        indicator
                    ]["higher_better"]:

                        user_values[
                            indicator
                        ] = min(
                            user_values[
                                indicator
                            ],
                            float(
                                series.max()
                            )
                        )

                    else:

                        user_values[
                            indicator
                        ] = max(
                            user_values[
                                indicator
                            ],
                            float(
                                series.min()
                            )
                        )

            elif direction == "Healthcare deterioration":

                for indicator in available_simulators:

                    series = indicator_data[
                        indicator
                    ].dropna()

                    if series.empty:
                        continue

                    if indicator_info[
                        indicator
                    ]["higher_better"]:

                        user_values[
                            indicator
                        ] = max(
                            user_values[
                                indicator
                            ],
                            float(
                                series.min()
                            )
                        )

                    else:

                        user_values[
                            indicator
                        ] = min(
                            user_values[
                                indicator
                            ],
                            float(
                                series.max()
                            )
                        )

            # =================================================
            # RECALCULATE CHANGES
            # =================================================

            changes = {}

            for indicator in available_simulators:

                series = (
                    indicator_data[
                        indicator
                    ].dropna()
                )

                if series.empty:
                    continue

                latest_value = float(
                    series.iloc[-1]
                )

                if latest_value != 0:

                    percentage_change = (
                        (
                            user_values[
                                indicator
                            ]
                            - latest_value
                        )
                        / abs(latest_value)
                    ) * 100

                else:

                    percentage_change = 0

                changes[indicator] = (
                    percentage_change
                )

            # =================================================
            # SIMPLE SIMULATION SCORE
            # =================================================

            improvement_scores = []

            for indicator in available_simulators:

                if indicator not in changes:
                    continue

                change = changes[
                    indicator
                ]

                if indicator_info[
                    indicator
                ]["higher_better"]:

                    improvement_scores.append(
                        change
                    )

                else:

                    improvement_scores.append(
                        -change
                    )

            if improvement_scores:

                average_change = (
                    sum(improvement_scores)
                    / len(improvement_scores)
                )

            else:

                average_change = 0

            # =================================================
            # SCENARIO ADJUSTMENT
            # =================================================

            adjustment = (
                average_change
                * 0.015
            )

            simulated_value = (
                baseline_2050
                + adjustment
            )

            # =================================================
            # LIMIT RESULT
            # =================================================

            simulated_value = max(
                baseline_2050 - 5,
                min(
                    baseline_2050 + 5,
                    simulated_value
                )
            )

            difference = (
                simulated_value
                - baseline_2050
            )

            # =================================================
            # RESULTS
            # =================================================

            st.subheader(
                "🔮 Your Healthcare Future"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "ARIMA Baseline — 2050",
                    f"{baseline_2050:.2f} years"
                )

            with col2:

                st.metric(
                    "Simulated 2050",
                    f"{simulated_value:.2f} years",
                    delta=f"{difference:+.2f} years"
                )

            with col3:

                if difference > 0:

                    result_label = (
                        "Potential improvement"
                    )

                elif difference < 0:

                    result_label = (
                        "Potential deterioration"
                    )

                else:

                    result_label = (
                        "Similar to baseline"
                    )

                st.metric(
                    "Modelled Direction",
                    result_label
                )

            # =================================================
            # COMPARISON GRAPH
            # =================================================

            st.subheader(
                "📊 Baseline vs Your Healthcare Future"
            )

            graph_data = pd.DataFrame({

                "Scenario": [
                    "ARIMA Baseline",
                    "Your Healthcare Future"
                ],

                "Life Expectancy": [
                    baseline_2050,
                    simulated_value
                ]
            })

            fig, ax = plt.subplots(
                figsize=(10, 5)
            )

            ax.bar(
                graph_data[
                    "Scenario"
                ],
                graph_data[
                    "Life Expectancy"
                ]
            )

            ax.set_ylabel(
                "Projected Life Expectancy "
                "in 2050 (years)"
            )

            ax.set_title(
                f"{country}: Healthcare Future Simulation"
            )

            ax.grid(
                axis="y"
            )

            plt.xticks(
                rotation=15
            )

            plt.tight_layout()

            st.pyplot(fig)

            # =================================================
            # INTERPRETATION
            # =================================================

            st.subheader(
                "🧠 How should we interpret this?"
            )

            if difference > 0:

                st.success(
                    f"""
                    Your selected healthcare trajectory produces
                    a simulated life expectancy approximately
                    **{difference:.2f} years higher** than the
                    ARIMA baseline.

                    This represents a **potentially favourable
                    statistical scenario**.

                    Improvements in healthcare capacity and
                    financial protection can, in a real healthcare
                    system, potentially support:

                    - Earlier diagnosis
                    - Better access to treatment
                    - Improved disease management
                    - Greater preventive care
                    - Reduced avoidable mortality
                    - Better continuity of care

                    However, this simulation does not establish
                    that these changes would directly cause the
                    increase.
                    """
                )

            elif difference < 0:

                st.warning(
                    f"""
                    Your selected healthcare trajectory produces
                    a simulated life expectancy approximately
                    **{abs(difference):.2f} years lower** than the
                    ARIMA baseline.

                    This represents a **potentially less favourable
                    statistical scenario**.

                    In a real healthcare system, deterioration in
                    healthcare resources or financial protection
                    could potentially contribute to:

                    - Reduced healthcare access
                    - Delayed diagnosis
                    - Longer waiting times
                    - Reduced treatment availability
                    - Greater financial barriers
                    - Reduced preventive care

                    Again, the simulation does not establish
                    direct causality.
                    """
                )

            else:

                st.info(
                    """
                    Your selected healthcare trajectory produces
                    a result approximately equal to the baseline.

                    This illustrates that not every change in a
                    healthcare indicator necessarily produces a
                    large change in the modelled outcome.
                    """
                )

            # =================================================
            # INDICATOR CHANGES
            # =================================================

            st.subheader(
                "📋 What did you change?"
            )

            change_table = []

            for indicator in available_simulators:

                series = (
                    indicator_data[
                        indicator
                    ].dropna()
                )

                if series.empty:
                    continue

                latest_value = float(
                    series.iloc[-1]
                )

                change_table.append({

                    "Indicator":
                        indicator_info[
                            indicator
                        ]["name"],

                    "Latest observed value":
                        round(
                            latest_value,
                            3
                        ),

                    "Your selected value":
                        round(
                            user_values[
                                indicator
                            ],
                            3
                        ),

                    "Change (%)":
                        round(
                            changes[
                                indicator
                            ],
                            2
                        )
                })

            change_table = pd.DataFrame(
                change_table
            )

            st.dataframe(
                change_table,
                use_container_width=True
            )

            # =================================================
            # COMPUTER SIMULATION EXPLANATION
            # =================================================

            st.subheader(
                "💻 How does this computer simulation work?"
            )

            st.markdown(
                """
                This interactive tool is a **controlled
                what-if experiment**.

                The user changes one or more healthcare
                indicators relative to their latest observed
                values.

                The application then calculates a relative
                scenario adjustment and compares it with the
                existing 2050 baseline.

                Conceptually:

                **Historical data**

                ↓

                **Healthcare indicator trajectory**

                ↓

                **Statistical scenario assumption**

                ↓

                **Simulated 2050 outcome**

                The simulation therefore asks:

                > *“What kind of outcome would the model produce
                if the healthcare system followed this assumed
                trajectory?”*

                It does **not** claim:

                > *“This is exactly what will happen in 2050.”*
                """
            )

            # =================================================
            # WHY RESULTS CAN DIFFER
            # =================================================

            with st.expander(
                "🔍 Why might the simulation differ from reality?"
            ):

                st.markdown(
                    """
                    Real healthcare systems are much more complex
                    than the simplified simulation.

                    Life expectancy is influenced by many factors,
                    including:

                    - Healthcare access
                    - Disease prevalence
                    - Lifestyle
                    - Socioeconomic conditions
                    - Education
                    - Demographic change
                    - Public health policy
                    - Medical technology
                    - Environmental conditions
                    - Unexpected events

                    The simulator changes selected indicators while
                    keeping many other factors comparatively
                    controlled.

                    Real populations do not behave this way.

                    Therefore, the result should be interpreted as
                    a **modelled scenario rather than a deterministic
                    prediction**.
                    """
                )

            # =================================================
            # MODEL LIMITATIONS
            # =================================================

            with st.expander(
                "🧮 Why can different models produce different trajectories?"
            ):

                st.markdown(
                    """
                    Different statistical models make different
                    assumptions about the same historical data.

                    **ARIMA**

                    Captures temporal patterns, differencing and
                    autocorrelation.

                    **Trend-based models**

                    Emphasise the long-term direction of the
                    observed data.

                    **Scenario modelling**

                    Allows hypothetical healthcare trajectories
                    to be explored.

                    Consequently, reasonable models can produce
                    different estimates for the same future period.

                    This is one reason why the application presents
                    scenarios rather than claiming a single certain
                    future.
                    """
                )