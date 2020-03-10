# Design Pattern
## Coupling
__Coupling__ is the amount of interdependence among modules.

* Design patterns often reduce coupling
 * Low coupling helps make software easier to understand and change
* ADTs also reduce coupling!
# Testing
## Regression Testing
Key idea: When you find a bug
* Write a test that exhibits the bug
* Always run the test when code changes
  * ensures bug doesn’t reappear
* Helps ensure forward progress
  * Ideally, we never go back to old bugs
• Note that automation is key
  * Set of test cases increases over time
  * Without automation, would be too hard to re-execute
  
## Black Box Testing
* Look only at specification, not at code

## Coverage Criteria
* Common metric for test suite quality: coverage
* Goal: test suite covers all possible program behaviors
* Assumption: high coverage ⇒ few mistakes remain in program

