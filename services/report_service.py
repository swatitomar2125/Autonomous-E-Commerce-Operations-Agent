import random
import pandas as pd


class ReportService:

    @staticmethod
    def weekly_report():

        return {

            "Orders":
                random.randint(10000,15000),

            "Complaints":
                random.randint(100,800),

            "Refunds":
                random.randint(50,200),

            "SLA":
                round(
                    random.uniform(
                        95,
                        99.5
                    ),
                    2
                )
        }

    @staticmethod
    def monthly_report():

        return {

            "Orders":
                random.randint(
                    50000,
                    100000
                ),

            "Revenue":
                random.randint(
                    500000,
                    2000000
                ),

            "Refunds":
                random.randint(
                    500,
                    1500
                ),

            "Customer Satisfaction":
                round(
                    random.uniform(
                        4.0,
                        5.0
                    ),
                    2
                )
        }

    @staticmethod
    def trend_analysis():

        return pd.DataFrame(
            {
                "Month":
                    [
                        "Jan",
                        "Feb",
                        "Mar",
                        "Apr",
                        "May",
                        "Jun"
                    ],

                "Orders":
                    [
                        random.randint(
                            10000,
                            20000
                        )
                        for _ in range(6)
                    ],

                "Complaints":
                    [
                        random.randint(
                            100,
                            600
                        )
                        for _ in range(6)
                    ]
            }
        )

    @staticmethod
    def ai_insights():

        insights = [

            "Refund complaints increased 12% this week.",

            "Inventory risk detected for 8 SKUs.",

            "SLA performance dropped 2.4%.",

            "Delayed shipments are concentrated in Zone-3.",

            "Customer satisfaction remains above target."
        ]

        return insights

    @staticmethod
    def executive_summary():

        return """
        Executive Summary

        Overall platform health remains stable.

        Delayed orders increased slightly but remain
        within acceptable thresholds.

        Inventory alerts require immediate attention
        for multiple SKUs.

        Refund processing efficiency improved by 8%.

        AI recommends prioritizing inventory and
        shipment workflows over the next 48 hours.
        """