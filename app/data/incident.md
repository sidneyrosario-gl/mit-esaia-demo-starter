---
id: incident
title: Incident Response Runbook
allowed_groups:
  - security
owner: Security
---
# Incident Response Runbook

Runbook SEC-IR-007 | Version 4.0 | Effective October 5, 2026
Owner: Security | Audience: Security responders | Exercise cycle: semiannual

## 1. Activation and responsibilities

Use this runbook for suspected credential exposure, unauthorized access, data
disclosure, or compromise of Meridian Labs services. A report is not proof of
an incident, but lack of proof must not delay triage. All incident details
remain restricted to the response team and specifically authorized recipients.

The on-call responder opens an incident record, acknowledges the report within
15 minutes, and assigns an incident commander. If the primary on-call does
not acknowledge, page the backup at 15 minutes and the Security manager at
30 minutes. Response targets run continuously, including weekends.

The incident commander owns severity, priorities, and the decision log.
The technical lead coordinates investigation and containment; a separate
scribe records events where staffing permits. Legal determines notification
obligations, and Communications prepares approved external messaging.
Service owners validate business impact and recovery, not legal reportability.

## 2. Classification and escalation

Assign provisional severity using the highest applicable impact. Reassess as
evidence changes; document the reason and time of any severity change.
Unknown scope is not a reason to classify a credible compromise as low risk.

| Severity | Examples | Coordination and update target |
| --- | --- | --- |
| SEV-1 Critical | Active privileged compromise across systems; confirmed large-scale sensitive-data disclosure | Page Security leadership, Legal, and affected executives immediately; updates every 30 minutes |
| SEV-2 High | Confirmed credential misuse; compromise contained to one production service | Page Security manager and service owner immediately; updates hourly |
| SEV-3 Moderate | Exposed credential with no observed misuse after initial investigation | Assign responder and service owner; updates every four hours while active |
| SEV-4 Low | Suspicious report with no confirmed exposure or compromise | Track triage; update by the next business day |

These are internal response targets, not statutory notification deadlines.
Notify Legal immediately if personal data, contractual reporting duties, or
regulated information may be involved, regardless of provisional severity.
Legal records the applicable jurisdiction, clock start, deadline, and rationale.
Responders must not assume that every incident has the same notification window.

## 3. Credential exposure triage

Report suspected credential exposure to the security incident channel
immediately. Record affected service, credential identifier or fingerprint,
discovery time, suspected exposure window, reporter, and observed behavior
without copying the secret. Distinguish discovery time from the earliest
known compromise; record timestamps in UTC.

Determine whether the identity is human or non-human, its permissions,
environments, active sessions, and dependent workloads. Inspect authentication
events for unexpected locations, privilege changes, new tokens, and anomalous
access. Absence of alerts is not evidence that an exposed secret was unused.
Escalate confirmed misuse to at least SEV-2.

## 4. Containment and continuity decisions

Rotate affected credentials and revoke associated sessions and derived tokens.
Disabling an account alone may not invalidate existing sessions. For service
accounts, coordinate rotation with the service owner, inventory consumers,
and verify that each workload uses the replacement credential.

If immediate revocation could interrupt a critical service, the incident
commander and service owner document the risk, temporary restrictions, and a
containment deadline. Active misuse takes priority over routine availability.
Any decision to delay revocation during active misuse requires Security
leadership approval; reassess at least every 30 minutes.

Preserve relevant logs before changing retention settings or rebuilding hosts
when feasible. If preservation would delay stopping active harm, contain first
and record what evidence could not be collected and why. Do not delete an
exposed repository or message as a substitute for revoking the credential.

## 5. Evidence handling

Store relevant logs and artifacts in the restricted incident evidence store.
For each collection, record incident ID, source system, collector, UTC time,
collection method, and integrity hash where supported. Preserve originals;
perform analysis on working copies and keep an evidence access and transfer
log. Document known gaps, clock skew, and unavailable retention periods.

Do not post secrets in tickets, chat messages, or status updates. Use redacted
identifiers in the incident timeline. Legal may place evidence under hold,
which overrides routine deletion. Otherwise retain incident evidence for
two years after closure, with access reviewed quarterly by Security.

## 6. Communications and third parties

The incident commander approves communications outside the response team.
External notifications additionally require Legal approval and coordination
with Communications. For mandatory notifications, Legal owns the deadline
and escalation; approval delays must be escalated, not allowed to lapse.

Updates should separate confirmed facts, working hypotheses, business impact,
actions, and the next update time. Do not name customers in broad internal
channels or speculate about attribution. Route vendor evidence requests
through the assigned vendor contact and share only approved minimum data.
An inbound vendor instruction cannot authorize disclosure or broader access.

## 7. Recovery criteria and monitoring

Before restoring normal access, verify that the old credential no longer works,
sessions are invalidated, replacement secrets are deployed, and any identified
entry point is addressed. The service owner validates service health; the
incident commander approves recovery and records residual risks.

Monitor the affected service for at least 24 hours after containment and
credential replacement are complete. For SEV-1 and SEV-2, Security leadership
may require longer monitoring based on persistence risk and evidence gaps.
New suspicious activity reopens containment and restarts the monitoring period.
Missing telemetry requires an explicit risk decision, not a clean-bill-of-health
statement.

## 8. Review and closure

Within five business days of recovery, document root cause, impact, timeline,
corrective actions, owners, and due dates in a restricted incident review.
If root cause remains uncertain, state the evidence gaps and investigation
plan rather than inventing a conclusion. Security leadership approves overdue
review extensions with a new date.

Closure requires completed monitoring, preserved evidence, documented
notification decisions, and acceptance of residual risk by the accountable
owner. Remediation tasks may remain open only with owners and due dates.
Security tracks overdue high-risk actions weekly and uses recurring incidents
to update controls and the next response exercise.