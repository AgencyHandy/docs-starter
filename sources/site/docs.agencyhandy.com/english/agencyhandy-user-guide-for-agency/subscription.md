# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/subscription

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/subscription.md).

The Recurring Billing & Subscription Management feature in **Agency Handy** allows agencies to automate the subscription-based billing process. Agencies can set up recurring pricing plans, generate invoices automatically, and collect payments efficiently. The system supports flexible billing cycles (daily, weekly, monthly, yearly) and ensures seamless client subscription management.

### 

**Full Subscription Flow in Agency Handy (Step-by-Step Guide)**

#### 

**🔹 Step 1: Creating a Subscription-Based Service**

1. Log in to **Agency Handy** and navigate to **Services**.
 
2. Click **Create New Service**.
 
3. Select **Subscription** as the service type.
 
4. Define:
 
 - **Billing Cycle** (Daily, Weekly, Monthly, Yearly)
 
 - **Renewal Behavior** (Create New Order / Update Existing / Keep Unchanged)
 
 - **Pricing & Payment Method** (PayPal, Stripe, Manual)
 
 
5. Click **Publish** to make it available for purchase.
 

---

#### 

**🔹 Step 2: Client Purchases a Subscription**

1. The client selects a **subscription service** from the agency’s dashboard.
 
2. They proceed to checkout and choose a **payment method**.
 
3. Agency Handy automatically:
 
 - Creates a **Subscription ID**
 
 - Generates an **Order**
 
 - Issues an **Invoice**
 
 
4. If using **PayPal or Stripe**, payment is processed instantly, and the invoice is marked **Paid**.
 
5. If using **Manual Payment**, the invoice remains **Open** until manually confirmed by the agency.
 

---

#### 

**🔹 Step 3: Automated Recurring Billing**

1. On each renewal date, Agency Handy:
 
 - **Processes payment automatically** (for PayPal/Stripe)
 
 - **Generates a new invoice** (or updates an existing one, based on renewal settings)
 
 
2. If payment succeeds, the **invoice is marked as Paid**.
 
3. If payment fails:
 
 - The invoice remains **Open**.
 
 - The client receives a **Failed Payment Notification**.
 
 - The agency can retry the payment or request an update to the client’s details.
 
 

---

#### 

**🔹 Step 4: Managing Active Subscriptions**

1. Navigate to **Subscription Management**.
 
2. Select a **subscription** to view details:
 
 - **Client Name, Subscription Fee, Last Payment Date, Next Payment Date, Total Payments Made**
 
 
3. Possible actions:
 
 - **Cancel Subscription** (With or without canceling the last order)
 
 

---

#### 

**🔹 Step 5: Handling Cancellations & Deletions**

1. **Cancel Subscription**: Stops future billing but retains existing orders.
 
2. **Delete Service**: Only possible if all active subscriptions are canceled.
 

---

#### 

**🔹 Step 6: Notifications & Email Updates**

- **Subscription Renewal Reminder** (Sent before renewal)
 
- **Successful Payment Confirmation** (Sent immediately after payment)
 
- **Failed Payment Alerts** (Sent to both the client and agency)
 

### 

**Important Notes**

1️⃣ **Subscription Creation & Management** ✔ **Clients Cannot Cancel Their Own Subscriptions** – Only **SuperAdmin and Admins** have permission to cancel subscriptions. Clients must request cancellation. ✔ **Subscription IDs Are Unique & Cannot Be Edited** – Once a subscription is created, its **Subscription ID** remains unchanged for tracking purposes.

2️⃣ **Recurring Billing & Invoicing** ✔ **Invoices Are Generated Automatically** – For **self-checkout orders**, invoices are created and marked as **Paid** upon successful payment. ✔ **Manual Payment Orders Require Confirmation** – If a client pays manually (e.g., bank transfer), the admin must mark the invoice as **Paid** in the system. ✔ **Unpaid Self-Checkout Attempts Become "Leads"** – If a client initiates a subscription but does not complete payment, they remain in the system as a **Lead** until they subscribe successfully. ✔ **Only One-Time Invoices Can Be Manually Added** – Manual invoicing for PayPal and Stripe only supports **one-time payments**, not automatic recurring charges.

3️⃣ **Payment Failures & Handling** ✔ **Failed Payments Generate New Orders with open invoice** – If a payment fails, the invoice remains **Open**, and a new order is created until payment is retried and subscription is canceled. ✔ **Failed Payment Notifications Are Sent Automatically** – Both **clients and admins** receive alerts when a payment fails. The system will retry the charge, or the admin can manually request updated payment details. ✔ **Subscription Status Remains "Active" Until Canceled** – A subscription does not automatically cancel after a failed payment; the admin must manually **retry or cancel it** if needed.

4️⃣ **Subscription Cancellations & Deletions** ✔ **Active Subscriptions Must Be Canceled Before Deleting a Service** – The **Delete** button is hidden for services with active subscriptions. To delete, cancel all related subscriptions first. ✔ **Admins Can Choose Whether to Cancel the Last Order** – When canceling a subscription, admins can decide to:

- **Cancel the subscription completely** (stopping all future orders & payments).
 
- **Keep the last active order running** (allowing the client to receive the service until its deadline).
 

5️⃣ **Subscription Timeline & Record Keeping** ✔ **Every Subscription Has a Detailed Timeline** – Clicking the **Subscription ID** provides a **history of payments, changes, and invoices** for tracking purposes. ✔ **Old Invoices Do Not Repeat Indefinitely** – Repeating invoices have a limit based on the **subscription plan’s terms** to prevent infinite charges. ✔ **Invoice Due Dates Are Auto-Set** – Due dates align with the **selected billing cycle** (e.g., monthly, weekly).

6️⃣ **Notifications & Client Communication** ✔ **Renewal Reminders Are Sent X Days Before Billing** – Clients receive **Subscription Renewal Reminder emails** ahead of their next billing cycle. ✔ **Successful Payments Trigger Instant Confirmations** – Clients receive **Payment Received notifications** immediately after a successful charge. ✔ **Admins Are Notified of Payment Failures** – If a payment fails, Agency Handy alerts admins to **take action (retry payment, request updated payment details, or cancel the subscription).**

[VorherigeRequested Task](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/requested-task) [NächsteSubscription Management & Recurring Billing in Agency Handy](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/subscription/subscription-management-and-recurring-billing-in-agency-handy)

Zuletzt aktualisiert vor 9 Monaten