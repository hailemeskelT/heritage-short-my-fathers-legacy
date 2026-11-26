# AI-Content Generation — The Heritage Short
## Project report: My Father's Legacy

**Participant:** [YOUR NAME]  
**Repository:** [PUBLIC GITHUB URL]  
**Film title:** የአባቴ ውርስ — My Father's Legacy  
**Narration language:** Amharic  
**Submission date:** 26 November 2026

## 1. Executive summary

This project developed an AI-assisted short documentary based on a
family account about the filmmaker's father and his legacy in North
Shewa, Ethiopia. The film communicates agricultural diligence, love
and ethical values in family life, community respect, customary
mediation and reconciliation, and lessons passed between generations.

The production workflow uses a structured ten-shot storyboard,
open-weight image generation with SSD-1B, Amharic text-to-speech,
programmatically synthesized instrumental music, English subtitles,
and FFmpeg-based video assembly. The target deliverables are vertical
9:16 and horizontal 16:9 MP4 versions.

## 2. Story, audience and intent

The source is a family account. It describes the father as a diligent
farmer, a loving parent who worked to raise the family with good values,
and a respected community member who participated in customary
mediation and reconciliation.

The intended audience is the filmmaker's family, Ethiopian young
people and viewers interested in family heritage and community values.

The intent is to help viewers appreciate diligence, love, respect,
patience and reconciliation, and to encourage the preservation of
family stories across generations.

The account did not provide a specific village, exact date, crop,
individual dispute or historical event. The visual scenes are
illustrative AI reconstructions and must not be understood as
historical photographs.

## 3. Creative development

The storyboard contains ten shots. Each shot has a narration line,
English subtitle, visual prompt, motion prompt and duration.

The visual direction uses North Shewa-inspired highland scenery,
natural earthy colours and a fictional, non-identifiable father figure.
The father is shown without reproducing the real person's likeness.

The visual style aims for a respectful documentary treatment rather
than a literal reconstruction of undocumented events.

## 4. System architecture

The storyboard JSON is the central production contract.

The image-generation stage uses Segmind SSD-1B through Hugging Face
Diffusers on a Google Colab Tesla T4. The narration is generated with
Edge TTS using an Amharic voice. The score is an original,
programmatically synthesized instrumental track. FFmpeg assembles the
images, camera movement, narration, music, English subtitles and
AI-disclosure end card into two aspect ratios.

The initial starter pipeline included validation, planning, logging,
media utilities and assembly code. Notebook stages were used during
production. The exact cache behaviour, retries and end-to-end CLI
reproducibility are documented only to the extent verified in the
repository.

## 5. Implementation and reproducibility

The project was developed in Google Colab with a Tesla T4 GPU.
The storyboard was validated as ten shots with an original target
duration of 68 seconds.

The first SSD-1B test image was 1024x1024 JPEG, generated in
approximately 27 seconds, with a reported peak GPU allocation of
3.32 GB. A long prompt exceeded the CLIP token limit and was shortened.

Validation and planning commands were tested. The full production
workflow was executed through the notebook. A fresh-clone test of a
single end-to-end command must be reported only after it has actually
been completed.

## 6. Audience tests and design changes

### 6.1 Radio cut test

Date: [ACTUAL DATE]  
Audience participants: [AT LEAST THREE]

What participants said:
[RECORD ACTUAL FEEDBACK, ANONYMISED.]

What changed in the narration, storyboard or timing:
[RECORD ACTUAL CHANGES.]

### 6.2 Near-final film test

Date: [ACTUAL DATE]  
Audience participants: [AT LEAST THREE]

What participants said:
[RECORD ACTUAL FEEDBACK, ANONYMISED.]

What changed in the final edit:
[RECORD ACTUAL CHANGES.]

## 7. Experiments and evidence

The experiments are documented in `EXPERIMENTS.md`. They cover
storyboard validation, planning, placeholder inspection, MP4 inspection,
source-code inspection, paid API limitations, SSD-1B loading, VAE
configuration, CLIP prompt truncation, and first-image generation.

The detailed evidence and any further experiments are recorded in
`runs.jsonl` and `COSTS.md`. Missing measurements are identified rather
than invented.

## 8. Hardest problem and resolution

The production encountered several connected environment and model
issues: paid image API access, Diffusers VAE API differences, notebook
state loss, Google Drive account migration, and a prompt longer than
the CLIP context limit.

The most significant image-generation issue was prompt truncation:
a 231-token prompt exceeded the 77-token limit. The prompt was shortened
to concise, shot-specific visual descriptions. The first SSD-1B test
image was then generated successfully.

The project also had to be restored into a second Google account after
a Colab GPU restriction. The ZIP did not contain generated media, so
the storyboard was restored and missing outputs were recreated.

## 9. Suggested practices tested honestly

### Practice that helped more than expected

Using `storyboard.json` as a shared production contract made it easier
to inspect the ten scenes, preserve the Amharic narration and revise
visual prompts without rewriting the story.

Evidence: storyboard validation, the ten-shot plan and the prompt
revision record.

### Practice that did not work as expected

Using long, highly detailed image prompts did not improve the output
because the CLIP tokenizer truncated text beyond 77 tokens.

Evidence: the 231-token warning. Shorter prompts were adopted.

## 10. Measurement and cost

The image-generation runtime was a Google Colab Tesla T4 with
14.56 GB reported VRAM. The first SSD-1B image took approximately
27 seconds and used a reported 3.32 GB peak allocated GPU memory.

SSD-1B is open-weight and its model card lists Apache 2.0. Local
inference did not incur a per-image hosted API fee, although Colab
GPU quota and runtime availability are constraints.

Gemini image generation was not used for the final images because
billing was required. The actual total generation latency, TTS latency,
assembly time and GPU minutes are recorded in `COSTS.md` when measured.

## 11. Consent, licences and AI disclosure

The father is portrayed by a fictional, non-identifiable generated
figure. The narration is synthetic and is not represented as his real
voice. The film includes a visible AI disclosure end card.

Family permission for public sharing, service terms and software
licences are recorded in `ETHICS.md`. Any identifiable real person
or replicated real voice must have documented informed consent.

## 12. Curiosity beyond the baseline

The project tested an open-weight image model after a paid image API
proved unsuitable. It also examined prompt-token limits and GPU
memory behaviour on a T4.

No paid frontier-model benchmark is claimed. Any additional language
test, model comparison or character-consistency experiment should be
added only if it was actually performed.

## 13. Lessons learned and next steps

The project demonstrated that a small production pipeline depends
not only on model generation, but also on validation, prompt design,
audio timing, reproducibility, storage management and honest evidence.

Next steps include stronger per-shot caching, a clean-clone
end-to-end command, automated model-call logging, better character
reference conditioning, and additional language support.

## 14. Links

- GitHub repository: [URL]
- Vertical film: [PUBLIC VIEW-ONLY URL]
- Horizontal film: [PUBLIC VIEW-ONLY URL]
- Walkthrough (maximum five minutes): [URL]
- Public post or screenshot: [URL]
