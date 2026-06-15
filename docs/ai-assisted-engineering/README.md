# AI-Assisted Engineering

AI tools can help teams explore ideas, draft code, write tests, summarize context, and improve documentation. They work best when they are part of normal engineering practice: a responsible person still owns the work, the team still validates the output, and project decisions still follow the customer and team context.

Use this guide as the shared baseline for AI-assisted engineering. Domain guides such as [Developer Experience](../developer-experience/README.md), [Automated Testing](../automated-testing/README.md), [Security](../security/README.md), [Observability](../observability/README.md), [Source Control](../source-control/README.md), [Code Reviews](../code-reviews/README.md), and [Documentation](../documentation/README.md) provide more specific guidance.

## When to Use AI Assistance

Use AI assistance for work where a draft, explanation, or candidate implementation can accelerate learning and delivery:

- Drafting boilerplate, examples, tests, documentation, diagrams, and review notes
- Explaining unfamiliar code, logs, errors, dependencies, or infrastructure templates
- Generating implementation options, refactoring ideas, threat-model prompts, and test scenarios
- Summarizing requirements, backlog items, architecture notes, and design tradeoffs
- Exploring alternatives before the team makes a decision

Avoid relying on AI alone for work that requires accountability, project-specific judgment, or policy interpretation:

- Architecture decisions, security-sensitive logic, privacy decisions, and release approvals
- Consequential decisions that affect people, access, eligibility, finance, health, safety, or legal status
- Customer data handling, regulated data handling, retention decisions, and disclosure obligations
- Production incident response, destructive operations, and changes to cloud or production resources
- Claims about compliance, licensing, vulnerability status, performance, or model behavior without evidence

## Human Oversight

Treat AI output as draft material until a responsible person reviews, tests, and accepts it.

- Keep a named human owner for every AI-assisted pull request, design decision, deployment, and customer-facing artifact.
- Review AI-generated code and text with the same or higher care as hand-written work.
- Check generated claims against source material, product documentation, requirements, and customer context.
- Reject generated output that is unrelated, unexplainable, unverifiable, over-broad, or inconsistent with the team architecture.
- Preserve normal engineering controls, including peer review, branch protection, CI checks, security review, accessibility review, and rollback planning.

## Data and Context Hygiene

AI tools should receive the minimum context needed to complete the task.

- Confirm which AI tools are approved for the project, customer, data classification, and engagement model before work starts.
- Do not paste secrets, credentials, private customer data, regulated data, or unnecessary proprietary context into AI tools.
- Prefer synthetic, representative, anonymized, or redacted examples when exploring prompts or reproducing issues.
- Remove access tokens, connection strings, personal data, customer identifiers, and confidential business details from prompts, screenshots, logs, and attachments.
- Understand tool retention, logging, telemetry, training, and data residency behavior before using project or customer context.
- Keep prompts and retrieved context scoped to the task. Extra context can increase leakage risk and produce less accurate output.

## Prompt and Repository Hygiene

Good AI results depend on accurate project context.

- Keep build, test, lint, setup, and run commands easy to find in repository documentation.
- Document project conventions, architectural boundaries, dependency choices, and coding standards where tools and people can discover them.
- Use repository instruction files, prompt files, or agent configuration only when the team has agreed on their purpose and maintenance owner.
- Avoid instructions that ask AI tools to bypass tests, ignore security review, hide generated changes, or make broad edits outside the task.
- Keep reusable prompts factual and current. Remove outdated assumptions when architecture, tooling, or customer constraints change.

## Security

Treat model output as untrusted input.

- Review generated code for injection, authorization, authentication, cryptography, dependency, logging, and error-handling issues.
- Do not execute generated commands or scripts until a responsible person understands their effect.
- Scope AI agent tools, credentials, file access, cloud permissions, and network access to the least privilege needed for the task.
- Add threat-model coverage for prompt injection, insecure output handling, sensitive information disclosure, excessive agency, unsafe tool calls, model or data poisoning, model theft, and AI supply chain risk.
- Validate generated dependency, container, infrastructure, and CI/CD changes against the normal security review path.

