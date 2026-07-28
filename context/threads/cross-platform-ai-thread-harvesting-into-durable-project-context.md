---
title: "Cross-Platform AI Thread Harvesting into Durable Project Context"
primary_topic: "Cross-platform AI thread harvesting into durable project context"
source_platform: "Claude"
capture_mode: "full-paste"
completeness: "partial"
extraction_depth: "comprehensive"
requested_extraction_depth: "highly detailed"
source_title: "Hey, Claude. I'm trying to figure out the difference between Claude Chat, Claude Code Work, and Claude Code"
source_date: "unknown"
source_time_context: "Claude paste timing unknown; Notion snapshot fetched 2026-06-07"
source_locator: "User-supplied Claude thread URL redacted; pasted-text.txt attachment; Notion page fetched read-only with URL redacted"
retention_decision: "redacted"
source_independence: "pass"
generated_at: "2026-07-25T03:21:12Z"
schema_version: "2.0"
artifact_type: thread-context-extract
---

# Cross-Platform AI Thread Harvesting into Durable Project Context

## Introduction

This Claude Chat conversation explores a durable workflow for moving valuable mobile-first AI conversations into persistent, version-controlled project context. The discussion begins by distinguishing ephemeral chat threads from persistent project or cowork workspaces, then develops a proposed ingestion pattern: use a private repository as a staging container, apply a reusable agent skill with platform adapters, harvest selected threads from Claude, ChatGPT, Perplexity, or Copilot, distill decisions and reusable assets, and commit the resulting context. The conversation favors a recurring triage rhythm over a one-time migration, identifies SSH as the proposed cross-machine Git authentication method, and considers browser-assisted process capture. The final state is intentionally provisional because several Claude product capabilities, including the named “cohort mode,” browser control, local tool access, and screen/process observation, were not verified in the supplied conversation.

## Extraction profile

- **Requested depth:** highly detailed synthesis and conversion
- **Selected depth:** comprehensive
- **Selection basis:** The user explicitly requested a highly detailed result, which maps to the comprehensive profile.
- **Profile changes:** None.
- **Focus areas:** Durable project context, cross-platform harvesting, reusable agent-skill design, private repository operations, cross-machine execution, and verification of Claude capabilities.
- **Must preserve:** The proposed workflow, platform-adapter architecture, privacy and repository decisions, SSH recommendation, process-capture idea, unresolved capability claims, and actionable next steps.
- **Safe exclusions:** Conversational filler and repeated acknowledgements were compressed. No substantive reasoning was intentionally omitted.
- **Coverage rule:** Each substantive user and assistant block is represented in the turn ledger. Repeated affirmations and closing acknowledgements are grouped where they add no new decision. Referenced but unavailable external pages are cataloged as missing sidecars.
- **Not carried forward:** Raw private-looking URLs, unsupported claims presented as facts, and a verbatim transcript. The source remains available at the user-supplied attachment if lossless review is needed.
- **Source-independence test:** pass for understanding the proposed workflow and resuming design; blocked for validating current Claude product capabilities because the original UI and linked pages were not supplied.

## Coverage accounting

| Material class | Assessed | Retained | Compressed | Omitted with reason | Missing or unavailable | Notes |
|---|---:|---:|---:|---:|---:|---|
| Turns or turn groups | 25 | 25 | 3 | 0 | 0 | Visible pasted sequence assessed in order; role assignment is based on alternating user/Claude blocks in the supplied capture.
| Rich elements | 5 | 1 | 0 | 0 | 4 | Notion page project context was fetched read-only and retained in redacted form; private operational details and source URLs were not retained.
| Decisions and alternatives | 12 | 12 | 0 | 0 | 2 | Private repository and SSH are proposed decisions; product capability details remain unresolved.
| Reusable assets | 8 | 8 | 0 | 0 | 1 | The skill/runbook structure is retained as a design; no actual skill scaffold or runbook was supplied.

## Source synopsis

