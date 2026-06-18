# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/tax-rates

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/tax-rates.md).

The Tax Rates Management feature allows Superadmins and Admins to configure and manage multiple tax types, such as VAT, GST, and Sales Tax, across different countries, states, and billing models. This ensures accurate and compliant tax application across services, subscriptions, and manual invoices.

### 

**What:**

A centralised workspace tool that enables the creation, editing, deletion, and linking of tax types to services and invoices, with support for country and state-specific rules, inclusive/exclusive settings, tax IDS, and verification logic.

### 

**Purpose:**

- Ensure tax compliance across local and international markets.
 
- Automate calculations to reduce human error.
 
- Make invoices accurate and audit-ready.
 
- Adapt billing models for inclusive or exclusive pricing.
 

### 

**Pre-conditions:**

- Only Superadmins and Admins can create or edit taxes.
 
- Users or clients must enter or confirm their billing country, state, and ZIP code at checkout.
 
- For Stripe India accounts, full location info (country, state, ZIP) is mandatory.
 
- Manual invoice tax must be exclusive.
 
- Country/State validation uses prebuilt country lists with optional manual overrides for ZIP codes and states.
 

### 

**Steps to Use (Detailed Guide)**

**1\. Configure Tax Settings**

1. Go to **Workspace Config → Tax Rates Tab**.
 
2. Click "**\+ New Tax".** A form will pop up**.**
 
3. Fill in the following:
 
 - **Title/Tax Type,** e.g., Standard VAT, Reduced VAT, Zero VAT, Exempt VAT, Flat Rate VAT, Input VAT, Output VAT, Import VAT, Reverse Charge VAT. **It's mandatory.**
 
 - **Tax ID** (agency's business tax ID) (optional).
 
 - **Home Country**
 
 - **Home Country General Tax Rate %** (optional)
 
 - **Country-Specific Rates**: (Country-specific VAT rates are the standard and reduced tax rates that vary from one country to another, based on local tax laws and regulations. These rates determine how much tax is applied to products and services in each country.) Choose country → add optional state, ZIP, and % ratele
 
 
4. Set **Active/Inactive** status.
 
5. Click **Save**.
 

> You may edit or delete a tax anytime. Inactive taxes will not apply to new purchases.

1. **Link Taxes to Services**
 

- While creating/editing a service:
 
 - Go to the Additional Info section (Step 3).
 
 - Click the Add Tax option.
 
 - Add one or more taxes.
 
 - Choose **inclusive (**the tax amount is already included in the total price shown to the customer**)** or **exclusive** (the tax amount is added on top of the listed price at checkout). It is applied to all linked taxes.
 
 - Taxes apply to **setup fees** (only for subscription) and **add-ons** as well.
 
 

**3\. Apply Taxes During Checkout or Invoice**

- There are two ways taxes can be applied — **automatically during checkout** or **manually when creating an invoice**:
 
 **Automatic (During Checkout)**
 
 - Taxes will be added automatically based on the client’s location.
 
 - This only works if taxes, such as VAT or GST, have already been linked to the service.
 
 - For example, if a client is from a region where tax applies, the system will detect it and add the correct tax during checkout.
 
 
 **Manual (When Creating an Invoice)**
 
 - You can manually choose which taxes to apply from a list.
 
 - When an invoice is created, go to the Add Taxes option.
 
 - Click it and all the boxes in the Bill Payment Address will be automatically filled up.
 
 - The tax will be automatically added.
 
 - **Only exclusive taxes** (added on top of the price) can be applied manually — inclusive taxes are not supported in manual invoices.
 
 

**4\. Invoice Tax Display**

- On the invoice, the following tax details will be shown:
 
 - **Tax Name**: The label or title you’ve entered (e.g., VAT, GST).
 
 - **Tax Percentage**: The applied tax rate (e.g., 15%).
 
 - **Tax Amount**: The exact amount charged based on the total.
 
 

### 

**Important Notes:**

- Title required (max 255 characters), no system-breaking characters
 
- Up to 4 decimal points supported for tax rates
 
- Optional Tax ID (max 20 characters)
 
- Supports **inclusive/exclusive** taxes (one type per service)
 
- Multiple taxes are supported per service and invoice
 
- Tax applies to **setup fees** and **add-ons**
 
- **Coupon applied → tax calculated on discounted amount**
 
- **The deleted tax** won’t apply to new purchases or subscriptions
 
- **The updated tax** will affect only future invoices/purchases
 
- For manual invoice: tax% editable, always exclusive
 
- Clients’ country/state is prefilled from the profile if available
 
- Profile is **not updated** when editing location during checkout
 
- 0% tax is valid (for zero-rated items or compliance use)
 

### 

**Example Scenarios**

Scenario

What Happens

A service has VAT and GST linked as exclusive

If a service includes both VAT and GST as exclusive taxes, both will be added **on top of** the listed price. For example, if the base price is $100, the final total will include VAT + GST.

A client in Quebec selects province tax

If the client is from Quebec and selects their province, **QST (Quebec Sales Tax)** will be automatically added **if it’s been set up** in the system.

Tax was deleted yesterday

If a tax was removed from your settings, it will **no longer be applied** to any **new purchases** from now on.

A coupon applies a discount

When a discount coupon is used, the tax is calculated **based on the new discounted price**, not the original price.

User enters a U.S. state with zip code

The system will **automatically detect the state** using the zip code and apply the correct **regional/state tax** if a match is found.

[VorherigeSetup SMTP](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/setup-smtp) [NächsteSEO Portal](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/seo-portal)

Zuletzt aktualisiert vor 1 Jahr