"""
Consider a scenario where you have a set of activities,
each with a start time and an end time. The goal is to select the maximum number of non-overlapping activities.
"""


def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities by end time
    selected_activities = [activities[0]]

    for i in range(1, len(activities)):
        current_activity = activities[i]
        last_selected_activity = selected_activities[-1]

        # If the current activity doesn't overlap with the last selected activity, add it
        if current_activity[0] >= last_selected_activity[1]:
            selected_activities.append(current_activity)

    return selected_activities


# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]

selected = activity_selection(activities)
print("Selected Activities:", selected)
