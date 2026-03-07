# [Geometric NL Specification]
TASK: serialize_deserialize_nary_tree
INTERFACE: deserialize(self, arg1)

LOGIC:
  INPUT: arg1
  1. deserialize tree
  OUTPUT: return value
---
TASK: serialize_deserialize_nary_tree
INTERFACE: serialize(self, arg1)

LOGIC:
  INPUT: arg1
  1. serialize tree
  OUTPUT: return value
