# Source: https://docs.agencyhandy.com/faq/add-on-setup-in-services.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/faq/add-on-setup-in-services.md).

# Add-on Setup in Services

#### \*\*FAQs: Add-on Setup in Services – AgencyHandy\*\*

1. \*\*What is an add-on in AgencyHandy?\*\*\\
 An add-on is an additional service that clients can select alongside a primary service, enhancing customization and flexibility in their orders.
2. \*\*Who can create add-ons in AgencyHandy?\*\*\\
 Only users with administrative access or the necessary permissions can create and manage add-ons.
3. \*\*How do I access the add-on configuration page?\*\*\\
 Navigate to the "Services" section in your dashboard and select "Add-ons" to access the configuration page.
4. \*\*What information is required to create a new add-on?\*\*\\
 You need to provide a name, description, pricing type (one-time or subscription), amount, and currency for the add-on.
5. \*\*Can I set different pricing types for add-ons?\*\*\\
 Yes, you can choose between one-time or subscription pricing for each add-on.
6. \*\*Is there a limit to the number of add-ons I can create?\*\*\\
 There is no specified limit; you can create as many add-ons as needed to complement your services.
7. \*\*How do I publish an add-on after creation?\*\*\\
 After entering all necessary details, click "Save" to add the new add-on and then publish it to make it available for selection.
8. \*\*Can I edit an existing add-on?\*\*\\
 Yes, you can edit the details of an existing add-on by accessing it through the "Add-ons" section.
9. \*\*How do I associate an add-on with a specific service?\*\*\\
 Go to the “Form” section, select the appropriate order form, and connect the relevant add-ons to the service via the “Add-ons” tab.
10. \*\*Can clients choose multiple add-ons for a single service?\*\*\\
 Yes, clients can select multiple add-ons when purchasing a service, depending on your configuration.
11. \*\*Is it possible to make an add-on mandatory for a service?\*\*\\
 Yes, during configuration, you can set add-ons as optional or mandatory extras for the service.
12. \*\*How do I remove an add-on from a service?\*\*\\
 Navigate to the order form, go to the “Add-ons” tab, and deselect the add-on you wish to remove from the service.
13. \*\*Can I delete an add-on entirely?\*\*\\
 Yes, you can delete an add-on from the "Add-ons" section; however, ensure it's not linked to any active services.
14. \*\*Will clients see the add-ons during the checkout process?\*\*\\
 Yes, once add-ons are connected to a service, clients will see them listed as optional or mandatory extras during checkout.
15. \*\*Can I offer discounts on add-ons?\*\*\\
 Currently, there is no direct feature to apply discounts to add-ons; consider adjusting the price manually if needed.
16. \*\*Are add-ons visible in the client portal?\*\*\\
 Yes, clients can view available add-ons associated with services in their portal during the purchasing process.
17. \*\*Can I track the popularity of specific add-ons?\*\*\\
 While there's no dedicated analytics for add-ons, you can monitor client selections and orders to gauge popularity.
18. \*\*Is it possible to duplicate an existing add-on?\*\*\\
 Currently, duplication isn't supported; you'll need to create a new add-on with similar details manually.
19. \*\*Do add-ons support different currencies?\*\*\\
 Yes, you can select the appropriate currency for each add-on during setup.
20. \*\*Can I schedule add-ons to be available only during specific periods?\*\*\\
 There isn't a built-in scheduling feature; you'll need to manually publish or unpublish add-ons as needed.
21. \*\*How do I ensure add-ons are mobile-friendly?\*\*\\
 AgencyHandy is designed to be responsive; add-ons will display appropriately on mobile devices during the client checkout process.
22. \*\*Can I categorize add-ons for better organization?\*\*\\
 While there's no specific categorization feature, you can use naming conventions to group similar add-ons.
23. \*\*Will clients receive invoices that include selected add-ons?\*\*\\
 Yes, invoices will reflect all selected add-ons along with the primary service details.
24. \*\*Is there a way to preview how add-ons appear to clients?\*\*\\
 You can simulate the client experience by navigating through the checkout process to see how add-ons are displayed.
25. \*\*Can I restrict certain add-ons to specific client groups?\*\*\\
 Currently, add-ons are linked to services and order forms; to restrict access, consider creating separate services or forms for different client groups.
26. \*\*Can I add any type of add-on to any service in AgencyHandy?\*\*

 No, in AgencyHandy, add-ons must match the pricing type of the service they are associated with.

 \* \*\*One-time add-ons\*\* can only be linked to \*\*one-time services\*\*.
 \* \*\*Subscription-based add-ons\*\* can only be linked to \*\*subscription-based services\*\*.
27. \*\*How are add-ons processed when purchased with a service in AgencyHandy?\*\*

 In AgencyHandy, when a client selects add-ons alongside a primary service, each add-on is processed as a separate order. Although the charges for the main service and its associated add-ons are billed simultaneously, distinct orders are created for each add-on. This approach ensures individualized tracking and management for each component of the client's purchase.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/faq/add-on-setup-in-services.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.