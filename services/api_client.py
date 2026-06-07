import random
from datetime import datetime, timedelta


class MockAPIClient:

    @staticmethod
    def get_kpis():

        return {
            "total_orders": random.randint(12000, 15000),
            "delayed_orders": random.randint(500, 1500),
            "complaints": random.randint(100, 800),
            "sla_violations": random.randint(50, 200),
            "refunds": random.randint(50, 150),
            "inventory_alerts": random.randint(10, 50)
        }

    @staticmethod
    def get_delayed_order_trend():

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        values = [
            random.randint(150, 700)
            for _ in range(7)
        ]

        return {
            "days": days,
            "values": values
        }

    @staticmethod
    def get_complaints_breakdown():

        return {
            "labels": [
                "Delivery",
                "Refund",
                "Payment",
                "Product Quality"
            ],
            "values": [
                random.randint(10, 50),
                random.randint(10, 50),
                random.randint(10, 50),
                random.randint(10, 50)
            ]
        }

    @staticmethod
    def get_sla_data():

        return {
            "days":
                ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

            "values":
                [random.randint(10,60) for _ in range(7)]
        }

    @staticmethod
    def get_agent_status():

        return [
            {
                "name":"Planner Agent",
                "status":"Running"
            },
            {
                "name":"Database Agent",
                "status":"Healthy"
            },
            {
                "name":"Policy Agent",
                "status":"Healthy"
            },
            {
                "name":"Analysis Agent",
                "status":"Running"
            },
            {
                "name":"Action Agent",
                "status":"Idle"
            },
            {
                "name":"Report Agent",
                "status":"Healthy"
            }
        ]

    @staticmethod
    def get_notifications():

        return [
            {
                "title":"Critical Inventory Alert",
                "priority":"High"
            },
            {
                "title":"Refund SLA Breach",
                "priority":"Medium"
            },
            {
                "title":"Delayed Shipment Spike",
                "priority":"High"
            }
        ]