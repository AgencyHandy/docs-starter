# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/3-decimal-currency-support

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/3-decimal-currency-support.md).

### 

1\. Short Description

Agency Handy now supports full precision for **3-decimal place currencies**, ensuring accuracy in billing, payments, and currency conversions. This guide covers the system's support for currencies like **BHD, JOD, KWD, OMR, TND**, and others that require three decimal places for precise transactions.

---

### 

2\. Goals

#### 

Business Goals

- Ensure reliable support for high-precision currencies.
 
- Prevent rounding errors and ensure regulatory compliance.
 
- Expand international usability with currencies that require 3-decimal precision.
 

#### 

User Goals

- Accurately process payments and refunds in supported currencies.
 
- View properly formatted amounts in both the UI and exports.
 
- Experience smooth currency selection, conversion, and transaction tracking.
 

---

### 

3\. Pre-Conditions

- Feature available on payment processors like **Stripe** where supported.
 
- User must be operating with one of the supported 3-decimal currencies.
 
- Admin permissions required for configuring currency settings and integrations.
 

---

### 

4\. Table of Contents

1. Supported Currencies
 
2. Currency Display & Formatting
 
3. Payment Processing
 
4. Currency Conversion
 
5. Specific Currency Behavior
 
6. API & Database Support
 
7. User Interface Experience
 
8. Edge Cases & Validations
 
9. Outcome
 
10. Important Notes
 

---

### 

5\. Contents

#### 

1\. Supported Currencies

Currency

Code

Stripe Support

Bahraini Dinar

BHD

✅ Yes

Jordanian Dinar

JOD

✅ Yes

Kuwaiti Dinar

KWD

✅ Yes

Omani Rial

OMR

✅ Yes

Tunisian Dinar

TND

✅ Yes

Libyan Dinar

LYD

Partial/Planned

Iraqi Dinar

IQD

❌ Not Available

Malagasy Ariary

MGA

❌ Not Available

Mauritanian Ouguiya

MRU

❌ Not Available

---

#### 

2\. Currency Display & Formatting

- All 3-decimal currencies display with **exactly three decimal places** (e.g., `BHD 123.456`)
 
- **Currency symbols and codes** are shown correctly (e.g., `KWD`, `OMR`)
 
- Negative and zero amounts are correctly formatted: `-12.345`, `0.000`
 
- Formatting is consistent across reports, dashboards, and exports.
 

---

#### 

3\. Payment Processing

- **Successful payments** preserve full 3-decimal precision.
 
- **Refunds** (full or partial) calculate with 3 decimals without rounding.
 
- **Payment failures**, if any, still maintain the correct decimal format in logs.
 
- **Stripe gateway** supports real-time payments for BHD, JOD, KWD, OMR, TND.
 

---

#### 

4\. Currency Conversion

- Accurate **exchange rate** application between 3-decimal and 2-decimal currencies.
 
- All conversion calculations maintain precision.
 
- Converted values are rounded and displayed based on the target currency’s decimal standard.
 

---

#### 

5\. Specific Currency Behavior

**Bahraini Dinar (BHD)**

- Fully supported via Stripe
 
- Format: `XXX.XXX`
 
- All transactions processed and refunded accurately
 

**Iraqi Dinar (IQD)**

- Listed but **not available for payments**
 
- User is informed accordingly during selection
 

**Kuwaiti Dinar (KWD), Jordanian Dinar (JOD), Omani Rial (OMR), Tunisian Dinar (TND)**

- Fully functional with Stripe
 
- Decimal handling and formatting verified
 

**Libyan Dinar (LYD), Malagasy Ariary (MGA), Mauritanian Ouguiya (MRU)**

- Display only; no active payment support
 
- Selection results in proper notification about unavailability
 

---

#### 

6\. API & Database Support

- API endpoints accept, process, and return **3-decimal values**
 
- Database fields store all values without rounding or loss of precision
 
- All integrations (e.g., Stripe, webhooks) retain 3-decimal accuracy
 
- Backup, restore, and data migration preserve precision
 

---

#### 

7\. User Interface Experience

**Input Validation**

- Allows valid input of up to **3 decimal places**
 
- Prevents inputs with more than 3 decimals
 
- Clear error messages for invalid entries
 
- Copy/paste from spreadsheets retains precision
 

**Display Consistency**

- Consistent formatting across all views: dashboard, mobile, reports, exports
 
- Responsive design handles 3-decimal currency formatting on all devices
 

**User Experience**

- Clear visual indication of 3-decimal currency use
 
- Help text/tooltips guide users during selection
 
- Easy-to-use currency selector interface
 

---

#### 

8\. Edge Cases & Validations

**Boundary Testing**

- Minimum (`0.001`) and maximum currency values are handled correctly
 
- Very large 3-decimal numbers are processed without overflow
 

**Error Handling**

- Graceful handling of payment gateway downtime
 
- Conversion failure fallback with user-friendly errors
 
- Robust error messages for failed transactions or invalid input
 

**Test Data Validation**

All of the following passed and display as expected:

- `0.001`, `0.999`, `1.000`, `123.456`, `999.999`, `1000.000`
 

---

#### 

9\. Outcome

You can now seamlessly process, display, convert, and refund 3-decimal currency values in Agency Handy—ensuring high accuracy and a smooth user experience across the board.

---

### 

10\. Important Notes

- **Not all currencies are available for payment processing.** IQD, MGA, and MRU are display-only.
 
- **Precision is maintained across all systems**—UI, database, and API.
 
- **Stripe only supports selected currencies**—always verify current availability.
 

---

[VorherigeTimesheet](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/timesheet) [NächsteFrench](https://docs.agencyhandy.com/french)

Zuletzt aktualisiert vor 11 Monaten