The primary supplied source is a pasted Claude Chat conversation titled from its opening prompt about the difference between Claude Chat, Claude Code Work, and Claude Code, and whether existing threads can be moved into project context. The capture method is not explicitly identified, but the visible text reads like a control-copy or export-style flattening of a voice conversation. It contains a sequence of user statements and Claude responses, ending with the standard Claude disclaimer. No exact source date, Project name, Project instructions, uploaded files, Artifact contents, citations, screenshots, or tool output are included.

The user also supplied a Notion page titled “SHOAL: Shared Home/Office AI, Locally.” It was fetched read-only during this extraction and returned a dated snapshot from 2026-06-07. Safe project-level context confirms that SHOAL is an active OverKill Hill P³ project associated with the `shoal-ai-server` repository, uses the reef/fish/shoal/ocean vocabulary, and frames the project as a shared local AI-server pattern for homes and small offices. The page describes related compute and persona projects and records that the repository documentation and naming were being developed in June 2026. The page also contained machine-specific addresses, workspace paths, account identifiers, and detailed deployment claims; those details were classified as sensitive or drift-prone and excluded from this artifact.

The user is not primarily seeking a one-time migration of a known small set of threads. The underlying need is a repeatable intake and cleansing system for a large backlog of legacy ChatGPT conversations and fewer than fifty Claude Chat threads. The user often enters conversations from a mobile device, where chat and voice are convenient, but wants valuable conversations to become durable context for projects, repositories, an AI brain, or related private work. The desired operating model is a periodic or event-driven “purge and cleanse” process rather than an expectation that every chat becomes active project context.

Claude's responses propose a distinction between ephemeral conversation history and persistent workspaces. The responses state that there is no direct bulk migration path and recommend manually preserving valuable decisions, prompts, artifacts, and context. The user then proposes using a locally connected cowork or coding environment with browser and local-file access to automate the visible copy and staging process. Claude reframes that as a browser-assisted harvesting orchestrator that navigates chat history, extracts selected material, and writes Markdown or other artifacts to a local repository.

The conversation then converges on a reusable agent skill. Its stable core would accept a source platform and batch of threads, apply keeper criteria, normalize and distill content, categorize it, stage it in an ingestion repository, and commit the result. Platform-specific navigation and extraction behavior would be isolated behind adapters for Claude, ChatGPT, Perplexity, and Copilot. The source suggests folders such as raw extracts, distilled decisions, and reusable artifacts, while warning that the skill should remain narrow and let downstream projects consume the results.

Operationally, the user asks whether the ingestion repository should be public or private and how to authenticate two machines. Claude recommends a private repository because the workflow may handle personal conversations and could eventually encounter credentials or API keys, and recommends SSH over PATs for persistent Git automation. This is a proposed operating choice, not a verified security conclusion for every environment. The conversation also considers teaching the automation by demonstrating a workflow while Claude observes and records clicks, URLs, selectors, text patterns, timing, and decision rules. The final exchange corrects the earlier certainty: “cohort mode” and the exact scope of browser, screen-observation, and local-tool features were not known and must be verified in the actual Claude interface before architecture is built around them.

## Turn ledger

