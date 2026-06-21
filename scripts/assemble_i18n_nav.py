#!/usr/bin/env python3
"""Assemble the 27 new-language navigation blocks into docs.json.

Reads translated nav labels from i18n-nav-labels.json (produced by the
translate-all-languages workflow) and builds one `navigation.languages`
entry per language from the canonical English structure, prefixing every
page path with the language code. Existing en/fr/es blocks are preserved.
"""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
DOCS = os.path.join(ROOT, "docs.json")
LABELS = os.path.join(ROOT, "i18n-nav-labels.json")

# Language codes Mintlify's language switcher accepts. Codes outside this set
# (e.g. bn, fa, th, lt, mn) are rejected by `mint dev` schema validation.
SUPPORTED = {
    "en", "cn", "zh", "zh-Hans", "zh-Hant", "es", "fr", "fr-CA", "fr-ca",
    "ja", "jp", "ja-jp", "pt", "pt-BR", "de", "ko", "it", "ru", "ro", "cs",
    "id", "ar", "tr", "hi", "sv", "no", "da", "lv", "nl", "uk", "vi", "pl",
    "uz", "he", "ca", "fi", "hu",
}

# Canonical English structure: tab label-key -> list of groups.
STRUCTURE = [
    ("tab_for_agency", [
        ("group_get_started", "rocket", True,
         ["getting-started/introduction", "getting-started/sign-up",
          "getting-started/log-in", "getting-started/dashboard-overview"]),
        ("group_workspace_setup", "settings", False,
         ["workspace/general-settings", "workspace/appearance",
          "workspace/custom-domain", "workspace/email-setup", "workspace/portals"]),
        ("group_crm", "users", False, ["crm/leads", "crm/clients"]),
        ("group_services_orders", "package", False,
         ["services/overview", "services/create-service", "orders/overview",
          "orders/create-order", "orders/tasks"]),
        ("group_proposals_invoices", "file-text", False,
         ["proposals/overview", "invoices/overview", "invoices/create-invoice",
          "invoices/subscriptions"]),
        ("group_team_tasks", "circle-check", False,
         ["teams/manage-team", "tasks/all-tasks", "tasks/timesheet",
          "tickets/support-tickets"]),
        ("group_forms_files", "layout-template", False,
         ["forms/order-forms", "forms/intake-forms", "files/manage-files"]),
        ("group_account_billing", "credit-card", False,
         ["account/profile", "account/plans-pricing", "account/multiple-workspaces"]),
        ("group_payments", "wallet", False,
         ["integrations/stripe", "integrations/paypal", "integrations/other-payments"]),
        ("group_integrations", "plug", False,
         ["integrations/slack", "integrations/webhooks"]),
    ]),
    ("tab_for_client", [
        ("group_getting_started", "rocket", True,
         ["client/introduction", "client/accessing-portal"]),
        ("group_orders_services", "package", False,
         ["client/browse-and-order", "client/orders-and-tasks"]),
        ("group_billing", "credit-card", False,
         ["client/proposals", "client/invoices-payments"]),
        ("group_support", "life-buoy", False,
         ["client/files-and-forms", "client/support-tickets"]),
    ]),
    ("tab_api_reference", [
        ("group_introduction", "book-open", True, ["api/getting-started"]),
        ("group_endpoints", "code", False,
         ["api/create-lead", "api/create-client", "api/update-order"]),
    ]),
]


def build_language(code, labels):
    tabs = []
    for tab_key, groups in STRUCTURE:
        g_out = []
        for gkey, icon, expanded, pages in groups:
            grp = {"group": labels[gkey], "icon": icon}
            if expanded:
                grp["expanded"] = True
            grp["pages"] = [f"{code}/{p}" for p in pages]
            g_out.append(grp)
        tabs.append({"tab": labels[tab_key], "groups": g_out})

    return {
        "language": code,
        "global": {
            "anchors": [
                {"anchor": labels["anchor_home"], "icon": "house", "href": f"/{code}"},
                {"anchor": labels["anchor_app"], "icon": "arrow-up-right",
                 "href": "https://app.agencyhandy.com"},
                {"anchor": labels["anchor_community"], "icon": "users",
                 "href": "https://community.agencyhandy.com"},
            ]
        },
        "navbar": {
            "links": [],
            "primary": {"type": "button", "label": labels["button_sign_in"],
                        "href": "https://app.agencyhandy.com"},
        },
        "tabs": tabs,
    }


def main():
    with open(DOCS) as f:
        docs = json.load(f)
    with open(LABELS) as f:
        all_labels = json.load(f)

    langs = docs["navigation"]["languages"]
    new_codes = [c for c in all_labels if c in SUPPORTED]
    unsupported = [c for c in all_labels if c not in SUPPORTED]
    if unsupported:
        print(f"skipping unsupported language codes: {unsupported}")

    # Drop any pre-existing blocks for codes we're about to (re)generate, then append.
    langs = [l for l in langs if l["language"] not in set(new_codes)]
    for code in new_codes:
        langs.append(build_language(code, all_labels[code]))
    docs["navigation"]["languages"] = langs

    with open(DOCS, "w") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"docs.json updated. languages now: {[l['language'] for l in langs]}")
    print(f"added/regenerated: {new_codes}")


if __name__ == "__main__":
    main()
