# Production Engineering for AI Systems

Course materials for **Production Engineering for AI Systems** (AI 320, HIT) — an advanced
3rd-year CS course on the engineering, deployment, monitoring, governance, and operation of
modern AI-enabled systems, spanning **DevOps, DataOps, MLOps, LLMOps, AgentOps, and AIOps**.

**Live site:** https://apartsin.github.io/AIOpsCourse/

## Format

- 13 weeks, each a **2-hour lecture + 2-hour practice** session.
- A single **running project** carried from specification to production, presented to the
  class three times: **Specification (week 5), Interim (week 8), Final (week 13)**.
- Project- and lab-based; no written exams.

## Layout

```
index.html              Course home / syllabus
assets/style.css        Shared house style (serif, navy accent)
lessons/weekNN.html     Per-week lesson plan: 2 h lecture + 2 h practice timelines
references/index.html   Curated reading list, grouped by layer and mapped by week
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