## Testing and Evaluation

AI assistance does not reduce the need for evidence.

- Review generated tests for meaningful assertions, realistic setup, negative cases, and failure modes.
- Add deterministic automated tests for ordinary software behavior.
- Add AI-specific evaluations when product behavior depends on prompts, retrieval, models, agents, generated content, ranking, summarization, or recommendations.
- Evaluate quality, groundedness, safety, bias, robustness, tool-call correctness, regression behavior, and fallback behavior where relevant.
- Keep evaluation datasets, rubrics, expected outcomes, and known limitations versioned with the system or linked from the project documentation.

## Observability

AI-enabled systems need enough telemetry for teams to debug behavior and detect drift while respecting privacy and policy constraints.

- Track model and configuration versions, prompt template versions, retrieval sources, tool calls, latency, token or cost signals, errors, fallback paths, safety outcomes, evaluation scores, and human escalation.
- Avoid logging raw prompts, completions, secrets, personal data, customer data, or sensitive retrieval content unless the project has an explicit approved logging design.
- Connect production signals to incident response, rollback, model or prompt change review, and customer support workflows.
- Review observability data for quality regression, unexpected tool use, abuse patterns, and changes in model behavior over time.

## Authorship and Traceability

Teams should be able to understand where AI materially influenced engineering work.

- Follow the team's convention for documenting material AI assistance in pull requests, commit metadata, work items, or decision records.
- Keep generated changes small enough to review and explain.
- Link AI-assisted decisions to the same evidence expected for other decisions: requirements, tests, evaluations, design notes, customer constraints, and review comments.
- Do not use AI-generated summaries as the only record of customer decisions or stakeholder approval.
- Make sure generated comments, release notes, and documentation do not claim behavior that has not been implemented and validated.

## Accessibility and Inclusion

AI can help identify accessibility and inclusion issues, but it does not replace user research, accessibility testing, or assistive-technology review.

- Review AI-generated UI, content, flows, and images for accessibility, inclusive language, cognitive load, localization, and cultural context.
- Validate generated UI with the same accessibility requirements used for the rest of the product.
- Test important experiences manually with keyboard navigation, screen readers, color contrast checks, and other assistive technology where appropriate.
- Include affected users, domain experts, and accessibility reviewers when AI-enabled behavior changes the user experience.

## Governance

AI guidance should be adapted to the project risk, customer policy, and system impact.

- Decide early which tools are approved, which data they can access, who owns review, and how exceptions are handled.
- Add AI policy and setup questions to project onboarding, first-week planning, team working agreements, and definitions of done where relevant.
- Route higher-risk AI work through Responsible AI assessment, privacy review, security review, design review, accessibility review, legal or compliance review, and stakeholder approval as appropriate.
- Document material limitations, known failure modes, monitoring expectations, and human escalation paths for AI-enabled features.
- Revisit the guidance when tools, customer constraints, model capabilities, or production usage change.

## Related Playbook Areas

- [Developer Experience](../developer-experience/README.md) and [Copilots](../developer-experience/copilots.md) for AI tool setup and attribution patterns
- [Automated Testing](../automated-testing/README.md) for test strategy and evaluation practices
- [Security](../security/README.md) for secure engineering practices and threat modeling
- [Observability](../observability/README.md) for telemetry and operational readiness
- [Source Control](../source-control/README.md) and [Code Reviews](../code-reviews/README.md) for review, traceability, and change control
- [Data Handling](../non-functional-requirements/privacy/data-handling.md) for privacy and data protection practices
- [Accessibility](../non-functional-requirements/accessibility.md) for inclusive and accessible delivery
- [Responsible AI](../ml-and-ai-projects/responsible-ai.md) for AI system impact assessment
