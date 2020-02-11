## HTTP
* GET: retrieve a representation of the resource but not change anything.
* POST: update the resource or a dependent resource base on supplied representation
* HEAD: Optimized GET – retrieves only headers, used for checking caches, etc.
* PUT: create or completely replace the resource base on supplied representation
* DELETE: delete the resource identified by the URI

### HTTP Status code
When a client makes a request to an HTTP server — and the server successfully receives the request — the server must notify the client if the request was successfully handled or not. HTTP accomplishes this with five categories of status codes:

* 100-level (Informational) — Server acknowledges a request
* 200-level (Success) — Server completed the request as expected
* 300-level (Redirection) — Client needs to perform further actions to complete the request
* 400-level (Client error) — Client sent an invalid request
* 500-level (Server error) — Server failed to fulfill a valid request due to an error with server
Based on the response code, a client can surmise the result of a particular request.

Sources:
1. https://www.baeldung.com/rest-api-error-handling-best-practices


## Rest (Representational State Transfer)
