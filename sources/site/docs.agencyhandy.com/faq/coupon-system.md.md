# Source: https://docs.agencyhandy.com/faq/coupon-system.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/faq/coupon-system.md).

# Coupon System

#### Agency Handy Coupon System – Frequently Asked Questions

\*\*1. What is the Coupon System in Agency Handy?\*\*

The Coupon System allows Super Admins and Admins to create, manage, and apply discount coupons to services. It supports various discount types, usage restrictions, and service-specific applications.

\*\*2. Who can create and manage coupons?\*\*

Only users with Super Admin or Admin roles have the permissions to create and manage coupons within Agency Handy.

\*\*3. How do I create a new coupon?\*\*

Navigate to the "Services" section, click on "Coupons," and then select “+ Add Coupon.” Fill in the required details such as name, applicable services, discount type, amount, redemption limits, expiration date, and usage restrictions.

\*\*4. What types of discounts can I offer?\*\*

You can offer either percentage-based discounts (e.g., 10% off) or fixed-amount discounts (e.g., $50 off). Discounts can be up to 100% of the service price.

\*\*5. Can I set a limit on how many times a coupon can be redeemed?\*\*

Yes, you can specify the total number of times a coupon can be redeemed across all clients.

\*\*6. Is it possible to set an expiration date for a coupon?\*\*

Absolutely. You can define an expiration date after which the coupon will no longer be valid.

\*\*7. What does 'Duration of the Code Redeem' mean?\*\*

This setting determines how long the discount applies after redemption:

\* \*\*Forever\*\*: The discount applies indefinitely.
\* \*\*Once\*\*: The discount applies only once.
\* \*\*Multiple Cycles\*\*: The discount applies for a specified number of billing cycles.

\*\*8. Can I restrict coupons to specific services?\*\*

Yes, during coupon creation, you can select one or multiple services to which the coupon will apply.

\*\*9. Is it possible to limit coupon usage to specific clients or client groups?\*\*

Yes, you can specify restrictions such as one-time use per customer, new customers only, or limit options for specific clients.

\*\*10. How do clients redeem coupons?\*\*

Clients can enter valid coupon codes during the checkout process. The system will verify the coupon's eligibility based on activation status, service applicability, and other defined criteria.

\*\*11. Can clients apply multiple coupons to a single purchase?\*\*

Yes, clients can apply multiple valid coupons during checkout. The system will calculate the combined discount on the order total.

\*\*12. Will the discount be visible during checkout?\*\*

Yes, discounts appear in the order summary, allowing clients to review the adjusted total before finalizing the payment.

\*\*13. How do I manage existing coupons?\*\*

In the “Coupons” section, you can edit, deactivate, or delete coupons. Note that deleting a coupon is irreversible and will stop any associated recurring discounts.

\*\*14. What happens if I delete a coupon that's currently in use?\*\*

Deleting an active coupon will immediately discontinue any discounts associated with it on active recurring subscriptions. It's recommended to inform clients in advance to avoid dissatisfaction.

\*\*15. Are there any currency considerations when creating coupons?\*\*

Yes, certain currencies do not support decimal values. In such cases, discount amounts will be rounded to the nearest whole number. Ensure accurate configuration for each currency to maintain consistency.

\*\*16. Which currencies do not support decimal discounts?\*\*

Currencies like BIF, CLP, DJF, GNF, JPY, KMF, KRW, MGA, PYG, RWF, UGX, VND, VUV, XAF, XOF, and XPF do not support decimal values and will round discounts to the nearest whole number.

\*\*17. How does the system define a 'new customer'?\*\*

A new customer is identified by an email address not previously recorded in the purchase database. The system checks the email against existing records to determine if it's a first-time purchase.

\*\*18. Can I temporarily deactivate a coupon without deleting it?\*\*

Yes, you can toggle the activation status of a coupon in the “Coupons” section without permanently deleting it.

\*\*19. What precautions should I take before deleting a coupon?\*\*

Before deleting a coupon, consider:

\* Communicating the change to affected clients.
\* Aligning the deletion with the end of a billing cycle.
\* Offering alternative discounts to maintain goodwill.
\* Preparing customer support for potential inquiries.

\*\*20. Is there a way to handle fractional discounts in currencies that don't support decimals?\*\*

In such cases, the system will automatically round the discount to the nearest whole number. To avoid discrepancies, ensure that this rounding aligns with your pricing strategy.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/faq/coupon-system.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.