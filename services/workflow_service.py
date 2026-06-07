import random
from datetime import datetime, timedelta


WORKFLOWS = [
    "Delayed Orders Escalation",
    "Refund Complaint Analysis",
    "Inventory Alert Monitoring",
    "SLA Violation Audit",
    "Customer Complaint Review",
    "Weekly Operations Report",
    "Payment Failure Investigation",
    "Warehouse Capacity Check"
]

AGENTS = [
    "Planner",
    "Database",
    "Policy",
    "Analysis",
    "Action",
    "Report"
]


class WorkflowService:

    @staticmethod
    def generate_workflows(count=25):

        records = []

        for idx in range(count):

            workflow_id = f"WF{10000 + idx}"

            status = random.choice(
                [
                    "Completed",
                    "Running",
                    "Failed"
                ]
            )

            execution_time = (
                datetime.now()
                - timedelta(
                    minutes=random.randint(1, 1000)
                )
            )

            records.append(
                {
                    "Workflow ID":
                        workflow_id,

                    "Workflow Name":
                        random.choice(WORKFLOWS),

                    "Status":
                        status,

                    "Executed At":
                        execution_time.strftime(
                            "%d-%b-%Y %I:%M %p"
                        ),

                    "Agent":
                        random.choice(AGENTS),

                    "Duration":
                        f"{random.randint(5,45)} min"
                }
            )

        return records

    @staticmethod
    def workflow_summary():

        return {

            "completed":
                random.randint(120, 180),

            "running":
                random.randint(5, 20),

            "failed":
                random.randint(1, 10),

            "success_rate":
                round(
                    random.uniform(
                        95.0,
                        99.8
                    ),
                    2
                )
        }

    @staticmethod
    def delayed_orders_page_data():

        return [

            {
                "Order ID":
                    f"ORD{random.randint(10000,99999)}",

                "Customer":
                    f"Customer {i}",

                "Days Delayed":
                    random.randint(1,10),

                "Status":
                    random.choice(
                        [
                            "Escalated",
                            "Pending",
                            "Resolved"
                        ]
                    )
            }

            for i in range(30)
        ]

    @staticmethod
    def refund_complaints_data():

        return [

            {
                "Complaint ID":
                    f"RC{random.randint(1000,9999)}",

                "Customer":
                    f"Customer {i}",

                "Amount":
                    f"${random.randint(20,500)}",

                "Status":
                    random.choice(
                        [
                            "Open",
                            "Investigating",
                            "Closed"
                        ]
                    )
            }

            for i in range(25)
        ]