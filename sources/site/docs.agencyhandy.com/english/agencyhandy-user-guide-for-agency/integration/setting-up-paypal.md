# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/setting-up-paypal

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/setting-up-paypal.md).

Agency Handy’s PayPal Integration lets you receive client payments directly to your PayPal account. With broad currency support and a simple setup process, it offers a convenient and secure alternative to card payments. Note: PayPal is not available for upsells due to currency and regional limitations.

### 

What You Can Do

- Connect your PayPal account to Agency Handy
 
- Accept payments in multiple international currencies
 
- Offer a secure, familiar payment option to clients
 
- View PayPal transactions from your Agency Handy dashboard
 

### 

Why It Matters

- Reduces friction for international clients
 
- Supports non-card payment preferences
 
- Speeds up payment collection for one-off invoices
 
- Utilizes PayPal’s secure and trusted infrastructure
 

### 

Who Can Use This

To connect PayPal, users must:

- Have an active Agency Handy account
 
- Have an active PayPal account
 
- Be a SuperAdmin or Admin
 
- Have access to Integration settings
 

### 

Getting Started

1. Log In to Your Account
 

- Sign in to your Agency Handy account using valid credentials
 

1. Navigate to Payment Settings
 

- From the left sidebar, go to Integrations
 
- Select PayPal Integration
 

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252Fo3PV4UPRa6rhkDTz7DOW%252FScreenshot_147.png%3Falt%3Dmedia%26token%3Ded7d2fa1-23f1-41bd-9ccc-1a6b10e3b1a7&width=768&dpr=3&quality=100&sign=33053c55&sv=2)

1. Connect PayPal
 

- Click the Connect PayPal button
 
- You’ll be redirected to PayPal’s login page
 
- Log in and authorize Agency Handy to access your account
 
- Grant permissions as prompted
 

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FXmNHWQmokiGEPLdbq15k%252FScreenshot_148.png%3Falt%3Dmedia%26token%3D3e3457d2-7be5-4d0d-83d2-a39f4c1003c8&width=768&dpr=3&quality=100&sign=a9823a34&sv=2)

1. Confirm the Connection
 

- After successful authorization, you’ll return to Agency Handy
 
- A confirmation message will appear: PayPal Connected
 

### 

Supported Currencies

Agency Handy supports the following PayPal currencies:

AUD, BRL, CAD, CNY, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, SGD, SEK, CHF, THB, USD

### 

Important Notes

- Currency Compatibility: Ensure that PayPal supports the currency used in your invoice
 
- Decimal Restrictions: Some currencies (e.g., JPY) do not support decimals—check before invoicing
 
- Regional Rules (e.g., BRL):
 
 - BRL is only available for Brazilian PayPal accounts
 
 - If your account is not based in Brazil, BRL payments will be auto-converted to your primary currency
 
 
- Currency Balances:
 
 - Some currencies are available for in-country accounts only
 
 - Ensure your account’s holding currency matches your payment setup to avoid errors
 
 
- Conversion Fees:
 
 - PayPal applies conversion fees and spreads when converting currency
 
 
- Not Supported for Upselling:
 
 - PayPal cannot be used for upsells due to platform-level restrictions
 
 

### 

Testing Transactions

- Before using PayPal in production, send a test invoice
 
- Use a supported currency
 
- Complete the payment using a secondary PayPal account
 
- Ensure the invoice updates correctly and funds are received
 

[VorherigeIntegrating Stripe](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/integrating-stripe) [NächsteBank Payment Method](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/bank-payment-method)

Zuletzt aktualisiert vor 9 Monaten