| Turn | Role | Role confidence | Boundary evidence | Content elements | Summary |
|---|---|---|---|---|---|
| T001 | user | medium | Opening question followed by an assistant answer | E001 | Asks about Claude Chat, Claude Code Work, Claude Code, threads, projects, and migration.
| T002 | assistant | medium | Response block ending with a question | E001 | Distinguishes chat history from persistent workspaces and proposes manual distillation; direct bulk migration is stated but not verified.
| T003 | user | medium | New first-person block | none | Clarifies that the need is a workflow pattern and mentions a backlog of older chats.
| T004 | assistant | medium | Response block ending with a question | none | Recommends triage, keeper criteria, and starting sustained work in Projects from the beginning.
| T005 | user | medium | New first-person block | none | Proposes browser and local-tool automation to copy Claude chats into local project artifacts.
| T006 | assistant | medium | Response block ending with a question | none | Reframes the idea as a browser-assisted local-repository harvesting workaround and raises rate-limit and keeper-heuristic concerns.
| T007 | user | medium | New first-person block | none | Estimates fewer than fifty Claude threads and describes mobile intake plus periodic cleansing.
| T008 | assistant | medium | Response block ending with a question | none | Proposes a recurring cadence, an intake Project, repository folders, and mobile tagging.
| T009 | user | medium | New first-person block | none | Suggests converting the repeatable workflow into an agent skill and using an ingestion repository.
| T010 | assistant | medium | Response block ending with a question | none | Supports an agent skill, names possible scope, and recommends keeping it narrow and versionable.
| T011 | user | medium | New first-person block | none | Asks whether separate skills are needed for Claude, GPT, Perplexity, and Copilot.
| T012 | assistant | medium | Response block ending with a question | none | Recommends one configurable core with platform adapters and flags divergence as a future split criterion.
| T013 | user | medium | New first-person block | none | Adds cross-machine execution on an Asus Windows laptop and Mac Studio with local clones and apps.
| T014 | assistant | medium | Response block ending with a question | none | Recommends a private repository and synchronized local clones; mentions Git credentials as an operational dependency.
| T015 | user | medium | New first-person block | none | Asks whether SSH keys or PATs provide a more consistent ingestion process.
| T016 | assistant | medium | Response block ending with a question | none | Recommends SSH for persistence and lower rotation overhead; the recommendation should be reviewed against local security practice.
| T017 | user | medium | New first-person block | none | Asks whether Claude can observe a manual process and turn it into an assembly-line workflow.
| T018 | assistant | medium | Response block ending with a question | none | Proposes narrated process capture and codification, while noting deterministic workflows and decision trees are prerequisites.
| T019 | user | medium | New first-person block | none | Asks how long the named “cohort mode” has been available.
| T020 | assistant | medium | Explicit uncertainty correction | none | Retracts certainty about the feature name and advises checking current Projects capabilities.
| T021 | user | medium | New first-person block | E002 | Notes the conversation is happening in mobile voice mode rather than a desktop UI.
| T022 | assistant | medium | Response block ending with a question | none | Advises bookmarking the thread and verifying available tools on Mac Studio or Asus before designing the runbook.
| T023 | user | medium | Short affirmation | none | Accepts the verification step.
| T024 | user | medium | Short affirmation | none | Confirms agreement again.
| T025 | assistant | medium | Closing response and disclaimer | E003 | Acknowledges completion; standard disclaimer is UI/source chrome, not a substantive decision.

## Content element ledger

| Element | Turn | Type | Owner | Fidelity | Source locator | Destination reference | Catalog action |
|---|---|---|---|---|---|---|---|
| E001 | T001-T002 | ui_chrome | unknown | metadata-only | Opening/title context inferred from supplied text | Metadata and source synopsis | exclude-chrome |
| E002 | T021 | audio_video | user | description-only | User states mobile voice mode; audio payload and transcript metadata not supplied | Source synopsis and normalization exceptions | flag-missing |
| E003 | T025 | ui_chrome | assistant | text-extracted | Standard Claude disclaimer at end of pasted text | Turn ledger only | exclude-chrome |
| E004 | source context | citation | unknown | referenced-not-supplied | User supplied Claude and Notion links outside the pasted transcript; private-looking URLs redacted in artifact | Provenance and open questions | flag-missing |
| E005 | source context | file | unknown | text-extracted | Read-only Notion fetch of “SHOAL: Shared Home/Office AI, Locally”; source URL redacted | Source synopsis, value inventory, and provenance | retain |

## Normalization exceptions

