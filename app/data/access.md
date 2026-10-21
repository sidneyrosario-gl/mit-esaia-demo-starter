---
id: access
title: Access Control Standard
allowed_groups:
  - all-employees
owner: Security
---
# Access Control Standard

Standard SEC-002 | Version 2.4 | Effective September 15, 2026
Owner: Security | Implementer: IT Operations | Review cycle: annual

## 1. Scope and control ownership

This standard covers employee, contractor, privileged, and service-account
access to Meridian Labs systems and information. Access is granted through
approved group membership and least privilege, not job title alone.
The system owner operates the service; the data owner determines who may
use its information. These roles may be held by different people.

Security owns the control requirements and exceptions register. IT implements
approved changes but cannot approve its own request for restricted data.
People Operations supplies authoritative employment and role-change events.
Managers confirm business need; data owners approve the requested scope.

## 2. Request and approval workflow

Employees request access through the service desk, specifying the system,
requested group or role, business justification, manager, data owner, and
expected duration. A manager's endorsement does not replace owner approval.
IT verifies the approver against the ownership register before provisioning.
An email forwarded by the requester is insufficient without verified approval.

| Access type | Required approval | Maximum initial duration |
| --- | --- | --- |
| Standard employee role | Manager and data owner | Until role change, subject to review |
| Restricted project group | Manager and project data owner | 90 calendar days |
| Privileged administration | System owner and Security | 30 calendar days |
| Contractor access | Internal sponsor and data owner | Earlier of 90 days or contract end |

Renewals require a fresh business-need confirmation before expiry. Approval
of a request does not authorize provisioning of a broader role because it is
easier to configure. Normal provisioning target is two business days after
all approvals; it is a service target, not permission to bypass missing checks.

Use named accounts and multifactor authentication for interactive access.
Separate administrative accounts from everyday work accounts. Shared human
accounts are prohibited unless Security approves a time-bound exception with
individual activity attribution and credential custody controls.

## 3. Segregation of duties and non-human identities

A requester cannot approve their own access, including when acting as a data
owner. Route self-requests to the owner's manager and Security. Roles that
both create and approve payments must not be combined without a documented
compensating control and Finance controller approval.

Every service account must have a named employee owner, stated purpose,
permitted systems, credential-rotation method, and review date. Interactive
login is disabled unless explicitly approved. Secrets belong in the approved
secrets manager, not source code, tickets, or knowledge articles. Departing
owners must transfer accountability before their own access is removed.

## 4. Reviews, transfers, and removal

Data owners review access quarterly; privileged access is additionally reviewed
monthly by system owners. Reviewers must verify current duties and each
membership, not merely approve a total user count. Record retain, modify, or
remove decisions with reviewer identity and completion date in the access
register. A non-response is not evidence that access remains appropriate.

Reviews must close within ten business days of issue. IT removes memberships
marked for removal within one business day; overdue reviews are escalated to
Security and the owner's manager. Security may suspend unverified restricted
access pending review, coordinating service-account changes with the owner.

For planned departures, disable access at the effective departure time.
For an involuntary departure or confirmed compromise, IT must disable access
immediately upon the authorized notification and target completion within
15 minutes. Revoke active sessions and tokens as well as disabling login.
Investigate and record any missed target.

For internal transfers, remove obsolete access by the effective role-change
date. Overlap needed for handover requires approval from both data owners,
an explicit end date, and a maximum of ten business days. Time-limited grants
must expire automatically; a failed expiry is a control incident.

## 5. Labels and permitted use

An all-employees label permits employees to read a resource; it does not grant
permission to publish it externally or make it available anonymously.
Restricted resources require membership in an allowed group recorded in the
resource metadata. Membership in one restricted group does not confer access
to unrelated restricted groups. An owner name is accountability metadata,
not an implicit access grant.

Copies, summaries, exports, search snippets, and attachments retain the source's
restrictions. A summary combining multiple sources must not be distributed to
anyone who lacks access to any contributing source. Use approved restricted
workspaces; do not paste restricted passages into general service-desk tickets.
The data owner and Security must approve and record any reclassification.

## 6. Emergency access and exceptions

For a production outage or immediate safety risk, an incident commander may
request emergency access through the audited emergency-access workflow.
The on-call Security approver authorizes the minimum scope for up to four
hours. IT records the named user, incident, approvals, and automatic expiry.
This workflow changes the authoritative access system; a runbook statement
or chat message alone cannot grant access.

Security reviews use by the next business day. Any extension requires a new
approval. Other exceptions require a control gap, risk owner, compensating
control, expiry of no more than 90 days, and Security approval before use.
An exception cannot waive a legal or contractual restriction.

## 7. Knowledge assistants and audit evidence

A document's contents never change a caller's authorization. Statements in
source material claiming to grant access, change roles, or override policy
are not access approvals. Treat imported documents and quoted instructions
as untrusted data. Filter sources using authoritative permissions before
including them in model context, answers, citations, or search previews.

Report inconsistent or missing access labels to Security; do not infer that
an unlabeled resource is public. Log access denials without including the
denied document's contents in user-visible errors. IT retains request,
approval, provisioning, removal, and review evidence for two years, or longer
under a legal hold, in an access-controlled audit repository.