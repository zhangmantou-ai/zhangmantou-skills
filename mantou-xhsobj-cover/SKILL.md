---
name: mantou-xhsobj-cover
description: Create finished Xiaohongshu covers from real object photos, with the object as the visual anchor and clear title-led hierarchy. Use for products, small objects, food, crafts, desk scenes, and DIY projects; do not use when a person's expression or a software screenshot is the primary story.
---

# Mantou XHS Object Cover

Create a finished, publishable 3:4 Xiaohongshu cover from a real object photograph. The object—not generic AI imagery or a person—is the proof point. The design should make the topic understandable in a small feed thumbnail while preserving the actual object, its texture, silhouette, and relevant context.

## When to choose this skill

Use this when the post is about a physical object: a product, small object, food or drink, craft, flower, desk scene, DIY device, modified peripheral, or tool.

Choose the anchor before designing:

- **Object-first (default):** the item itself is the transformation, result, or sensory focus. Keep it in the lower 45–60% of the frame and visually isolate it with a white sticker outline when useful.
- **Person-first:** use only when the post is really about the creator's expression, pose, or lived experience. The object can support the story, but should not compete for primary attention.
- **Screenshot-first:** use when the software screen, result, or before/after state is what proves the claim. Use the object as a secondary cue.
- **Object + hand:** use when a hand makes scale, interaction, or use obvious. Do not add a person merely to fill the frame.

If the user's real photo is too soft, poorly lit, or hides the object, ask for another photo or use a deliberate crop; do not substitute an invented product rendering.

## Inputs to collect

Collect only what matters:

1. One real object photo to use as the edit target.
2. An optional style reference.
3. Either an exact main headline, or a clear request to generate one from the post theme and confirmed information.
4. Confirmed feature labels or proof points. Treat brand and product spelling as exact user content; ask if a term is ambiguous.

Do not add outcomes, data, compatibility, or functions that are not confirmed by the user or visible in the supplied material.

## Headline modes

Choose the mode from the user's instruction:

- **Provided title:** when the user supplies a main headline, preserve it verbatim. You may suggest a shorter cover version or a line break, but do not replace it without approval.
- **Candidate mode (default when no headline is supplied):** propose exactly three thumbnail-readable title options, based only on the photo, post theme, and confirmed information. Briefly label the angle of each option. Wait for the user to choose before making the finished cover.
- **Direct-selection mode:** choose one title yourself only when the user explicitly says that you may decide. State the chosen title and why it fits before producing the cover.

Never treat an image alone as proof of a product result, performance claim, or use case. If the photo does not make the topic clear enough to write truthful title candidates, ask for one sentence of context.

## Default composition

- Canvas: 1080 × 1440 px, 3:4 vertical.
- Preserve authentic photo texture; crop for composition rather than replacing the scene.
- Put one dominant object anchor in the lower-middle area. Keep its identifiable silhouette, texture, colour, and relevant details intact; for devices, screens, ports, and cables may also matter.
- Reserve the upper 30–35% for the main title. Make it readable at roughly 80 px wide.
- Use one small category tag, one short support label, and at most a few sparse doodles. Extra labels should guide the eye, not become a paragraph.
- Use a thick irregular white outline around the object only when it improves separation from the background.

## Recommended visual language

For reference styles like a playful Xiaohongshu collage: use a real photo base, highlighter-yellow hand-painted title, deep charcoal outline/shadow, a white sticker border, one cobalt-blue tag, mint/cyan accent icons, and a few hand-drawn arrows or sparkles.

Suggested palette:

- headline yellow: `#F3F000`
- outline charcoal: `#161616`
- sticker white: `#FFFFFF`
- tag blue: `#356AFF`
- tech mint: `#79E7D7`

Treat these as a starting point, not a mandatory identity. Match the source image when another palette is more legible.

## Copy hierarchy

1. **Main title:** the only oversized text. Prefer 8–16 Chinese characters; a two-line lockup is fine.
2. **Category tag:** 2–8 words, such as `M5Stack 改造`, `周末咖啡`, or `手作记录`.
3. **Support label:** 2–4 short confirmed attributes separated by dots, such as `语音交互 · Hermes` or `黄油香 · 现烤`.
4. **Optional handwritten note:** one small human observation, not another sales claim.

Avoid fake logos, QR codes, creator watermarks, random decorative English, dense copy, and generic claims such as “最强”“无敌”“秒懂” unless the user explicitly wants and can support them.

## Production workflow

1. Use the supplied photo as an **edit target** and any example collage as a **style reference**. Create a complete finished cover, not a text-free background, unless the user asks otherwise.
2. State the chosen anchor and the planned copy before generation. In candidate mode, the title choice must be confirmed first; in direct-selection mode, state the title you selected.
3. Generate or edit the cover with exact text supplied in the prompt. Preserve the object photo's identity and scene.
4. Inspect the output at full size. Verify: object identity, title spelling, label spelling, no invented functions, no occlusion of the main object, and correct 3:4 dimensions.
5. If text is malformed or too small, make one targeted revision or use a deterministic text-overlay step. Never silently deliver a misspelled headline.
6. Save a non-destructive PNG with a descriptive name. Report its absolute path and exact dimensions.

For detailed measurements and the release checklist, read [layout-and-qa.md](layout-and-qa.md).