- The pasted text has no explicit `User` and `Claude` labels on every block. Roles are assigned from the clear alternating conversational structure and response-ending questions, so confidence is medium rather than high.
- The capture method is not stated. It is recorded as `full-paste` because the user supplied a flattened visible conversation in one attachment, but this remains an interpretation. The artifact does not claim a complete export.
- The conversation references a Claude thread URL and a Notion page, but their contents were not provided and no source-platform login or page fetch was performed. They are not runtime dependencies and are redacted from the artifact's source locator.
- The Notion page was available through the connected read-only Notion source and was fetched once. Its safe project-level context is retained, while machine addresses, local paths, account identifiers, and other operational details are excluded.
- The phrase “Claude Code Work” and the phrase “cohort mode” appear in the supplied conversation. Their exact product meanings and availability are unresolved. The source itself later acknowledges uncertainty, so earlier capability claims are retained only as conversation proposals or claims needing verification.
- No actual browser trace, DOM selector, API response, repository scaffold, agent skill, commit, or automation run was supplied. These are proposed outputs, not completed work.
- “Voice mode” is recorded as a source-context description. The actual audio recording, device metadata, and any omitted spoken material are unavailable.

## Value inventory

| Area | Extracted value | Claim class | Source support |
|---|---|---|---|
| Purpose | Create a repeatable intake valve that turns mobile-first AI conversations into durable, searchable project context. | stated | T003, T007, T009 |
| Context and constraints | Large legacy ChatGPT backlog, fewer than fifty Claude threads, mobile convenience, two machines with local repositories, a desire to preserve only material worth future reuse, and an existing SHOAL repository/project context that can act as a related destination or model. | stated | T003, T007, T013; E005 |
| Reasoning and alternatives | Prefer recurring triage over bulk preservation; prefer a unified core plus platform adapters over four unrelated skills; keep the ingestion repository private; use SSH as the proposed Git authentication method. | proposal / inferred | T004, T010, T012, T014, T016 |
| Decisions and outcomes | Treat the workflow as a candidate agent skill and private ingestion repository, subject to capability verification and keeper-criteria design. | unresolved / proposal | T009-T010, T014, T020-T022 |
| Reusable assets | Keeper rubric, intake-repository taxonomy, normalized cross-platform record, adapter architecture, runbook cadence, process-capture checklist, and verification gate. | proposal | T004, T008, T010, T012, T018 |

## Decisions and rationale

### Accepted working direction

1. **Use an ingestion repository as the durable staging container.** The repository should separate raw or minimally normalized captures from distilled decisions and reusable artifacts. This supports review, traceability, and Git history. The source proposes the structure but does not define a final schema.
2. **Implement one narrow cross-platform skill with adapters.** The stable pipeline should be platform-neutral: intake, privacy review, normalization, keeper triage, extraction, categorization, staging, and verification. Claude, ChatGPT, Perplexity, and Copilot differences should be isolated to source-specific capture adapters. This is a design proposal, not an implemented architecture.
3. **Use a recurring triage rhythm.** A monthly cadence or a threshold such as ten to fifteen accumulated threads is proposed. A mobile user may also trigger a run when a cluster begins to form. The exact cadence is unresolved.
4. **Keep the ingestion repository private.** The rationale is that the source material may include personal conversations and future credentials or sensitive context. Secrets should never be stored in the repository. A public, generalized skill may be separated later from the private ingestion data.
5. **Treat SSH as the proposed two-machine Git authentication path.** The source favors SSH because it avoids PAT rotation during unattended or repeated runs. Key storage, passphrase handling, agent forwarding, revocation, and machine compromise risks still require an explicit security design.

### Significant alternatives and rejected or deferred options

- **Direct bulk migration from chat history into a Project:** treated as unavailable or unsupported in the source discussion. This must be independently verified before being used as a product fact.
- **Manual copy and paste for every thread:** retained as a fallback and as a validation method for the automation, but considered unsuitable as the long-term process at backlog scale.
- **Four independent platform skills:** deferred in favor of one core plus adapters. A split becomes justified if platform differences create substantially different safety, navigation, or output contracts.
- **Automating before defining “keeper”:** explicitly discouraged. The workflow needs a decision rubric before batch harvesting, or it risks creating a second archive of noise.

