# DASS-A2

## Question 1

### Task A: SRS Document

#### Functional Requirements

1. **Authentication**: Sign up and Login for the following people:

- App Manager
- Customers
- Delivery agents

2. **Type of delivery**: Different types of deliveries:

- Home Delivery
- Takeaway

3. **Order Management**: This is the main functionality of this application. We can split this into two sub-functions:
  a. Viewing Order Details: Details such as:
    - Type:
      - Home Delivery
      - Takeout
    - Items:
      - Name
      - Quantity
    - User Details
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

### Use Cases - Fully Dressed Use-Cases

#### 1. Customer Registration and Login

**Primary Actor:** Customer
**Stakeholders:** Customer, System
**Preconditions:** Customer has internet access and the application installed
**Main Success Scenario:**

1. Customer launches the application
2. Customer selects "Register" option
3. System displays registration form
4. Customer enters personal details (name, email, phone, address, password)
5. System validates the information
6. System creates customer account
7. System sends verification email/SMS
8. Customer verifies account
9. System confirms successful registration

**Login Flow:**

1. Customer enters credentials (email/phone and password)
2. System validates credentials
3. System grants access to customer dashboard

**Alternative Flows:**

- Registration with invalid information: System provides specific error messages
- Forgotten password: System offers password recovery option
- Failed login attempts: System limits attempts and offers account recovery

**Postconditions:** Customer has access to ordering functionality

#### 2. Delivery Agent Registration and Login

**Primary Actor:** Delivery Agent
**Stakeholders:** Delivery Agent, Manager, System
**Preconditions:** Delivery agent is authorized by the company
**Main Success Scenario:**

1. Delivery agent launches application
2. Delivery agent selects "Delivery Agent Login"
3. First-time agents select "Register"
4. Agent enters personal details (name, ID, phone, vehicle information, password)
5. System validates the information
6. Manager approves the registration
7. System creates delivery agent account
8. Agent logs in with credentials

**Login Flow:**

1. Agent enters credentials
2. System validates credentials
3. System grants access to delivery dashboard

**Alternative Flows:**

- Registration pending approval: System notifies agent
- Registration rejected: System notifies agent with reason
- Agent status update (available/unavailable): Agent can toggle status

**Postconditions:** Agent can view and accept delivery assignments

#### 3. Customer Placing an Order

**Primary Actor:** Customer
**Stakeholders:** Customer, Restaurant, System
**Preconditions:** Customer is logged in
**Main Success Scenario:**

1. Customer browses restaurant menu
2. Customer selects items and quantities
3. Customer adds items to cart
4. Customer can continue shopping or proceed to checkout
5. System displays order summary with items and prices
6. Customer selects delivery type (Home Delivery or Takeaway)
7. For Home Delivery, customer confirms delivery address
8. Customer selects payment method
9. Customer completes payment
10. System displays estimated delivery/pickup time
11. System confirms order placement

**Alternative Flows:**

- Multiple orders: Customer can place additional orders before checkout
- Modification: Customer can modify quantities or remove items before checkout
- Cancellation: Customer can cancel order within defined timeframe
- Payment failure: System offers alternative payment methods

**Postconditions:**

- Order is submitted to restaurant
- Customer can track order status
- Delivery time is displayed for customer reference

#### 4. Order Received by Restaurant

**Primary Actor:** Restaurant Staff
**Stakeholders:** Customer, Restaurant Staff, System
**Preconditions:** Customer has placed an order
**Main Success Scenario:**

1. System notifies restaurant of new order
2. Restaurant staff views order details through POV terminal
3. Restaurant staff confirms order receipt
4. Restaurant staff updates order status to "Preparing"
5. System notifies customer of status change
6. Restaurant prepares food
7. Restaurant updates order status to "Ready for Delivery/Pickup"

**Alternative Flows:**

- Order rejection: Restaurant can reject order with reason
- Order modification: Restaurant can suggest modifications if items unavailable
- Delay notification: Restaurant can update estimated preparation time

**Postconditions:** Order is prepared and ready for delivery/pickup

#### 5. Restaurant Assigning a Delivery Agent

**Primary Actor:** Restaurant Manager/System
**Stakeholders:** Customer, Delivery Agent, Restaurant, System
**Preconditions:** Order is ready for delivery
**Main Success Scenario:**

1. System automatically identifies available delivery agents based on location
2. System assigns order to optimal delivery agent
3. Selected agent receives notification with order details
4. Agent accepts delivery assignment
5. Agent's status updates to "On Delivery"
6. System notifies customer of agent assignment with agent details
7. Agent picks up order from restaurant
8. Agent confirms pickup in system
9. System updates order status to "Out for Delivery"

**Alternative Flows:**

- Agent rejection: System reassigns to next available agent
- No agents available: System notifies restaurant and customer of delay
- Agent status change: If agent becomes unavailable, system reassigns order

**Postconditions:** Order is assigned to delivery agent and in transit

#### 6. Manager Registration and Login

**Primary Actor:** Restaurant Manager
**Stakeholders:** Manager, System
**Preconditions:** Manager has company authorization
**Main Success Scenario:**

1. Manager accesses management portal
2. First-time manager selects "Register"
3. Manager enters credentials and company verification code
4. System validates manager authorization
5. System creates manager account
6. Manager logs in with credentials

**Login Flow:**

1. Manager enters credentials
2. System validates credentials
3. System grants access to management dashboard

**Alternative Flows:**

- Invalid authorization: System rejects registration
- Account recovery: System provides secure recovery process

**Postconditions:** Manager has access to restaurant POV and system management features

#### 7. Manager Checking Pending Orders

**Primary Actor:** Restaurant Manager
**Stakeholders:** Manager, Restaurant Staff, Customers, System
**Preconditions:** Manager is logged in
**Main Success Scenario:**

1. Manager accesses "Pending Orders" section
2. System displays list of all orders with statuses
3. Manager can filter orders by status, time, or customer
4. Manager can view detailed information for each order
5. Manager can update order status or priority
6. Manager can communicate with kitchen about specific orders
7. System reflects any changes in real-time

**Alternative Flows:**

- Order issue resolution: Manager can flag problematic orders
- Communication with customer: Manager can send updates directly to customer
- Order cancellation: Manager can cancel orders with proper notification

**Postconditions:** Manager has comprehensive view of order statuses and can make informed decisions

#### 8. Manager Checking Available Delivery Agents

**Primary Actor:** Restaurant Manager
**Stakeholders:** Manager, Delivery Agents, System
**Preconditions:** Manager is logged in
**Main Success Scenario:**

1. Manager accesses "Delivery Agents" section
2. System displays list of all delivery agents with current status
3. Manager can view agent locations on map interface
4. Manager can filter agents by status, location, or performance metrics
5. Manager can view detailed information for each agent
6. Manager can manually assign/reassign agents to orders if needed
7. Manager can communicate with agents through the system

**Alternative Flows:**

- Agent performance review: Manager can access agent metrics
- Manual override: Manager can override automatic assignments
- Agent support: Manager can provide assistance to agents facing issues

**Postconditions:** Manager has oversight of delivery fleet and can optimize operations
