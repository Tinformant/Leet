# Design Pattern
## Coupling
__Coupling__ is the amount of interdependence among modules.
* Design patterns often reduce coupling
 * Low coupling helps make software easier to understand and change
* ADTs also reduce coupling!

## Cohesion
* Cohesion is the degree to which a module’s internal elements are related
 * LinkedList, ArrayList have high cohesion because all the methods are concerned with the data structures
 * But, java.lang.Math has only moderate cohesion, because the methods are not that related
• High cohesion is good because
 * Code that may need to be modified together is grouped together
 * Code that has dependencies on each other is grouped inside a module
 * Design patterns say little to nothing about cohesion!
 
## Decorator Pattern
* Problem:
 * Want to add several different pieces of functionality to object
 * Want to combine these pieces without making classes for all
* possible combinations
* Want to decide at run time what the combinations are
• Solution: The decorator pattern
■ Act like a proxy/adapter, but also implement the same
interface as the original component
■ That way, multiple decorators can be combined 

## Observer Pattern
* One object is the subject, it holds the state
* Another object is the observer, it wants to know when the subject’s state changes
* Whenever the subject changes, notify the observer
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