## Actionable handoff

- **Current state:** The workflow is a well-formed concept, not an implemented skill or automation. The source ends at the point where the user must inspect current Claude Projects and local-tool capabilities.
- **Resume point:** Verify capabilities on the Mac Studio or Asus, then write a platform-neutral intake contract and keeper rubric before building browser automation.
- **Required context:** This artifact, the repository's `AGENTS.md`, the actual Claude/Codex application capabilities, the intended private GitHub repository, and the user's privacy/retention rules.

| Action | Owner | Status | Dependencies | Evidence or acceptance condition |
|---|---|---|---|---|
| Inspect Claude Projects and local-app/browser capabilities on both machines | user | ready | Physical access to Mac Studio and Asus; current product UI | Record exact available tools, authentication boundaries, browser control, file access, and process-observation behavior.
| Define keeper criteria and a triage rubric | user + agent | ready | Examples of threads and desired downstream destinations | A reviewer can classify a thread as retain, distill, archive-only, or discard with consistent rationale.
| Define normalized thread and extract schemas | agent | proposed | Keeper rubric and downstream project needs | Schema captures source, completeness, turns, rich elements, claims, decisions, actions, and provenance.
| Scaffold the private ingestion repository | user + agent | proposed | Private GitHub repository decision; folder/schema approval | Repository contains sanitized instructions, skills, schemas, and staging folders without credentials or raw private data.
| Prototype one manual Claude batch | user + agent | proposed | Verified source capture method | At least three threads produce traceable Markdown extracts and a review log.
| Add platform adapters incrementally | agent | proposed | Successful Claude prototype and platform-specific capture evidence | Each adapter produces the same normalized record and documents its limitations.
| Add Git review and commit workflow | user + agent | proposed | SSH setup on both machines and repository policy | Dry-run, diff review, secret scan, commit, and sync are documented and tested.
| Establish recurring cadence or trigger threshold | user | unresolved | Observed backlog volume and effort per batch | A practical monthly or threshold-based runbook exists and has an owner.
| Independently verify claims about migration, browser tools, and “cohort mode” | user | blocked | Current first-party product documentation or live UI inspection | Each capability is labeled confirmed, unavailable, or unknown with evidence.

## Reusable methods and assets

### Proposed normalized pipeline

`source selection -> capture boundary -> privacy gate -> turn and element normalization -> keeper triage -> detailed extraction -> destination routing -> review/diff -> commit -> downstream handoff`

### Proposed repository taxonomy

```text
ingestion-repo/
├── AGENTS.md
├── skills/
│   └── thread-harvest-intake/
├── schemas/
│   ├── normalized-thread.md
│   └── extract-record.md
├── captures/
│   ├── claude/
│   ├── chatgpt/
│   ├── perplexity/
│   └── copilot/
├── extracts/
│   ├── decisions/
│   ├── prompts/
│   ├── artifacts/
│   └── research/
├── review/
└── runbooks/
```

This layout is a proposal derived from the conversation, not an existing repository structure. Raw captures should be private, minimized, and retained only when the user's policy permits them. Sanitized extracts should preserve provenance and distinguish source claims from verified facts.

### Keeper rubric to prototype

Retain or distill a thread when it contains one or more of: a consequential decision and rationale; a reusable prompt or method; a durable artifact or specification; project context that is difficult to reconstruct; a research finding with traceable sources; or an unresolved question that materially affects future work. Archive without active extraction when the problem is solved, context is duplicative, or no reusable asset remains. Escalate rather than automate when the thread contains secrets, regulated data, third-party confidential information, or unresolved ownership/consent concerns.

### Platform-adapter contract

Each adapter should report the source platform, capture method, completeness, source locator, selected thread identifiers, visible turns, rich elements, missing sidecars, rate limits or operational constraints, and confidence in boundaries. It should not assume that UI text is a lossless export. The core extractor should consume this normalized record without depending on DOM selectors or platform-specific terminology.

### Process-capture checklist

