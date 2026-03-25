# Python Question: Minimum Number of Platforms Required for a Railway Station
'''
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.

Consider the following constraints:
- Arrival and departure times are given in 24-hour format (e.g., "0900", "1100", "1530").
- No two trains can arrive or depart at the exact same time.
- The arrival and departure times are not necessarily sorted.

Example:
Input:
arr = ["0900", "0940", "0950", "1100", "1500", "1800"]
dep = ["0910", "1200", "1120", "1130", "1900", "2000"]
Output: 3

Explanation:
The first train arrives at 0900 and departs at 0910.
The second train arrives at 0940 and departs at 1200.
The third train arrives at 0950 and departs at 1120.
The fourth train arrives at 1100 and departs at 1130.
The fifth train arrives at 1500 and departs at 1900.
The sixth train arrives at 1800 and departs at 2000.

At time 0950, we have 3 trains on the platform.
At time 1100, we still have 3 trains on the platform.

'''

# Solution
def solution():
    def solve(arr, dep):
        """
        Calculates the minimum number of platforms required for a railway station.

        Args:
            arr: A list of arrival times in 24-hour format (e.g., "0900").
            dep: A list of departure times in 24-hour format (e.g., "0910").

        Returns:
            The minimum number of platforms required.
        """

        n = len(arr)

        # Convert times to integers for easier comparison
        arr_int = [int(time) for time in arr]
        dep_int = [int(time) for time in dep]

        # Sort the arrival and departure times
        arr_int.sort()
        dep_int.sort()

        platforms_needed = 1  # Initialize with 1 platform
        max_platforms = 1     # Initialize with 1 platform
        i = 1                 # Index for arrival times
        j = 0                 # Index for departure times

        # Iterate through the arrival and departure times
        while i < n and j < n:
            # If a train arrives before the current train departs,
            # we need an additional platform
            if arr_int[i] <= dep_int[j]:
                platforms_needed += 1
                i += 1

                # Update the maximum number of platforms needed
                max_platforms = max(max_platforms, platforms_needed)
            else:
                # If a train departs before the current train arrives,
                # we can free up a platform
                platforms_needed -= 1
                j += 1

        return max_platforms

    return solve

# Test cases
def test_solution():
    solve = solution()
    # Test case 1
    arr1 = ["0900", "0940", "0950", "1100", "1500", "1800"]
    dep1 = ["0910", "1200", "1120", "1130", "1900", "2000"]
    assert solve(arr1, dep1) == 3, "Test Case 1 Failed"

    # Test case 2
    arr2 = ["0900", "1100", "1235"]
    dep2 = ["1000", "1200", "1240"]
    assert solve(arr2, dep2) == 2, "Test Case 2 Failed"

    # Test case 3
    arr3 = ["1000", "1030", "1045", "1050", "1100"]
    dep3 = ["1015", "1040", "1100", "1055", "1130"]
    assert solve(arr3, dep3) == 4, "Test Case 3 Failed"

    # Test case 4 (Empty input)
    arr4 = []
    dep4 = []
    assert solve(arr4, dep4) == 1, "Test Case 4 Failed"

    # Test case 5 (Single train)
    arr5 = ["0800"]
    dep5 = ["0830"]
    assert solve(arr5, dep5) == 1, "Test Case 5 Failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()