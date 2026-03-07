# [Geometric NL Specification]
TASK: activity_selection
INTERFACE: maxActivities(self, arg1)

LOGIC:
  INPUT: arg1
  1. sort by end time
  2. select non-overlapping
  OUTPUT: return length
