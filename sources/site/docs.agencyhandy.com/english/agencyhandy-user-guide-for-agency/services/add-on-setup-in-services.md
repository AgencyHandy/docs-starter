# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/add-on-setup-in-services

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/add-on-setup-in-services.md).

The **Add-on Setup** feature in Agency Handy lets you enhance your core services by offering optional add-ons that clients can select during purchase. Add-ons allow agencies to bundle extra value, upsell complementary services, and customize orders based on client needs—without creating entirely new services.

You can create both **one-time** and **subscription-based** add-ons and attach them to service order forms. Once published, add-ons appear as selectable options for clients during checkout.

---

#### 

What You Can Do

- Create one-time or subscription-based add-ons
 
- Define pricing, billing cycles, and currency
 
- Add rich descriptions using the built-in editor
 
- Publish or unpublish add-ons as needed
 
- Attach add-ons to service order forms
 
- Control add-on visibility for client checkout
 

---

#### 

Why It Matters

- Increases average order value through upsells
 
- Gives clients more flexibility when purchasing services
 
- Keeps service customization clean and structured
 
- Reduces the need for creating multiple similar services
 
- Enables clearer tracking for each purchased item (service + add-ons)
 

---

#### 

Who Can Use This

- Super Admin
 
- Admin
 

---

#### 

How to Create an Add-on

1. Go to **Services** from the dashboard. Click the down arrow button.
 
2. Click **Add-ons**
 
3. Select **Add New Add-on**
 
4. Enter the **Add-on Name**
 
5. Add a detailed **Description**
 
6. Choose a **Pricing Type**
 
 - One-time
 
 - Subscription
 
 
7. Configure pricing details
 
 - For one-time: amount and currency
 
 - For subscription:
 
 - Billing interval (e.g., every 1 month)
 
 - Optional billing cycle limit
 
 - Subscription fee and currency
 
 
 
8. Toggle **Publish** to make it available
 
9. Click **Create**
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FawYt0EX2XSG2SnlTrSFM%252FScreenshot_111.png%3Falt%3Dmedia%26token%3De1bc9202-e134-4a5f-8574-c0c8aea879e3&width=768&dpr=3&quality=100&sign=64a113e0&sv=2)
 

Only published add-ons will be visible when connecting them to order forms.

---

#### 

Attach Add-ons to an Order Form

1. Go to **Forms**
 
2. Open the relevant **Order Form**
 
3. Select the **Service**
 
4. Select the **Add-ons** section from the left panel
 
5. Choose the add-ons you want to associate with the service
 
6. Save the form
 

Once connected, clients will see these add-ons as selectable options during checkout.

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252Foyoy2LOih76YTf2OQvYS%252FScreenshot_112.png%3Falt%3Dmedia%26token%3Dd95bb48a-d178-45ea-9c95-f183fb275980&width=768&dpr=3&quality=100&sign=218fd53&sv=2)

---

#### 

Pricing & Billing Behavior

- **One-time add-ons** are charged once during purchase.
 
- **Subscription add-ons** follow the billing interval you set (e.g., every 1 month).
 
- **When the service and add-on have different billing cycles**, Agency Handy bills them together only for the **overlapping cycles**, then continues billing only the one that still has remaining cycles.
 

**Case 1: Add-on Cycle Is Longer Than Service Cycle**

- Both the **service + add-on** are billed together for the service’s total cycles.
 
- After the service ends, **only the add-on** continues billing (if it still has remaining cycles).
 

Example: If a service runs for **4 cycles** and a subscription add-on runs for **5 cycles**, both are billed for **4 cycles**, then only the add-on is billed for the **remaining 1 cycle**.

**Case 2: Add-on Cycle Is Shorter Than Service Cycle**

- Both the **service + add-on** are billed together for the add-on’s total cycles.
 
- After the add-on ends, **only the service** continues billing for its remaining cycles.
 

Example: If a service runs for **5 cycles** and a subscription add-on runs for **3 cycles**, both are billed for **3 cycles**, then only the service is billed for the **remaining 2 cycles**.

---

#### 

Client Purchases

Once the add-on is **published** and **connected to an order form**, clients can select it when purchasing a service.

- Clients will see add-ons listed as optional extras during checkout.
 
- When a client selects add-ons along with the primary service, **each add-on is processed as a separate order**.
 
- Even though the **main service and add-ons are billed at the same time**, Agency Handy creates **distinct orders for each add-on** to support separate tracking and management.
 

This helps your team manage delivery, progress, and reporting for each add-on independently.

---

#### 

Additional Notes

- Unpublished add-ons will not appear on order forms
 
- Add-ons can be reused across multiple services
 
- Currency is set per add-on and cannot be mixed within the same add-on
 
- Deleting an add-on removes it from future purchases but does not change existing orders
 
- Currency is set per add-on and cannot be mixed within the same add-on.
 
- An add-on can only be attached to services that use the same currency.
 
- If an add-on’s currency does not match the service’s currency, the add-on will not appear in the add-on selection list when you try to connect add-ons to that service.
 

[VorherigeDelete a Service](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/delete-a-service) [NächsteMultiple Pricing and Multiple Packages](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/multiple-pricing-and-multiple-packages)

Zuletzt aktualisiert vor 4 Monaten