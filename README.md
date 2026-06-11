# Modern AI Systems: Development, Deployment, and Operations

Course materials for **Modern AI Systems** (AI 320, HIT) — an advanced 3rd-year CS course on
building and running AI-enabled systems in production, spanning **DevOps, DataOps, MLOps,
LLMOps, and AgentOps**.

**Live site:** https://apartsin.github.io/AISystemsCourse/

## Format

- 13 weeks, each **2 h lecture + 2 h practice** (4 contact hours); the practice session
  teaches its own hands-on material and ends with a weekly project-integration brief.
- One **running team project** integrates the covered material into an end-to-end system,
  graded at three **Student Project Presentations**: Specification (week 5), Interim
  (week 8), Final with oral defense (week 13).
- No written exams and no separate weekly labs; the project is the single deliverable.

## Layout

```
index.html              Course home / syllabus (English + Hebrew title)
assets/style.css        Shared house style (serif, navy accent)
lessons/weekNN.html     Per-week lesson plan: detailed lecture + practice timelines
prereq/index.html       Prerequisites review and self-check
references/index.html   Curated reading list, BoKs and tool indexes, mapped by week
build/gen.py            Generator for the weekly lesson-plan pages
```

## Building the lesson plans

The 13 lesson-plan pages under `lessons/` are generated from structured content in
`build/gen.py`:

```bash
python build/gen.py
```

Edit the `WEEKS` data in `build/gen.py` and re-run to regenerate. The page template and the
shared `assets/style.css` are the only things to touch for a style change.

## License

Course materials &copy; the instructor. Reuse for teaching with attribution.
