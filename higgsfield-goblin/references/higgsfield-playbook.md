# Higgsfield production playbook

Snapshot: 2026-08-08. Treat names, parameters, pricing, limits, and availability as volatile. Verify live before execution.

## Contents

- Production principles
- Asset-first workflow
- Tool and model routing
- Continuity system
- Efficient iteration
- Common production routes

## Production principles

1. Start from a deliverable, not a model.
2. Lock a hero frame, reference, or Element before asking motion to solve appearance and action simultaneously.
3. Separate camera direction from subject action and from editorial intent.
4. Build recurring characters, locations, products, props, styles, and voices once; name and reuse them.
5. Design clips as components of an edit. Include handles and transition intent.
6. Prototype at a lower-cost setting. The official guides repeatedly recommend validating motion/composition at 720p before a final 1080p pass when the selected model supports those settings.
7. Review beyond the first seconds. Identity and motion failures often emerge later in a clip.
8. Change one major input class at a time: prompt, reference, settings, or model.

## Asset-first workflow

Create assets in this order when relevant:

1. product/prop truth sheet
2. character or identity sheet
3. location sheet
4. wardrobe and production-design details
5. hero composition
6. start/end frames or motion reference
7. video

Use multi-view reference sheets for anything seen from more than one angle. Match reference aspect ratios to intended composition where possible. Keep brand labels, product geometry, and material behavior explicit in acceptance criteria.

### Cast versus Soul ID

- Use Cast for a persistent fictional screen character inside the cinematic workflow.
- Use Soul ID for a consenting real person's persistent identity across compatible Higgsfield generations.
- Use ordinary image references when persistence is limited to a shot or short sequence and training is unnecessary.

## Tool and model routing

Always inspect live schemas with MCP or `higgsfield model list`, `higgsfield model get`, `higgsfield workflow list`, and `higgsfield workflow get` where supported.

Use these as routing hypotheses, not promises:

- **Cinema Studio / Cinematic Studio** — controlled film shots, rig/lens intent, genre, characters, locations, start/end frames, multishot reasoning, and production-oriented composition.
- **Soul / Soul Cinema / Soul Cast / Soul Location** — photoreal key art and reusable people or places.
- **GPT Image / Nano Banana / Seedream / Flux family** — reference sheets, prop sheets, product truth frames, compositing, edits, graphic precision, and image exploration; pick from the live capabilities.
- **Seedance family** — multimodal video, reference-rich sequences, complex action, multiple shots, transitions, and native audio when available. State total duration, aspect ratio, and shot structure up front for structured sequences.
- **Kling family** — controlled image-to-video, character movement, dynamic single shots, and model-specific motion options.
- **Veo family** — cinematic video and native audio/dialogue routes when the current schema supports them.
- **Gemini Omni** — combined visual/audio generation, VFX, editing, or explainer blocks when present in the live catalog.
- **Marketing Studio / UGC tools** — URL/product-led ad creation, spokesperson formats, high-volume variations, and performance creative.
- **Popcorn** — connected storyboards, multi-frame campaigns, and reference-guided image sequences.
- **Canvas / Draw-to-Edit / Draw-to-Video** — spatial edits, product placement, localized changes, and visually directed transformations.
- **Audio / voice / dubbing workflows** — narration, voice replacement, localization, and lip-sync; confirm consent and current voice schema.
- **Virality Predictor** — analyze a finished cut for hook, attention, and retention. Treat the score as a diagnostic signal, not truth.
- **Reframe/upscale/background tools** — finishing utilities after the master creative is approved.

### Selection rubric

Rank candidate routes on:

- required input support
- identity/product/location continuity
- camera and motion controllability
- dialogue/native audio
- clip duration and resolution
- editability and transition needs
- speed and credit cost
- known failure mode for this shot

If two routes are close, test the riskiest shot once on each rather than switching models randomly throughout the project.

## Continuity system

Maintain a continuity ledger with:

- asset ID and approved version
- immutable traits
- shot-specific allowed changes
- reference file or generation ID
- camera-side and eyeline
- position, pose, wardrobe, hair, makeup, dirt/damage, props
- time, weather, light direction, color temperature
- dialogue, emotional state, and action endpoint
- previous and next shot handoff

For transitions, use the approved final frame of shot A and opening frame of shot B as anchors when supported. Preserve screen direction unless the cut intentionally crosses the axis.

## Efficient iteration

Use this diagnosis order:

1. Is the story/action physically possible in the duration?
2. Does the reference clearly show what must remain fixed?
3. Are subject action and camera action unambiguous?
4. Are there too many simultaneous events?
5. Does the selected model support the needed control?
6. Is a still edit or new hero frame cheaper than forcing the video prompt?

Prototype without optional audio and at lower resolution when that preserves the quality dimensions being tested. Add final audio and resolution after movement, performance, composition, and continuity pass.

## Common production routes

### Cinematic commercial

Brief → product truth sheet → world/location → hero casting → hook storyboard → hero frames → motion prototypes → proof/pack shot → edit → sound → claims review → aspect-ratio cutdowns.

### Narrative short

Logline → beat map → character/location bibles → coverage plan → scene hero frames → shot generations → continuity review → assembly → pickups → sound/color/titles.

### UGC/performance ad

Audience pain → truthful product promise → hook variants → consenting avatar/performer → script beats → product close-ups → native captions → CTA variants → performance review.

### Music or visualizer piece

Track map → visual motif → rhythm grid → hero assets → motion families → transitions → sync edit → lyric/rights check → format exports.

### Existing-footage transformation

Rights check → footage inventory → select timestamps → define preserve/change masks → test one representative shot → apply visual system → continuity/color/audio finishing.
