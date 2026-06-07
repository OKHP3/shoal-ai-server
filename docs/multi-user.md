# Multi-User Setup: Accounts, Roles, and Kid-Safe Models

Open WebUI handles user management out of the box. The first person to sign up becomes the admin. Everyone after that gets a "pending" account until the admin approves them.

## User Roles

| Role | Can Chat | Can Change Settings | Can Manage Users | Can See All Models |
|------|----------|---------------------|------------------|-------------------|
| Pending | No | No | No | No |
| User | Yes | Limited | No | Only models assigned to their group |
| Admin | Yes | Yes | Yes | Yes |

## Creating User Accounts

Two approaches:

1. **Open registration.** Leave signups open, approve each one manually. Good for families.
2. **Admin-created accounts.** The admin creates accounts in Settings > Admin > Users. Better for offices.

## Groups and Model Permissions

This is where SHOAL gets powerful for families and offices.

**The pattern:** Create user groups (e.g., "Adults," "Kids," "Attorneys," "Support Staff"), then assign model visibility per group.

1. Go to **Admin Settings > Groups**
2. Create a group (e.g., "Kids")
3. Add the relevant users
4. Set permissions: disable Tools Access, disable Web Search, restrict to specific models

**Important:** Open WebUI permissions are additive. To restrict a feature, it must be disabled in the Global Defaults AND disabled in all groups the user belongs to. If any group grants a permission, the user has it.

## Creating a Kid-Safe Model

The "curated model" pattern is the right approach for child safety:

1. Go to **Workspace > Models > Create a Model**
2. Set a friendly name (e.g., "Study Buddy")
3. Write a system prompt that enforces age-appropriate boundaries:
   - "You are a helpful homework assistant for middle school students."
   - "Do not discuss violence, drugs, alcohol, or adult content."
   - "If asked about topics outside your scope, say 'Let's ask a parent about that.'"
4. Set the base model to your installed Ollama model
5. Set visibility to **Restricted**
6. Grant access only to the "Kids" group
7. Keep the unrestricted base model **Private** (admin-only) or restricted to the "Adults" group

**Critical safety note:** Open WebUI's Tools Access permission is documented as "root-equivalent, equivalent to giving them shell access to your server." Never grant Tools Access to child accounts.

## Office Setup Example

A small law firm with 4 attorneys and 2 support staff:

| Group | Members | Models Visible | Tools Access | Web Search |
|-------|---------|---------------|--------------|------------|
| Attorneys | 4 | Full model (unrestricted) | Yes | Yes |
| Support | 2 | "Office Assistant" (curated, no legal research) | No | No |

The attorneys get the full model for contract review, case research, and document drafting. Support staff get a curated model scoped to scheduling, correspondence, and general office tasks.

## Session Isolation

Each user's chat history is private to their account. User A cannot see User B's conversations. The admin can see aggregate usage but not individual chat content (unless they access the database directly).

## What's Next

- [Privacy and data sovereignty](privacy-case.md) for regulated professions
- [Remote access](remote-access.md) for out-of-office use

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
