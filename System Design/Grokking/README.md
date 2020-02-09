## Load Balancing
It helps to spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. 

LB also keeps track of the status of all the resources while distributing requests. If a server is not available to take new requests or is not responding or has elevated error rate, LB will stop sending traffic to such a server.

## Redundant Load Balancers
The load balancer can be a single point of failure; to overcome this, a second load balancer can be connected to the first to form a cluster. Each LB monitors the health of the other and, since both of them are equally capable of serving traffic and failure detection, in the event the main load balancer fails, the second load balancer takes over.

## Consistent Hashing
Hash Tables need a key, a value, and a hash function where hash function maps the key to a location where the value is stored.

index = hash_function(key)

