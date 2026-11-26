# Provider Integration Plan

The challenge brief suggests the following baseline stack. Treat these as recommendations from the supplied brief, not guarantees of current access or fixed model availability.

| Stage | Suggested option in brief | Where to run |
|---|---|---|
| Story/script/translation | Gemini Flash family | Gemini API / Google AI Studio |
| Amharic narration | Gemini Flash TTS | Gemini API |
| Keyframes | FLUX.2 Klein or FLUX.1 Schnell | Cloudflare Workers AI |
| Moving shots | Wan 2.2 TI2V-5B; HunyuanVideo alternative | Kaggle or Colab GPU |
| Original score | ACE-Step 1.5 | Colab/Kaggle GPU |
| Assembly | FFmpeg | Local computer or Colab |
| Coding agent | Antigravity CLI or OpenCode | Development machine |

## Integration acceptance criteria

For every provider adapter:

1. Read credentials/model identifiers from environment variables or Colab Secrets.
2. Never log API secrets or private prompt data unnecessarily.
3. Log model identifier/revision, parameters, seed (where supported), latency, status, output path, and cost estimate.
4. Save the provider response immediately.
5. Retry transient failures with a bounded retry policy; do not retry permanent invalid-request/authentication errors blindly.
6. Handle rate limits and quota exhaustion with a documented fallback.
7. Preserve provider watermark/provenance metadata where present.
8. Record the provider's licence and data-use terms in `ETHICS.md`.

The starter kit does not hardcode model IDs or claim that API integrations are active. Verify the live official API/model documentation and free-tier conditions before wiring each adapter.
