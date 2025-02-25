# DASS-A2

## Question 1
### Task A: SRS Document

#### Functional Requirements

1. **Authentication**: Sign up and Login for the following people:
  - App Manager
  - Customers
  - Delivery agents <br/>

2. **Type of delivery**: Different types of deliveries:
  - Home Delivery
  - Takeaway <br/>
3. **Order Management**: This is the main functionality of this application. We can split this into two sub-functions: <br/>
  a. Viewing Order Details: Details such as:
    - Type:
      - Home Delivery
      - Takeout
    - Items:
      - Name
      - Quantity
    - User Details <br/>
  b. Multiple Orders from the same user.
4. **Manager Terminal**: Viewing activity of the restaurant like pending orders, available delivery agents, etc.

#### Non Functional Requirements

1. Persistent instance of the app for every user.

#### System Requirements

1. Python for codebase.
2. PyTest for testing of individual modules.

#### Stakeholders

1. Users
2. Delivery agents
3. Cooks
4. Manager

#### Use Cases

1. Customer registration and login
2. Delivery agent registration and login
3. Customer placing an order
4. Order received by cooks in restaurant
5. Restaurant assigning a delivery agent
6. Manager registration and login
7. Manager checking out pending orders
8. manager checking out available delivery agents
