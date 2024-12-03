# DSA Problem for 2024-12-04

Here is a novel DSA problem with a Python solution:

**Problem Statement:**

**Calendar Scheduling**

You are a virtual assistant tasked with scheduling meetings for a company. You have a list of available time slots and a list of meeting requests. Each meeting request has a duration and a list of preferred time slots. Your goal is to schedule the meetings in a way that maximizes the number of meetings that can be accommodated.

**Input Format:**

* `time_slots`: a list of integers representing the available time slots (e.g., [9, 10, 11, ...])
* `meeting_requests`: a list of tuples, where each tuple contains the meeting duration and a list of preferred time slots (e.g., [(30, [9, 10]), (60, [11, 12, 13]), ...])

**Output Format:**

* A list of scheduled meetings, where each meeting is represented as a tuple containing the meeting duration and the assigned time slot.

**Example Input:**

```
time_slots = [9, 10, 11, 12, 13, 14, 15]
meeting_requests = [(30, [9, 10]), (60, [11, 12, 13]), (30, [10, 11]), (90, [12, 13, 14])]
```

**Example Output:**

```
[(30, 9), (60, 11), (30, 10), (90, 12)]
```

**Optimal Solution:**
```python
def schedule_meetings(time_slots, meeting_requests):
    # Sort meeting requests by duration in descending order
    meeting_requests.sort(key=lambda x: x[0], reverse=True)

    # Create a dictionary to store the scheduled meetings
    scheduled_meetings = {}

    # Iterate over the meeting requests
    for duration, preferred_slots in meeting_requests:
        # Find a time slot that can accommodate the meeting
        for slot in preferred_slots:
            if slot not in scheduled_meetings:
                # Schedule the meeting
                scheduled_meetings[slot] = duration
                break

    # Convert the scheduled meetings to a list of tuples
    scheduled_meetings_list = [(duration, slot) for slot, duration in scheduled_meetings.items()]

    return scheduled_meetings_list
```

**Time Complexity Analysis:**

* The time complexity of sorting the meeting requests is O(n log n), where n is the number of meeting requests.
* The time complexity of iterating over the meeting requests and scheduling the meetings is O(n \* m), where m is the average number of preferred time slots per meeting request.
* Therefore, the overall time complexity is O(n log n + n \* m).

**Space Complexity Analysis:**

* The space complexity is O(n), where n is the number of scheduled meetings. This is because we store the scheduled meetings in a dictionary and convert it to a list at the end.

Note that this problem can be solved using a greedy approach, and the optimal solution provided uses a combination of sorting and iteration to find a feasible schedule.