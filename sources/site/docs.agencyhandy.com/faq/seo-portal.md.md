# Source: https://docs.agencyhandy.com/faq/seo-portal.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/faq/seo-portal.md).

# SEO Portal

SEO Portal – FAQs for AgencyHandy

\* \*\*What is the SEO Portal feature in AgencyHandy?\*\*\\
 The SEO Portal allows users to configure the Meta Title, Meta Description, and Meta Image for shared workspaces or custom domains, ensuring consistent and professional link previews across various platforms.
\* \*\*Who can access and modify the SEO Portal settings?\*\*\\
 Only Super Admins and Admins with the necessary permissions can configure the SEO Portal settings.
\* \*\*How do I access the Meta settings in AgencyHandy?\*\*\\
 Log in to your AgencyHandy account, navigate to Workspace Settings → Portal SEO, and click on Meta Title & Description Settings.
\* \*\*What is a Meta Title, and why is it important?\*\*\\
 A Meta Title is the main heading that appears in link previews. It provides a concise summary of the page's content, influencing click-through rates.
\* \*\*What is a Meta Description, and how does it affect link previews?\*\*\\
 A Meta Description is a brief summary that appears below the Meta Title in link previews, offering additional context and encouraging users to click the link.
\* \*\*What are the recommended character limits for Meta Titles and Descriptions?\*\*\\
 Meta Titles should be concise, ideally under 120 characters, and Meta Descriptions should be under 300 characters to ensure optimal display across platforms.
\* \*\*Can I upload a custom image for link previews?\*\*\\
 Yes, you can upload a custom Meta Image in JPEG, PNG, or JPG format, with a recommended size of 1200×630 px and a maximum size of 5 MB.
\* \*\*How do I preview the changes made to Meta settings?\*\*\\
 A mockup of the link preview appears on the right side during editing, showing how it will look on platforms like LinkedIn, Slack, and WhatsApp.
\* \*\*Is there an option to reset Meta settings to default?\*\*\\
 Yes, by clicking the 'Reset to Default' button in the top right corner, all custom metadata will revert to the default workspace settings.
\* \*\*What happens when I reset to default metadata?\*\*\\
 All custom Meta Title, Description, and Image settings will be removed, and the workspace will use the default metadata. This action is irreversible.
\* \*\*Why isn't my custom Meta Image displaying correctly?\*\*\\
 Ensure the image is within the size limit (5 MB), in a supported format (JPEG, PNG, JPG), and meets the recommended dimensions (1200×630 px).
\* \*\*Why are my Meta Title or Description not appearing in link previews?\*\*\\
 Clear your browser cache and refresh the link preview. Some platforms cache metadata, so changes might not reflect immediately.
\* \*\*How can I force social platforms to update the link preview?\*\*\\
 Use tools like Facebook Debugger to refresh the cache and update the link preview on social platforms.
\* \*\*Can I customize metadata for each workspace or domain separately?\*\*\\
 Yes, you can configure unique Meta Titles, Descriptions, and Images for each shared workspace or custom domain.
\* \*\*What are best practices for writing effective Meta Titles?\*\*\\
 Use clear, specific titles that reflect the workspace's purpose, keeping them concise and descriptive for better visibility.
\* \*\*What are best practices for crafting Meta Descriptions?\*\*\\
 Highlight key benefits or important information, summarizing the page's content to encourage user engagement.
\* \*\*How often should I update my Meta settings?\*\*\\
 Update Meta settings whenever there's a significant change in content or branding to ensure link previews remain accurate and engaging.
\* \*\*Do changes to Meta settings affect SEO rankings?\*\*\\
 While Meta Titles and Descriptions don't directly impact SEO rankings, they influence click-through rates, which can indirectly affect rankings.
\* \*\*Can I use the same Meta Image across multiple workspaces?\*\*\\
 Yes, you can use the same Meta Image for consistency, but ensure it accurately represents each workspace's content.
\* \*\*What should I do if my changes aren't saving?\*\*\\
 Ensure all required fields are filled correctly, the image meets the specified criteria, and you have the necessary permissions. If issues persist, contact support.
\* \*\*Is there a way to test how my link preview looks on different platforms?\*\*\\
 While AgencyHandy provides a mockup, you can also use platform-specific tools like Facebook Debugger or LinkedIn Post Inspector for testing.
\* \*\*Can I schedule changes to Meta settings for future updates?\*\*\\
 Currently, AgencyHandy doesn't support scheduling Meta setting changes; updates take effect immediately upon saving.
\* \*\*Are there any restrictions on the content of Meta Titles and Descriptions?\*\*\\
 Avoid using special characters or excessive capitalization. Ensure the content is relevant, concise, and free from misleading information.
\* \*\*How does the Meta Image influence user engagement?\*\*\\
 A clear, professional Meta Image can enhance the visual appeal of your link preview, increasing the likelihood of user interaction.
\* \*\*Can I revert to previous Meta settings after making changes?\*\*\\
 Once changes are saved or reset to default, previous settings can't be retrieved. It's advisable to document settings before making significant changes.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/faq/seo-portal.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.