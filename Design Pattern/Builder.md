An object with some optional parameters.
```java
public User (String firstName, String lastName, int age, String phone, String address){
    this.firstName = firstName; // Required
    this.lastName = lastName; // Required
    this.age = age; // Optional
    this.phone = phone; // Optional
    this.address = address; // Optional
}
```
Multiple construtors are needed:
```java
public User (String firstName, String lastName, int age, String phone){ ... }
public User (String firstName, String lastName, String phone, String address){ ...  }
public User (String firstName, String lastName, int age){ ...   }
public User (String firstName, String lastName){ ...    }
```
