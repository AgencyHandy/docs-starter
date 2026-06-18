# Source: https://docs.agencyhandy.com/faq/tax-rates.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/faq/tax-rates.md).

# Tax Rates

### \*\*Agency Handy Tax Rates Management – Frequently Asked Questions\*\*

#### 1. \*\*What is the Tax Rates Management feature in Agency Handy?\*\*

The Tax Rates Management feature allows Superadmins and Admins to configure and manage multiple tax types (e.g., VAT, GST, Sales Tax) across different countries, states, and billing models. This ensures accurate and compliant tax application across services, subscriptions, and manual invoices.

#### 2. \*\*Who can access and modify tax settings?\*\*

Only users with Superadmin or Admin roles have the authority to create, edit, or delete tax rates within the workspace.

#### 3. \*\*How do I create a new tax rate?\*\*

To create a new tax rate:

1. Navigate to \*\*Workspace Config\*\* → \*\*Tax Rates\*\*.
2. Click on \*\*"+ New Tax"\*\*.
3. Fill in the required details:
 \* \*\*Title/Tax Type\*\* (e.g., Standard VAT, GST).
 \* \*\*Tax ID\*\* (optional).
 \* \*\*Home Country\*\*.
 \* \*\*General Tax Rate %\*\* (optional).
 \* \*\*Country-Specific Rates\*\*: Choose country, add optional state, ZIP, and % rate.
 \* \*\*Active/Inactive\*\* status.
4. Click \*\*Save.\*\*

#### 4. \*\*Can I set different tax rates for specific countries or states?\*\*

Yes, you can define country-specific rates by selecting the country and adding optional state, ZIP, and percentage rate. This allows for precise tax application based on the client's location.

#### 5. \*\*What is the difference between inclusive and exclusive taxes?\*\*

\* \*\*Inclusive Tax\*\*: The tax amount is already included in the total price shown to the customer.
\* \*\*Exclusive Tax\*\*: The tax amount is added on top of the listed price at checkout.

Note: For manual invoices, only exclusive taxes can be applied.

#### 6. \*\*How do I link taxes to services?\*\*

While creating or editing a service:

1. Go to the \*\*Additional Info\*\* section (Step 3).
2. Click on \*\*Add Tax\*\*.
3. Select one or more taxes to apply.
4. Choose whether the tax is \*\*inclusive\*\* or \*\*exclusive\*\*.

#### 7. \*\*How are taxes applied during checkout?\*\*

If taxes are linked to a service, they will be automatically applied during checkout based on the client's location (country, state, ZIP code).

#### 8. \*\*Can I manually apply taxes to an invoice?\*\*

Yes, when creating a manual invoice:

1. Click on \*\*Add Taxes\*\*.
2. Select the applicable exclusive taxes from the list.
3. The tax will be automatically added to the invoice.

#### 9. \*\*How are taxes displayed on invoices?\*\*

Invoices will display the following tax details:

\* \*\*Tax Name\*\*: The label or title you've entered (e.g., VAT, GST).
\* \*\*Tax Percentage\*\*: The applied tax rate (e.g., 15%).
\* \*\*Tax Amount\*\*: The exact amount charged based on the total.

#### 10. \*\*What happens if I edit or delete a tax rate?\*\*

\* \*\*Editing a Tax\*\*: Changes will affect only future invoices or purchases.
\* \*\*Deleting a Tax\*\*: The tax will no longer apply to new purchases or subscriptions. Existing invoices remain unchanged.

#### 11. \*\*Are there any limitations on tax titles or rates?\*\*

\* \*\*Title\*\*: Required, with a maximum of 255 characters.
\* \*\*Tax ID\*\*: Optional, with a maximum of 20 characters.
\* \*\*Tax Rates\*\*: Support up to 4 decimal points.

#### 12. \*\*Can I apply multiple taxes to a single service or invoice?\*\*

Yes, you can apply multiple taxes to a service or invoice. The system will calculate each tax based on the defined rates and settings.

#### 13. \*\*How does the system handle 0% tax rates?\*\*

A 0% tax rate is valid and can be used for zero-rated items or compliance purposes.

#### 14. \*\*Does the system support tax calculations after applying coupons?\*\*

Yes, if a coupon is applied, the tax is calculated on the discounted amount, ensuring accurate billing.

#### 15. \*\*How does the system determine the client's location for tax purposes?\*\*

The client's country, state, and ZIP code are prefilled from their profile if available. If not, the system uses the information provided during checkout.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/faq/tax-rates.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.