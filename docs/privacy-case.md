# The Privacy Case: Why Local Matters

The strongest argument for a SHOAL is not cost. It is data sovereignty.

## The Problem with Cloud AI

Every prompt you send to ChatGPT, Claude, or Gemini travels to a third-party server. The provider's privacy policy governs what happens next: whether your data trains future models, how long it is retained, who can access it, and under what legal jurisdiction.

For casual personal use, this is often fine. For professional use with client data, it is a risk that regulated professions are increasingly uncomfortable with.

## Who Cares Most

### Law Firms

ABA Formal Opinion 512 (July 2024) addresses confidentiality obligations when lawyers use generative AI. The guidance highlights risks including data leakage, hallucination, and the duty to understand how AI tools handle client information.

A SHOAL sidesteps the cloud-data question entirely. Prompts about client matters never leave the building. No BAA to negotiate. No vendor privacy policy to parse. No risk of a cloud provider's training pipeline ingesting your client's privileged communications.

### Medical and Dental Practices

HIPAA requires that any system handling Protected Health Information (PHI) meet specific security and privacy standards. Cloud AI providers can be made HIPAA-compliant through Business Associate Agreements, but negotiating and maintaining BAAs adds cost and complexity that small practices struggle with.

A local AI server processing clinical notes, appointment summaries, or patient communication drafts keeps PHI entirely within the practice's physical and network perimeter.

### Real Estate Offices

Client financial information, mortgage details, contract negotiation drafts, and property records all flow through a real estate office daily. While real estate lacks the regulatory teeth of HIPAA or legal ethics rules, the practical exposure is similar: a data breach involving client financial data is a liability and reputation event.

### Families

The motivations are softer but real:
- Kids' conversations with AI should not train commercial models
- Family discussions (health, finances, relationships) stay in the house
- No ad targeting derived from AI conversation content
- The AI works during internet outages
- One hardware purchase replaces multiple monthly subscriptions

## What "Local" Does Not Mean

Local AI is not automatically secure. The reef is a computer on your network with a filesystem full of chat logs. For genuine high-stakes confidentiality:

- Enable full-disk encryption on the reef
- Use strong passwords on Open WebUI accounts
- Segment the reef onto its own VLAN if the network serves untrusted devices
- Physically secure the reef machine (it should not be in the lobby)
- Back up the Open WebUI data volume, and store backups encrypted

"Local" means your data does not leave your network perimeter. It does not mean you can skip basic security hygiene.

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
