class ImpactPlan:
    def __init__(self, name, goals):
        self.name = name
        self.goals = goals
        self.metrics = {}

    def add_metric(self, goal, metric):
        if goal in self.goals:
            self.metrics[goal] = metric
        else:
            print(f"Goal '{goal}' is not part of the impact plan.")

    def track_metric(self, goal, value):
        if goal in self.metrics:
            self.metrics[goal].append(value)
        else:
            print(f"Goal '{goal}' is not part of the impact plan.")

    def get_average_metric(self, goal):
        if goal in self.metrics:
            metric_values = self.metrics[goal]
            if metric_values:
                return sum(metric_values) / len(metric_values)
            else:
                print(f"No metric values tracked for goal '{goal}'.")
        else:
            print(f"Goal '{goal}' is not part of the impact plan.")


# Create an impact plan
impact_plan = ImpactPlan("Charitable Donations Impact", ["Education", "Healthcare", "Poverty Alleviation"])

# Add metrics for each goal
impact_plan.add_metric("Education", [])
impact_plan.add_metric("Healthcare", [])
impact_plan.add_metric("Poverty Alleviation", [])

# Simulate tracking metrics
impact_plan.track_metric("Education", 80)
impact_plan.track_metric("Education", 90)
impact_plan.track_metric("Education", 95)

impact_plan.track_metric("Healthcare", 70)
impact_plan.track_metric("Healthcare", 75)
impact_plan.track_metric("Healthcare", 80)

impact_plan.track_metric("Poverty Alleviation", 60)
impact_plan.track_metric("Poverty Alleviation", 65)
impact_plan.track_metric("Poverty Alleviation", 70)

# Get average metrics for each goal
education_avg = impact_plan.get_average_metric("Education")
healthcare_avg = impact_plan.get_average_metric("Healthcare")
poverty_avg = impact_plan.get_average_metric("Poverty Alleviation")

# Display the average metrics
print("Average metrics for each goal:")
print(f"Education: {education_avg}")
print(f"Healthcare: {healthcare_avg}")
print(f"Poverty Alleviation: {poverty_avg}")


