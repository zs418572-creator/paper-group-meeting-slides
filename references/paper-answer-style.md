# Paper Answer Style

## Default structure

Use this order flexibly:

1. One-sentence answer.
2. Intuitive explanation.
3. Concrete example or numerical calculation.
4. Mechanism or formula.
5. Common misconception.
6. Relation to the audience's field when relevant.
7. One or two self-check questions.

Connect the explanation to the audience's field only when the relationship is meaningful.

## When comparing concepts

State both:

- what is similar;
- what is different;
- which analogy is useful;
- where the analogy breaks.

Example:

> BSRNN_init 像 WavLM 的地方是 pretrain-finetune 范式；不像的地方是 WavLM 使用自监督通用表征，而 BSRNN_init 是同任务的监督式热启动。

## When the user gives a personal takeaway

Keep the meaning of the user's wording. Fix only:

- factual mistakes;
- misleading terminology;
- overclaims;
- grammar that impedes the presentation.

Do not replace the user's takeaway with a generic polished conclusion.

## Evidence labels

Use labels such as:

- `论文验证`
- `论文没有拆解，这是合理推断`
- `需要实验确认`
- `如果直接照搬，风险是……`

Never present an inferred optimization reason as a proven mechanism.

## When introducing authors or publication context

Use this only when the author team or publication path genuinely helps the audience read the paper.

- Give the first author, senior/corresponding author, and one or two directly relevant affiliations.
- Name one or two prior works that explain why this team is prepared for the problem.
- State the verifiable venue/year and publication context; omit unverified review details.
- Finish with the reading implication, not with praise.

Keep it to 30–60 seconds. Separate “作者/团队背景” from “论文本身的证据”; author reputation never proves the paper's claims.



## Tone

- Direct, patient, and technical.
- Chinese by default.
- Keep English terms when they are standard.
- Avoid marketing language, vague praise, and generic filler.
- Use numbers and tensor/audio shapes whenever the concept benefits from them.
