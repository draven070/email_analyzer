from scoring.risk_engine import RiskEngine


def main():

    engine = RiskEngine()

    result = engine.calculate(

        ml_score=99.74,

        url_score=80,

        authentication_score=70,

        header_score=40,

        attachment_score=0,

        reputation_score=90
    )

    print(
        "\nRisk Analysis:"
    )

    print(
        f"Risk Score: "
        f"{result['risk_score']}"
    )

    print(
        f"Severity: "
        f"{result['severity']}"
    )

    print(
        "\nSignals:"
    )

    for name, score in result[
        "signals"
    ].items():

        print(
            f"{name}: {score}"
        )


if __name__ == "__main__":

    main()