When demonstrating the workflow, record the starting state, authentication boundary, navigation sequence, selection rule, scroll/pagination behavior, extraction boundary, file naming, error/retry behavior, rate-limit handling, human approval points, and final diff review. Treat observed actions as a draft runbook until repeated successfully on more than one thread.

## Open questions and limits

- Does Claude currently provide the browser, local-file, repository, or process-observation capability assumed by the conversation? The source explicitly leaves this unresolved.
- Is “cohort mode” an actual current feature name, an internal label, or a misunderstanding? Do not use it as an implementation dependency without evidence.
- Is there a supported direct migration or export path between Claude Chat and Projects? The source claims no direct bulk path, but provides no current primary-source evidence.
- What exactly is meant by “Claude Code Work,” and how does it differ from Claude Chat, Claude Projects, or another product surface?
- What thread export or browser capture methods are allowed by each platform's terms, privacy controls, and account model?
- What is the authoritative destination taxonomy: project repository, AI brain, Notion, or another private knowledge base? The supplied Notion page is a referenced source/context anchor, not a resolved write destination.
- What data must never enter the ingestion repository, even privately? Define secret, personal, employer-confidential, regulated, and third-party retention rules.
- What is the minimum viable keeper rubric, and who reviews uncertain classifications?
- How are duplicates, superseded decisions, contradictions, and links between a source thread and downstream project context represented?
- How will SSH keys be protected on both machines, and what is the recovery/revocation plan?
- How will browser automation handle login state, MFA, pagination, rate limits, layout changes, failures, and human approval?
- The conversation contains no actual attachments, Claude Artifacts, citations, screenshots, DOM trace, or code. Those items must be captured separately if they affect implementation.
- The fetched Notion snapshot is dated 2026-06-07 and may not represent the current project state. Its hardware, pricing, deployment, legal, and technical claims require independent verification before publication or automation design.

## Rehydration test

| Test | Result | Evidence or gap |
|---|---|---|
| A reader can explain the objective without the source platform | pass | The objective, backlog context, target workflow, and intended output are in the synopsis and handoff.
| Decisions and consequential rationale are recoverable | pass | Private repository, unified adapter architecture, triage rhythm, SSH proposal, and capability-verification gate are documented in Decisions and rationale.
| Current state and next action are unambiguous | pass | The next action is live capability inspection followed by keeper-rubric and schema design.
| Retained assets are available or missing assets are explicitly cataloged | pass | Proposed schemas, taxonomy, pipeline, rubric, and checklist are included; absent browser traces and external pages are cataloged.
| No source account, thread, project, canvas, or connector is a runtime dependency | pass | The artifact is self-contained for workflow design; external links are provenance only and redacted.

- **Overall source-independence result:** pass for workflow continuity and design; capability validation remains blocked as an external verification task.
- **Blocked capability, if any:** The artifact cannot confirm the current behavior or availability of Claude product features discussed in the source.

## Provenance and retention

- **Capture boundary:** One user-supplied pasted-text attachment containing a flattened Claude conversation excerpt, plus one read-only fetch of the explicitly supplied Notion page titled “SHOAL: Shared Home/Office AI, Locally.” The original Claude account, Claude Project context, and omitted Claude sidecars were not accessed.
- **Completeness:** partial. The supplied text appears to cover one visible conversation, but completeness of the original thread and any voice, UI, Project, artifact, or attachment context is unknown.
- **Source time context:** unknown. The current target date is 2026-07-24, but no source conversation date or export time was supplied.
- **Retention decision:** redacted. The artifact retains the durable workflow synthesis while omitting raw transcript text and redacting private-looking source URLs.
- **Source caveats:** Role boundaries are inferred from the flattened sequence; the Claude source includes assistant claims that require verification; the Notion page was fetched as a dated snapshot and contains claims and operational details that were selectively excluded; no lossless archive was created; and the repository's tracked artifact should remain free of credentials, tokens, private URLs, machine-specific paths, and raw sensitive conversation content.
