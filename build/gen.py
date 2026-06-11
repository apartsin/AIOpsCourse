# -*- coding: utf-8 -*-
"""Generate weekly lesson-plan pages for Production Engineering for AI Systems.
Each week -> lessons/weekNN.html with a 2 h lecture timeline and a 2 h practice
timeline, matching the DLCourseHIT house style (assets/style.css)."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "lessons")
os.makedirs(OUT, exist_ok=True)

BRAND = "Production Engineering for AI Systems"
FOOT = "Production Engineering for AI Systems &middot; HIT &middot; Advanced Course &middot; course materials"

def esc(s): return html.escape(s, quote=False)

# Each timeline row: (clock, minutes, head, detail)  detail = str | list[str] | None
WEEKS = [
{
 "n":1,"part":"Part I &middot; DevOps Foundations",
 "title":"Production Engineering & the Ops Landscape",
 "obj":["Explain why production systems fail in operations more than in modelling.",
        "Map the six operational layers (DevOps through AIOps) and how they stack.",
        "Set up the course toolchain (Git, Docker) and the team project repository."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Course mechanics, the running project, and this week's objectives."),
        ("0:10-0:30",20,"Motivation","The prototype-to-production gap: an accurate model is a small part of a working system. Outages, latency, and stale data cost more than a point of accuracy."),
        ("0:30-1:10",40,"The reliability stack & the SRE mindset",
            ["Service-level indicators, objectives, and error budgets: reliability as a measurable contract.",
             "Toil, on-call, and the development-versus-operations tension SRE was created to resolve.",
             "What 'production-ready' means: availability, latency, cost, recoverability, and observability.",
             "Board work: turning a vague 'it should be reliable' into an SLO with a number."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"The six operational layers",
            ["DevOps, DataOps, MLOps, LLMOps, AgentOps, AIOps: what each one owns.",
             "How the layers compose; each later layer inherits the guarantees of the earlier ones.",
             "Where the running project will touch every layer over the semester."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Revisit the checks below and preview the toolchain setup.")],
 "miss":("If the model is accurate, the system is done.",
         "Accuracy is one property. Availability, latency, cost, data freshness, and recoverability are separate properties that usually dominate production outcomes."),
 "checks":[("Give one failure a 99%-accurate model can still cause in production.",
            "It can serve at 5 s latency, crash under load, or be fed stale/garbage inputs. Accuracy says nothing about any of these."),
           ("What does an error budget let a team do?",
            "Spend a quantified amount of unreliability on shipping features, and freeze risky changes once it is exhausted. It makes reliability a negotiable, measurable resource.")],
 "take":["Production failures are mostly operational, not algorithmic.",
         "SLOs and error budgets turn 'reliability' into a measurable contract.",
         "The six layers compose; each later layer inherits the earlier ones."],
 "prac":[("0:00-0:10",10,"Setup & recap","Confirm Git, Docker, and editor are installed; recap the lecture."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["A clean Git workflow: branches, pull requests, and branch protection.",
             "A sensible repository layout for a service; .gitignore and secrets hygiene.",
             "Form project teams and create the shared repository."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Containerise a minimal 'hello-service' with a Dockerfile.",
             "Build the image, run the container, and read its logs.",
             "Pin versions so the image is reproducible off your laptop."]),
         ("1:50-2:00",10,"Wrap-up & project kickoff","Brief the project: teams pick a domain before week 5.")],
 "pit":["Never commit secrets or large data to Git; use .gitignore and environment variables from day one.",
        "A container that runs only on your laptop usually pins no versions. Pin them."],
},
{
 "n":2,"part":"Part I &middot; DevOps Foundations",
 "title":"Continuous Integration & Delivery",
 "obj":["Build a CI pipeline that lints, tests, builds, and produces an artifact.",
        "Explain the testing pyramid and where each kind of test belongs.",
        "Describe infrastructure as code and why environments must be reproducible."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Last week's reliability stack; today's objectives."),
        ("0:10-0:30",20,"Motivation","Manual deploys break in ways no one can reproduce. Fast, repeatable, automated feedback is what makes change safe."),
        ("0:30-1:10",40,"CI/CD concepts",
            ["Pipelines, stages, and artifacts; what 'continuous integration' actually means.",
             "The testing pyramid: many fast unit tests, fewer integration tests, very few end-to-end.",
             "Trunk-based versus long-lived feature branches and their effect on integration pain.",
             "Continuous delivery versus continuous deployment."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Infrastructure as code",
            ["Declarative versus imperative provisioning; the Terraform model.",
             "Idempotency: why applying the same config twice must converge to one state.",
             "Environment parity: dev, staging, and prod from the same definitions."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building a pipeline in GitHub Actions.")],
 "miss":("CI is just running the tests.",
         "CI is the discipline of integrating small changes into a shared mainline continuously, with automated verification. The test run is one stage of that, not the whole idea."),
 "checks":[("Why are end-to-end tests the thin top of the pyramid, not the base?",
            "They are slow, flaky, and expensive. Most coverage should come from fast unit tests, with fewer integration tests and very few end-to-end."),
           ("What property makes infrastructure-as-code safe to re-apply?",
            "Idempotency: applying the same configuration repeatedly converges to the same target state instead of stacking changes.")],
 "take":["CI integrates small changes continuously; the test run is one stage.",
         "Push coverage down the pyramid: fast unit tests are the base.",
         "Idempotent, declarative infrastructure gives reproducible environments."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open last week's repository and the Actions tab."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Write a GitHub Actions workflow: lint, test, build, upload artifact.",
             "Cache dependencies and use a matrix to test multiple versions.",
             "Make a failing test block the merge via a required check."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Add a Docker image build to the pipeline and push it to a registry.",
             "Introduce a tiny Terraform definition and apply it twice to show idempotency."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Summarise the pipeline stages and brief the lab.")],
 "pit":["Flaky tests erode trust in CI; quarantine and fix them rather than re-running.",
        "A 40-minute pipeline kills the feedback loop; parallelise and cache."],
},
{
 "n":3,"part":"Part I &middot; DevOps Foundations",
 "title":"Containers, Orchestration & Observability",
 "obj":["Containerise a service properly and run it under an orchestrator.",
        "Explain the core Kubernetes primitives and two rollout strategies.",
        "Instrument the three pillars of observability and read them."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From one container to a fleet; today's objectives."),
        ("0:10-0:30",20,"Motivation","Running one container is easy; running hundreds with health, scaling, and rollout is why orchestration exists."),
        ("0:30-1:10",40,"Kubernetes primitives & rollouts",
            ["Pods, deployments, services, and how desired state is reconciled.",
             "Health checks, autoscaling, and resource requests/limits.",
             "Blue-green versus canary deployments and when each fits.",
             "Board work: tracing a request from service to pod."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Observability: logs, metrics, traces",
            ["The three pillars and what each answers; monitoring versus observability.",
             "The RED and USE methods for choosing what to measure.",
             "High-cardinality, structured telemetry as the enabler of new questions."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview deploying to a local cluster.")],
 "miss":("Observability just means more dashboards.",
         "Observability is the ability to ask new questions of a running system without shipping new code. Well-structured, high-cardinality telemetry, not the number of dashboards, is what enables it."),
 "checks":[("What is the difference between blue-green and canary deployment?",
            "Blue-green swaps all traffic between two full environments at once; canary shifts a small percentage gradually and watches metrics before ramping up."),
           ("When do traces help where aggregate metrics do not?",
            "Traces follow a single request across services and show where its latency is spent, which an aggregate metric cannot localise.")],
 "take":["Orchestration reconciles desired state across a fleet.",
         "Canary shifts traffic gradually and watches metrics; blue-green flips all at once.",
         "Tail latency (p95/p99) and traces reveal what averages hide."],
 "prac":[("0:00-0:10",10,"Setup & recap","Start a local cluster (kind or minikube)."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Deploy the week-1 service: a Deployment plus a Service.",
             "Scale it, kill a pod, and watch the orchestrator self-heal.",
             "Perform a canary rollout and shift traffic gradually."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Wire Prometheus to scrape metrics and Grafana to display them.",
             "Build a RED dashboard (rate, errors, duration) and read p95/p99 latency."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the rollout and observability setup.")],
 "pit":["p50 latency hides the tail; always watch p95/p99.",
        "Unstructured logs are hard to query; emit structured (JSON) logs."],
},
{
 "n":4,"part":"Part II &middot; DataOps",
 "title":"Data Pipelines & Versioning",
 "obj":["Build an orchestrated data pipeline with retries and backfills.",
        "Reason about batch versus streaming and idempotency.",
        "Version a dataset and reproduce a result from a pinned snapshot."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Data as the largest source of production ML bugs; objectives."),
        ("0:10-0:30",20,"Motivation","Garbage in, garbage out: most ML incidents trace to data, not the model. Pipelines must be reproducible and observable like any other service."),
        ("0:30-1:10",40,"Pipeline orchestration",
            ["DAGs, scheduling, and dependencies in Airflow or Dagster.",
             "Idempotency, retries, and backfills; why re-execution must be safe.",
             "Batch versus streaming, and where each belongs.",
             "Parameterising the run date instead of hardcoding 'today'."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Data versioning & lineage",
            ["Immutable snapshots with DVC or lakeFS; pointers instead of blobs in Git.",
             "Reproducing a result by pinning the exact dataset version.",
             "Lineage graphs: tracing a number back to the data that produced it."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building a DAG and versioning a dataset.")],
 "miss":("Re-running a pipeline always gives the same result.",
         "Only if every stage is idempotent and inputs are versioned. Late-arriving data, mutable sources, and non-deterministic steps make repeated runs diverge."),
 "checks":[("Why must an orchestrated task be idempotent?",
            "Retries and backfills re-execute tasks. A non-idempotent task double-writes or corrupts state when it runs twice."),
           ("What does data versioning buy you that code versioning does not?",
            "The ability to reproduce a model or result exactly by pinning the dataset snapshot, not just the code that processed it.")],
 "take":["Most ML production bugs are data bugs.",
         "Idempotency makes retries and backfills safe.",
         "Pinning a data version is what makes a result reproducible."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the orchestrator and a small sample dataset."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Author an extract-transform-load DAG with explicit dependencies.",
             "Trigger a retry and a backfill; show idempotent re-execution.",
             "Add a data-freshness check to the pipeline."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Version a dataset with DVC and commit the pointer, not the data.",
             "Roll back to an earlier snapshot and reproduce a prior output."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the DAG and versioning workflow.")],
 "pit":["Hardcoding 'today' breaks backfills; parameterise the run date.",
        "Committing raw data to Git bloats the repo; use DVC pointers."],
},
{
 "n":5,"part":"Part II &middot; DataOps",
 "title":"Data Quality, Contracts & Feature Stores",
 "obj":["Enforce data quality continuously with validation rules.",
        "Define a data contract between a producer and a consumer.",
        "Explain feature stores and the cause of train/serve skew."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Versioned pipelines; today's objectives."),
        ("0:10-0:30",20,"Motivation","Upstream schema changes and silent quality drops break models without any error. Quality must be guarded at the boundary, continuously."),
        ("0:30-1:05",35,"Data quality & contracts",
            ["Validation with Great Expectations: schema, ranges, nullity, uniqueness.",
             "Data contracts: the schema, semantics, freshness, and quality a producer guarantees.",
             "Quality SLAs and where to fail a pipeline loudly versus quarantine bad rows."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:40",25,"Feature stores & train/serve skew",
            ["Offline versus online features; point-in-time correctness.",
             "Train/serve skew: when serving features differ from training features.",
             "What a feature store centralises and why."]),
        ("1:40-2:00",20,"Wrap-up & Presentation-1 logistics","Recap and brief the specification presentation rubric.")],
 "miss":("Data validation is a one-time cleaning step.",
         "Quality is a continuous contract checked on every run. Upstream producers keep changing, so validation must guard the boundary forever, not once."),
 "checks":[("What is train/serve skew and one cause?",
            "The features seen at serving differ from those at training, e.g. a transformation applied only in the training notebook, or time leakage in offline features."),
           ("What does a data contract specify?",
            "The schema, semantics, freshness, and quality guarantees a producer promises a consumer, enforced automatically at the boundary.")],
 "take":["Data quality is a continuous contract, not a one-off clean.",
         "Contracts make producer-consumer guarantees explicit and enforced.",
         "Train/serve skew is a top cause of silent model failure."],
 "prac":[("0:00-0:10",10,"Setup & rubric","Presentation logistics and the specification rubric."),
         ("0:10-1:00",50,"Project Presentation 1 - Specification (round 1)",
            ["Teams present: problem, success metrics (SLOs), system and data architecture.",
             "DevOps and DataOps plan: repository, CI skeleton, data sources.",
             "Peer and instructor questions after each talk."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Project Presentation 1 - Specification (round 2)",
            ["Remaining teams present and field questions.",
             "Risk and governance register reviewed for each team."]),
         ("1:50-2:00",10,"Feedback synthesis","Common gaps and next steps toward the interim milestone.")],
 "pit":["A specification without measurable SLOs is not a specification; name the numbers.",
        "Validate at the boundary you do not control, not only your own outputs."],
 "pres":"Presentation 1 &middot; Specification",
 "present":["Problem statement and success metrics (SLOs).",
            "System and data architecture.",
            "DevOps and DataOps plan: repository, CI skeleton, and data sources.",
            "Risk and governance register."],
},
{
 "n":6,"part":"Part III &middot; MLOps",
 "title":"Experiment Tracking & the Model Registry",
 "obj":["Track experiments so any result is reproducible.",
        "Use a model registry with governed stage transitions.",
        "Write a model card that documents a model honestly."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From data to models; objectives."),
        ("0:10-0:30",20,"Motivation","'Which run produced this model?' is a question most teams cannot answer. Tracking ties a number to the exact code, data, and environment that made it."),
        ("0:30-1:10",40,"Experiment tracking",
            ["Logging parameters, metrics, and artifacts with MLflow or Weights & Biases.",
             "Pinning the git SHA, the data version, and the environment to each run.",
             "Comparing runs and reading curves, not just final numbers.",
             "Run lineage: from raw data to the trained artifact."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Model registry & governance",
            ["Registry stages: staging, production, archived; versioned models.",
             "Governed promotion with approvals, and rollback to a prior version.",
             "Model cards: intended use, data, metrics, and limitations."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview instrumenting training with MLflow.")],
 "miss":("Logging metrics to a spreadsheet is enough.",
         "Without linking each metric to the exact code, data version, and environment, the number is not reproducible. Tracking is what ties them together."),
 "checks":[("What three things must a tracked run pin to be reproducible?",
            "The code version (git SHA), the data version, and the environment plus hyperparameters."),
           ("Why use a registry stage transition rather than just copying a file?",
            "It gives an auditable, governed promotion path with approvals and a clear rollback target, instead of an untracked file copy.")],
 "take":["A metric is reproducible only when tied to code, data, and environment.",
         "A registry gives governed, auditable model promotion and rollback.",
         "Model cards document intended use and limitations, not just accuracy."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open a training script and the tracking UI."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Instrument training with MLflow: log params, metrics, and artifacts.",
             "Pin the git SHA and the dataset snapshot id to the run.",
             "Compare two runs and read the training curves."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Register the best model and move it staging then production.",
             "Generate a model card from the run metadata."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap tracking and registry workflow.")],
 "pit":["Logging only the final metric loses the story; log the full curve.",
        "An unpinned data version makes the run impossible to reproduce."],
},
{
 "n":7,"part":"Part III &middot; MLOps",
 "title":"CI/CD for ML & Model Serving",
 "obj":["Package a model and serve it behind an API.",
        "Choose between online, batch, and streaming serving.",
        "Roll out a new model safely with shadow, canary, or A/B."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Tracked, registered models; objectives."),
        ("0:10-0:30",20,"Motivation","Training is a small fraction of the work. Serving, scaling, and continuously retraining the model is where production ML actually lives."),
        ("0:30-1:10",40,"Serving patterns",
            ["Online, batch, and streaming serving; REST versus gRPC.",
             "Request batching, autoscaling, and the latency budget.",
             "Continuous training: when and how to retrain automatically.",
             "Packaging a model with pinned dependencies."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Safe rollout for models",
            ["Shadow deployment: real traffic, responses not used.",
             "Canary and A/B for models; measuring the online metric.",
             "The offline-online gap: why a good offline score can disappoint live."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview wrapping a model in a serving runtime.")],
 "miss":("A good offline metric guarantees a good online result.",
         "Offline metrics use historical data and proxy objectives. Feedback loops, latency, and distribution shift mean online behaviour can differ, so validate with shadow, canary, or A/B."),
 "checks":[("What is a shadow deployment?",
            "Sending real traffic to the new model in parallel without using its responses, to compare it against production safely."),
           ("When would you choose batch serving over online?",
            "When predictions can be precomputed and freshness tolerances allow it; batch is cheaper and operationally simpler.")],
 "take":["Serving and retraining dominate the ML lifecycle, not training.",
         "Shadow and canary validate a model on live traffic before it decides anything.",
         "Offline metrics are a proxy; confirm online."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the registered model from week 6."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Wrap the model in a serving runtime (BentoML or FastAPI) and containerise it.",
             "Deploy it and call the endpoint; measure latency.",
             "Add request batching and warm the model to cut cold-start latency."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Configure a canary between the old and new model versions.",
             "Load-test and compare p95 latency and error rate."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap serving and rollout.")],
 "pit":["Cold starts and model load blow the latency budget; warm the model.",
        "Serving a pickled model without pinned library versions breaks silently."],
},
{
 "n":8,"part":"Part III &middot; MLOps",
 "title":"Monitoring, Drift & Model Governance",
 "obj":["Monitor a deployed model and its inputs.",
        "Distinguish data drift from concept drift and detect each.",
        "Define retraining triggers and an audit trail."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Served models; the day-two problem; objectives."),
        ("0:10-0:30",20,"Motivation","Models decay silently as the world shifts. Labels often arrive late, so live accuracy is unknown and inputs become the early-warning signal."),
        ("0:30-1:05",35,"Monitoring & drift",
            ["Data drift versus concept drift: which distribution changed.",
             "Detectors: population stability index, KS test, embedding distance.",
             "Prediction-distribution and proxy monitoring when labels are delayed."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:40",25,"Retraining & governance",
            ["Retraining triggers: schedule, drift threshold, or performance proxy.",
             "Human-in-the-loop approval and audit trails for model changes.",
             "Pairing every detector with a documented action."]),
        ("1:40-2:00",20,"Wrap-up & Presentation-2 logistics","Recap and brief the interim presentation rubric.")],
 "miss":("If accuracy looks fine, there is no drift.",
         "Labels are often delayed, so live accuracy is usually unknown. Input drift can be detected before any accuracy drop and is the real early-warning signal."),
 "checks":[("What is the difference between data drift and concept drift?",
            "Data drift is a change in the input distribution; concept drift is a change in the input-to-output relationship itself."),
           ("What do you monitor when ground-truth labels arrive weeks late?",
            "Input and feature distributions and the prediction distribution as proxies, alongside business KPIs.")],
 "take":["Models decay; monitoring is a day-two necessity, not optional.",
         "Input drift is detectable before accuracy drops.",
         "A detector without an attached action is just noise."],
 "prac":[("0:00-0:10",10,"Setup & rubric","Presentation logistics and the interim rubric."),
         ("0:10-1:00",50,"Project Presentation 2 - Interim (round 1)",
            ["Teams demo: working data and training pipeline, tracking, and registry.",
             "First deployed endpoint with CI/CD shown live.",
             "Questions on the monitoring and drift plan."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Project Presentation 2 - Interim (round 2)",
            ["Remaining teams demo and field questions.",
             "Operational-readiness gaps flagged for the final."]),
         ("1:50-2:00",10,"Feedback synthesis","Common gaps and the path to the final demo.")],
 "pit":["A drift alarm with no playbook is noise; attach an action to every detector.",
        "Watching only accuracy misses drift while labels are delayed."],
 "pres":"Presentation 2 &middot; Interim",
 "present":["Working data and training pipeline.",
            "Experiment tracking and a model registry.",
            "A first deployed endpoint, with CI/CD demonstrated live.",
            "Monitoring and drift plan."],
},
{
 "n":9,"part":"Part IV &middot; LLMOps & AgentOps",
 "title":"Serving LLMs, Prompts & RAG",
 "obj":["Serve an LLM and reason about its cost and latency.",
        "Manage prompts and context as versioned program logic.",
        "Build a retrieval-augmented generation pipeline."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From classical ML to LLMs; objectives."),
        ("0:10-0:30",20,"Motivation","LLMs change the cost, latency, and quality trade-offs and introduce new failure modes: hallucination, prompt drift, and context limits."),
        ("0:30-1:05",35,"LLM serving & inference",
            ["Tokens, context windows, and why length drives cost and latency.",
             "Batching, the KV cache, and throughput-oriented serving with vLLM.",
             "Hosted APIs versus self-hosted models: the operational trade-offs."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:50",35,"Retrieval-augmented generation",
            ["Embeddings, vector databases, chunking, and retrieval.",
             "Assembling a grounded prompt with retrieved context and citations.",
             "Versioning prompts like code: review, rollback, and evaluation."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building a RAG service.")],
 "miss":("RAG means the model can no longer hallucinate.",
         "Retrieval grounds the answer, but the model can still ignore or misread the context. Faithfulness depends on retrieval quality, chunking, and citations, and must be measured rather than assumed."),
 "checks":[("Why version prompts like code?",
            "Prompts are program logic: a prompt change alters behaviour, so it must be tracked, reviewed, and rollback-able like any other code."),
           ("Give one reason RAG retrieval fails.",
            "Poor chunking or an embedding mismatch means the relevant passage is never retrieved, a recall failure the generator cannot recover from.")],
 "take":["Context length is the main driver of LLM cost and latency.",
         "Prompts are versioned program logic, not free text.",
         "RAG faithfulness depends on retrieval quality and must be measured."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open a document corpus and an embedding model."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Embed and index documents in a vector database (FAISS or Qdrant).",
             "Retrieve relevant chunks and assemble a grounded prompt.",
             "Generate an answer with citations and inspect the retrieved context."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Serve generation via vLLM or a hosted API and measure latency.",
             "Store prompts as versioned files and swap a prompt version."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the RAG pipeline.")],
 "pit":["A huge context window is expensive and slow; retrieve few, relevant chunks.",
        "Embedding and querying with different models silently destroys retrieval."],
},
{
 "n":10,"part":"Part IV &middot; LLMOps & AgentOps",
 "title":"LLM Evaluation, Guardrails & Cost",
 "obj":["Evaluate generation quality with a real eval set.",
        "Apply guardrails against unsafe and injected behaviour.",
        "Control token cost and latency at scale."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Serving and RAG; objectives."),
        ("0:10-0:30",20,"Motivation","'Looks good' is not evaluation. At scale, safety, faithfulness, and cost have to be measured and bounded, not eyeballed."),
        ("0:30-1:05",35,"LLM evaluation",
            ["Building an offline evaluation set that represents real usage.",
             "LLM-as-judge and its biases: position, verbosity, self-preference.",
             "Faithfulness and groundedness metrics; regression evaluation on prompt changes."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:50",35,"Guardrails & cost",
            ["Input and output filtering; PII handling; prompt-injection defenses.",
             "Caching repeated calls and routing easy queries to a cheaper model tier.",
             "Batching and shorter context as cost levers."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building an eval harness.")],
 "miss":("LLM-as-judge is objective.",
         "A judge model carries position, verbosity, and self-preference biases. It must be calibrated against human labels and used with controls, not trusted blindly."),
 "checks":[("What is prompt injection and one defense?",
            "Untrusted input that overrides the system instructions. Defenses include input/output filtering, privilege separation, and not acting on tool instructions embedded in untrusted content."),
           ("Name two levers to cut LLM cost.",
            "Cache repeated calls and route easy queries to a cheaper model tier; shortening context is a third.")],
 "take":["A representative eval set is the foundation; a 10-item set is noise.",
         "LLM-as-judge is biased and must be calibrated against humans.",
         "Caching and tier routing are the first cost levers to reach for."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the RAG service and a small labelled set."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Build an eval harness (Ragas or custom) over an offline set.",
             "Score faithfulness and answer relevance; run a regression on a prompt change.",
             "Add an LLM-as-judge and sanity-check it against human labels."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Add input/output guardrails and test prompt-injection cases.",
             "Add a response cache and measure the cost and latency drop."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap evaluation, guardrails, and cost.")],
 "pit":["A 10-item eval set measures noise; build a representative one.",
        "Never put secrets in prompts or logs; treat them as untrusted output."],
},
{
 "n":11,"part":"Part IV &middot; LLMOps & AgentOps",
 "title":"AgentOps - Operating Autonomous Agents",
 "obj":["Reason about agent architectures and their failure surface.",
        "Trace agents at the step level and evaluate them.",
        "Bound agents with step, cost, and permission limits."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From single calls to agent loops; objectives."),
        ("0:10-0:30",20,"Motivation","Agents add autonomy, tools, and memory, and with them a large new failure surface: runaway loops, wrong tool calls, and unbounded cost."),
        ("0:30-1:10",40,"Agent architectures",
            ["Tool use and function calling; the plan-act-observe loop.",
             "Memory: short-term context versus long-term stores.",
             "Multi-agent orchestration and when it helps versus hurts.",
             "Where agents fail: tool errors, hallucinated arguments, loops."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"AgentOps",
            ["Tracing agents as spans: every step, tool call, and decision.",
             "Step-level evaluation, not just final-output evaluation.",
             "Bounds: max steps, wall-clock and cost budgets, least-privilege tools."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview instrumenting an agent.")],
 "miss":("An agent loop will stop on its own.",
         "Without explicit step, cost, and wall-clock bounds and a termination criterion, agents loop, retry, and burn budget. Bounds and an error classifier are mandatory: a retry-on-any-exception loop spins forever on a caller-side bug."),
 "checks":[("Why trace at the step level, not just the final output?",
            "Failures hide in intermediate tool calls and decisions; step traces localise exactly where the agent went wrong."),
           ("Name two bounds every agent loop needs.",
            "A maximum step/iteration cap and a wall-clock or cost budget, with an error classifier so caller-side bugs fail fast instead of retrying.")],
 "take":["Agents add autonomy and a large new failure surface.",
         "Trace and evaluate at the step level, not just the output.",
         "Every agent loop needs step, cost, and permission bounds."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open a simple tool-using agent scaffold."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Give the agent two tools and run the plan-act-observe loop.",
             "Add tracing (OpenTelemetry or LangSmith) and read the step spans.",
             "Trigger a failure and locate it in the trace."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Add a max-step cap, a cost budget, and an error classifier.",
             "Write a small step-level evaluation for the agent."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap tracing and bounding agents.")],
 "pit":["Broad tool permissions are dangerous; grant least privilege.",
        "A retry-on-any-exception loop spins on caller bugs; classify the error first."],
},
{
 "n":12,"part":"Part V &middot; AIOps, Security & Governance",
 "title":"AIOps - AI for IT Operations",
 "obj":["Apply anomaly detection to service telemetry.",
        "Reduce alert noise through correlation and deduplication.",
        "Automate a safe remediation with guardrails."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Operating AI, now AI for operations; objectives."),
        ("0:10-0:30",20,"Motivation","No human can watch millions of metrics. Alert fatigue means real incidents get missed in the noise; AIOps aims for fewer, sharper, actionable signals."),
        ("0:30-1:10",40,"AIOps techniques",
            ["Anomaly detection on metrics and logs; handling seasonality.",
             "Alert correlation and deduplication to cut volume.",
             "Root-cause hints: grouping symptoms to a likely cause.",
             "Precision over volume: an alert must be actionable."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Incident automation",
            ["Runbooks and auto-remediation for known failure modes.",
             "Self-healing and closed-loop control, and the risks of both.",
             "Rate limits, circuit breakers, and human-in-the-loop for risky actions."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview anomaly detection on telemetry.")],
 "miss":("More alerts means a safer system.",
         "Alert overload causes fatigue and missed real incidents. The goal is fewer, correlated, actionable alerts: precision over volume."),
 "checks":[("Why is seasonality important for anomaly detection?",
            "Normal traffic has daily and weekly cycles; a detector that ignores seasonality flags every Monday-morning spike as an anomaly."),
           ("Name one risk of automated remediation.",
            "A wrong auto-action, or a feedback loop, can amplify an incident. Guardrails, rate limits, and human-in-the-loop for risky actions are required.")],
 "take":["AIOps trades alert volume for alert precision.",
         "Seasonality must be modelled or every cycle looks anomalous.",
         "Automated remediation needs circuit breakers and rate limits."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open a telemetry stream from the project service."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Run anomaly detection on a seasonal metric and tune sensitivity.",
             "Correlate and deduplicate a burst of alerts into one incident.",
             "Map an anomaly to impact so it becomes actionable."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Write one auto-remediation rule with a rate limit and circuit breaker.",
             "Trigger it safely and confirm it backs off."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap AIOps and safe automation.")],
 "pit":["A self-healing action without a circuit breaker can flap; bound it.",
        "An anomaly is not an incident; tie every alert to impact."],
},
{
 "n":13,"part":"Part V &middot; AIOps, Security & Governance",
 "title":"Security, Governance & Synthesis",
 "obj":["Secure the software, data, and model supply chain.",
        "Apply privacy, compliance, and responsible-AI practice.",
        "Synthesise the six layers into one operational stack."],
 "lec":[("0:00-0:10",10,"Recap & objectives","The whole stack; objectives."),
        ("0:10-0:30",20,"Motivation","AI systems widen both the attack surface and the governance surface: new data, new models, new autonomy, all of which can be abused or audited."),
        ("0:30-1:05",35,"Security & supply chain",
            ["Secrets management, least privilege, and dependency/SBOM hygiene.",
             "The model and data supply chain: poisoned datasets and backdoored weights.",
             "The OWASP Top 10 for LLM applications as a checklist."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:40",25,"Governance & responsible AI",
            ["Privacy, PII handling, and compliance obligations.",
             "Model documentation and audit trails across the stack.",
             "Synthesis: how DevOps through AIOps compose into one system."]),
        ("1:40-2:00",20,"Wrap-up & course synthesis","Recap the course and brief the final presentation.")],
 "miss":("Security and governance are a final checklist.",
         "They are cross-cutting properties designed in from week one: secrets, least privilege, data contracts, and audit trails. Bolting them on at the end does not work."),
 "checks":[("Name one supply-chain risk unique to ML and LLM systems.",
            "A poisoned or backdoored pretrained model or dataset pulled from a public hub; verify provenance and pin versions."),
           ("Why keep audit trails across the whole stack?",
            "For compliance, incident forensics, and reproducibility: to answer which data, model, and prompt produced a decision, and who approved it.")],
 "take":["Security and governance are designed in from week one, not appended.",
         "The model and data supply chain is a real attack surface.",
         "The six layers compose into one auditable operational stack."],
 "prac":[("0:00-0:10",10,"Setup & rubric","Final presentation logistics and oral-defense format."),
         ("0:10-1:00",50,"Project Presentation 3 - Final (round 1)",
            ["Teams give the end-to-end production demo.",
             "Observability, AIOps, evaluation, guardrails, and cost report.",
             "Short oral defense: any team member answers on any part."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Project Presentation 3 - Final (round 2)",
            ["Remaining teams demo and defend.",
             "Security and governance review for each system."]),
         ("1:50-2:00",10,"Course wrap-up","Retrospective and where each layer goes next.")],
 "pit":["Secrets in client-side code or logs leak; keep them server-side and rotated.",
        "A model card nobody maintains is theatre; keep documentation live."],
 "pres":"Presentation 3 &middot; Final",
 "present":["End-to-end production demo.",
            "Observability and an AIOps capability in place.",
            "Evaluation, guardrails, and a cost/latency report.",
            "Security and governance review, plus a retrospective.",
            "Short oral defense: any team member answers on any part."],
},
]

def render_timeline(rows):
    out = ['<table class="timeline">']
    for clock, mins, head, detail in rows:
        m = f'{mins} min' if mins else ''
        cell = f'<b>{esc(head)}</b>'
        if isinstance(detail, list):
            cell += '<ul class="dt-list">' + ''.join(f'<li>{esc(x)}</li>' for x in detail) + '</ul>'
        elif detail:
            cell += f'<span class="dt">{esc(detail)}</span>'
        out.append(f'<tr><td class="tm">{clock}</td><td class="mn">{m}</td><td>{cell}</td></tr>')
    out.append('</table>')
    return ''.join(out)

def page(w, prev, nxt):
    nn = f'{w["n"]:02d}'
    title = esc(w["title"])
    obj = ''.join(f'<li>{esc(x)}</li>' for x in w["obj"])
    checks = ''.join(
        f'<details><summary>{esc(q)}</summary><div class="ans">{esc(a)}</div></details>'
        for q, a in w["checks"])
    take = ''.join(f'<li>{esc(x)}</li>' for x in w["take"])
    pit = ''.join(f'<li>{esc(x)}</li>' for x in w["pit"])
    pres_badge = f' &middot; {w["pres"]}' if w.get("pres") else ''

    if w.get("pres"):
        present = ''.join(f'<li>{esc(x)}</li>' for x in w["present"])
        practice_html = (
            '<h2 id="practice"><span class="ic">&#128483;&#65039;</span>'
            '<span class="secttag prac">Practice &middot; 2 hours &middot; student presentations</span></h2>'
            f'<p>The full two-hour practice slot is given over to <b>student project presentations ({w["pres"]})</b>. '
            'There is no instructor-prepared material: teams present and defend their work to the class, with peer '
            'and instructor questions after each talk. Each team has 12 to 15 minutes plus questions, and submits a '
            'short written report and a tagged release of the repository.</p>'
            '<div class="callout check"><b>What each team presents.</b>'
            f'<ul class="clean" style="margin-bottom:0">{present}</ul></div>'
            '<p style="margin-top:10px">See the <a href="../index.html#project">running-project brief</a> for the '
            'full milestone description and the grading weight.</p>')
    else:
        practice_html = (
            '<h2 id="practice"><span class="ic">&#128187;</span>'
            '<span class="secttag prac">Practice &middot; 2 hours</span></h2>'
            '<p>In the practice session the instructor demonstrates the tooling, runs the code live, and works '
            'through examples. The weekly lab is then set as homework, where students apply this themselves.</p>'
            f'{render_timeline(w["prac"])}'
            f'<div class="callout hint"><b>Common pitfalls to pre-empt.</b>'
            f'<ul class="clean" style="margin-bottom:0">{pit}</ul></div>')

    pager = []
    if prev:
        pager.append(f'<a href="week{prev["n"]:02d}.html"><span class="lbl">Previous</span>Week {prev["n"]}: {esc(prev["title"])}</a>')
    if nxt:
        pager.append(f'<a class="nx" href="week{nxt["n"]:02d}.html"><span class="lbl">Next</span>Week {nxt["n"]}: {esc(nxt["title"])}</a>')
    pager_html = f'<div class="pager">{"".join(pager)}</div>' if pager else ''

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Week {w['n']} Lesson Plan: {title}</title>
<link rel="stylesheet" href="../assets/style.css"></head><body>
<div class="topnav"><div class="inner">
<a class="brand" href="../index.html">{BRAND} <span>&middot; HIT</span></a>
<nav><a href="../index.html">Home</a><a href="../index.html#weekly">Weekly materials</a><a href="../index.html#project">Project</a><a href="../references/index.html">References</a></nav>
</div></div>
<div class="wrap">
<div class="whead">
<p class="eyebrow"><span class="wbadge">Week {w['n']}</span> &nbsp; {w['part']}{pres_badge}</p>
<h1>{title}</h1>
<p class="sub">Instructor lesson plan: lecture (2 h) and practice (2 h).</p>
</div>

<div class="goals"><h2>Learning objectives</h2><ul class="clean">{obj}</ul></div>

<h2><span class="ic">&#127891;</span><span class="secttag">Lecture &middot; 2 hours</span></h2>
{render_timeline(w['lec'])}

<div class="callout miss"><b>Common misconception to confront.</b>
<p style="margin:6px 0 0"><i>Students often think:</i> {esc(w['miss'][0])}<br>
<i>Set it straight:</i> {esc(w['miss'][1])}</p></div>

<div class="callout check"><b>Check for understanding</b> (pose during the concept blocks; let students answer before revealing).
<div class="selfcheck" style="margin-top:8px">{checks}</div></div>

<div class="callout"><b>Key takeaways.</b><ul class="clean" style="margin-bottom:0">{take}</ul></div>

{practice_html}

<p style="margin-top:22px"><a class="btn" href="../references/index.html#w{nn}">Curated references</a> <a class="btn" href="../index.html#project">Project brief</a></p>
{pager_html}
</div>
<footer>{FOOT}</footer>
</body></html>
"""

def main():
    for i, w in enumerate(WEEKS):
        prev = WEEKS[i-1] if i > 0 else None
        nxt = WEEKS[i+1] if i < len(WEEKS)-1 else None
        path = os.path.join(OUT, f'week{w["n"]:02d}.html')
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(w, prev, nxt))
        print(f'wrote {path}')
    print(f'done: {len(WEEKS)} lesson plans')

if __name__ == "__main__":
    main()
