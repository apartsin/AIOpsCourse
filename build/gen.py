# -*- coding: utf-8 -*-
"""Generate weekly lesson-plan pages for Production Engineering for AI Systems.
Each week -> lessons/weekNN.html with a 2 h lecture timeline and a 2 h practice
timeline, matching the DLCourseHIT house style (assets/style.css).
v2: cloud fundamentals from zero (wk 2), LLM/AI-API foundations from zero (wk 9),
data lakes + medallion (wk 5), streaming (wk 6), managed agents + MCP (wk 11),
use cases threaded throughout (IoT, chatbot, document processing)."""
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
 "n":1,"part":"Part I &middot; Foundations &amp; the Cloud",
 "title":"Production Engineering & the Ops Landscape",
 "obj":["Explain why production systems fail in operations more than in modelling.",
        "Map the six operational layers (DevOps through AIOps) and how they stack.",
        "Name the course use-case domains and pick a direction for the team project."],
 "lec":[("0:00-0:10",10,"Welcome & objectives","Course mechanics, the running project, and this week's objectives."),
        ("0:10-0:30",20,"Motivation","The prototype-to-production gap: an accurate model is a small part of a working system. Outages, latency, stale data, and runaway cost hurt more than a point of accuracy."),
        ("0:30-1:10",40,"The reliability stack & the SRE mindset",
            ["Service-level indicators, objectives, and error budgets: reliability as a measurable contract.",
             "Toil, on-call, and the development-versus-operations tension SRE was created to resolve.",
             "What 'production-ready' means: availability, latency, cost, recoverability, and observability.",
             "Board work: turning a vague 'it should be reliable' into an SLO with a number."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"The six layers & the course use cases",
            ["DevOps, DataOps, MLOps, LLMOps, AgentOps, AIOps: what each one owns and how they compose.",
             "The three running use cases: IoT telemetry (sensor streams, anomaly alerts), a document-QA chatbot (RAG), and document processing (extraction at scale).",
             "How the running project touches every layer over the semester; teams pick a domain by week 3."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Revisit the checks below and preview the toolchain setup.")],
 "miss":("If the model is accurate, the system is done.",
         "Accuracy is one property. Availability, latency, cost, data freshness, and recoverability are separate properties that usually dominate production outcomes."),
 "checks":[("Give one failure a 99%-accurate model can still cause in production.",
            "It can serve at 5 s latency, crash under load, or be fed stale or garbage inputs. Accuracy says nothing about any of these."),
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
         ("1:50-2:00",10,"Wrap-up & project kickoff","Brief the project: teams pick a use-case domain by week 3.")],
 "pit":["Never commit secrets or large data to Git; use .gitignore and environment variables from day one.",
        "A container that runs only on your laptop usually pins no versions. Pin them."],
},
{
 "n":2,"part":"Part I &middot; Foundations &amp; the Cloud",
 "title":"Cloud Computing Fundamentals",
 "obj":["Explain the core cloud primitives: compute, storage, and networking.",
        "Choose between IaaS, PaaS, SaaS, and serverless for a given workload.",
        "Reason about regions, availability zones, shared responsibility, and cost.",
        "Stand up a small service on a cloud free tier."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Last week's reliability stack; today: the platform everything runs on. No prior cloud experience assumed."),
        ("0:10-0:30",20,"Motivation","Every production AI system runs on someone's cloud. The bill, the latency, and the blast radius of a failure are design inputs from day one, not afterthoughts."),
        ("0:30-1:10",40,"Compute & storage primitives",
            ["Compute: virtual machines, containers, and serverless functions; what each abstracts away.",
             "Storage: object versus block versus file; why object storage (the S3 model) is the default home for datasets and model artifacts.",
             "Managed databases and queues: paying the provider to carry the operational burden.",
             "Board work: mapping the document-processing use case onto compute + object storage + a queue."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Networking, deployment models & cost",
            ["Networking essentials: virtual networks, load balancers, DNS, HTTPS termination.",
             "IaaS versus PaaS versus SaaS, and serverless: the control-versus-toil trade-off.",
             "Regions and availability zones; what multi-AZ buys you.",
             "The shared-responsibility model and the pay-as-you-go cost model (compute time, storage, egress)."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview standing up the first cloud service.")],
 "miss":("The cloud is just someone else's computer, so nothing really changes.",
         "Elasticity, managed services, per-use billing, and the shared-responsibility split change how systems are designed, costed, and secured. A design that ignores them is either fragile or expensive."),
 "checks":[("You need to store trained model artifacts and serve them to many machines. Object, block, or file storage, and why?",
            "Object storage: cheap, durable, URL-addressable, and built for many readers. Block storage belongs to one VM; file shares scale poorly for this."),
           ("What failure does deploying across two availability zones protect against?",
            "The loss of a single data center (power, cooling, network). It does not protect against a region-wide outage or a bad deploy you ship to both zones.")],
 "take":["Compute, storage, and networking primitives compose into any architecture.",
         "The deployment model (IaaS to serverless) is a control-versus-toil trade-off.",
         "Cost and blast radius are design inputs; budgets and multi-AZ are decisions, not defaults."],
 "prac":[("0:00-0:10",10,"Setup & recap","Cloud free-tier accounts ready; recap the primitives."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Launch a VM, connect to it, and run the week-1 container on it.",
             "Create an object-storage bucket; upload and download an artifact from code.",
             "Set a budget alert before anything else."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Deploy the same service again as a PaaS/serverless app; compare effort and control.",
             "Walk the price calculator: what this week's lab actually costs.",
             "Tear everything down and verify nothing is still billing."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the primitives and brief the lab.")],
 "pit":["A forgotten running instance silently burns the free tier; set budget alerts first and tear down last.",
        "Never put cloud credentials in code or notebooks; use roles and environment configuration."],
},
{
 "n":3,"part":"Part II &middot; DevOps",
 "title":"CI/CD, Testing & REST Services",
 "obj":["Build a CI pipeline that lints, tests, builds, and produces an artifact.",
        "Apply the testing pyramid to a service.",
        "Design, version, and containerise a REST API."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Cloud primitives; today: making change safe and shipping a real service interface."),
        ("0:10-0:30",20,"Motivation","Manual deploys break in ways no one can reproduce. Fast, repeatable, automated feedback is what makes change safe, and the REST API is the contract everything else calls."),
        ("0:30-1:10",40,"CI/CD & the testing pyramid",
            ["Pipelines, stages, and artifacts; what 'continuous integration' actually means.",
             "The testing pyramid: many fast unit tests, fewer integration tests, very few end-to-end.",
             "Trunk-based development versus long-lived branches and their effect on integration pain.",
             "Continuous delivery versus continuous deployment; infrastructure as code in one slide."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"REST services done properly",
            ["Resources, verbs, and status codes; JSON request/response contracts.",
             "Versioning an API so consumers do not break when it evolves.",
             "Containerising the service; health endpoints the orchestrator will need next week."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building the pipeline and the service.")],
 "miss":("CI is just running the tests.",
         "CI is the discipline of integrating small changes into a shared mainline continuously, with automated verification. The test run is one stage of that, not the whole idea."),
 "checks":[("Why are end-to-end tests the thin top of the pyramid, not the base?",
            "They are slow, flaky, and expensive. Most coverage should come from fast unit tests, with fewer integration tests and very few end-to-end."),
           ("What does versioning an API buy you?",
            "Consumers keep working when the API evolves: old clients stay on v1 while v2 changes the contract, and deprecation becomes a managed process instead of a breakage.")],
 "take":["CI integrates small changes continuously; the test run is one stage.",
         "Push coverage down the pyramid: fast unit tests are the base.",
         "An API contract is a promise; version it and guard it with tests."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the team repository and the Actions tab."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Build a FastAPI service with two endpoints and a health check.",
             "Write unit and integration tests; watch the pyramid in miniature.",
             "Write a GitHub Actions workflow: lint, test, build, upload artifact."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Containerise the service and push the image to a registry from CI.",
             "Make a failing test block the merge via a required check.",
             "Version the API and show an old client surviving a v2 change."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Summarise the pipeline stages and brief the lab.")],
 "pit":["Flaky tests erode trust in CI; quarantine and fix them rather than re-running.",
        "A 40-minute pipeline kills the feedback loop; parallelise and cache."],
},
{
 "n":4,"part":"Part II &middot; DevOps",
 "title":"Orchestration, Deployment Patterns & Observability",
 "obj":["Run a containerised service under an orchestrator.",
        "Choose and execute a rollout pattern (blue-green, canary).",
        "Instrument the three pillars of observability and read them."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From one container to a fleet; today's objectives."),
        ("0:10-0:30",20,"Motivation","Running one container is easy; running many with health checks, scaling, and safe rollouts is why orchestration exists, and you cannot operate what you cannot see."),
        ("0:30-1:10",40,"Kubernetes primitives & rollouts",
            ["Pods, deployments, and services; how desired state is reconciled.",
             "Health checks, autoscaling, and resource requests and limits.",
             "Blue-green versus canary deployments and when each fits.",
             "GitOps in one slide: the cluster state lives in Git and an agent (Argo CD) reconciles it."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Observability: logs, metrics, traces",
            ["The three pillars and what each answers; monitoring versus observability.",
             "The RED method (rate, errors, duration) for choosing what to measure.",
             "Tail latency: why p95/p99 matter and averages lie; structured, high-cardinality telemetry."]),
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
            ["Deploy the week-3 service: a Deployment plus a Service.",
             "Scale it, kill a pod, and watch the orchestrator self-heal.",
             "Perform a canary rollout and shift traffic gradually."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Wire Prometheus to scrape metrics and Grafana to display them.",
             "Build a RED dashboard and read p95/p99 latency under a small load test."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the rollout and observability setup.")],
 "pit":["p50 latency hides the tail; always watch p95/p99.",
        "Unstructured logs are hard to query; emit structured (JSON) logs."],
},
{
 "n":5,"part":"Part III &middot; DataOps",
 "title":"Data Lakes, Pipelines & Versioning",
 "obj":["Explain the data lake, the lakehouse, and the medallion architecture.",
        "Build an orchestrated data pipeline with retries and backfills.",
        "Version a dataset and reproduce a result from a pinned snapshot."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From services to the data that feeds them; objectives."),
        ("0:10-0:30",20,"Motivation","Garbage in, garbage out: most ML incidents trace to data, not the model. Data needs an architecture, a refinery, and version control, exactly like code."),
        ("0:30-1:05",35,"Data lakes, the lakehouse & medallion architecture",
            ["From warehouse to data lake to lakehouse: object-storage lakes with table semantics (Delta, Iceberg).",
             "The medallion architecture: bronze (raw, immutable), silver (cleaned, conformed), gold (business- and feature-ready).",
             "Why staged refinement beats a single 'clean it later' dump; ownership and auditability per layer.",
             "Board work: the IoT telemetry use case as bronze sensor events, silver de-duplicated readings, gold hourly features."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:40",25,"Pipelines & data versioning",
            ["DAG orchestration (Airflow, Dagster); scheduling, retries, backfills, idempotency.",
             "Batch versus streaming, previewed; next week goes deeper.",
             "Data versioning with DVC or lakeFS: pinning the exact snapshot that produced a result; lineage."]),
        ("1:40-2:00",20,"Wrap-up & Presentation-1 logistics","Recap and brief the specification presentation rubric.")],
 "miss":("A data lake is a dump; structure can be added later for free.",
         "Without explicit zones and contracts the lake becomes a swamp nobody trusts. The medallion architecture makes refinement stages, quality expectations, and ownership explicit from the first byte."),
 "checks":[("What lives in each medallion layer?",
            "Bronze: raw, immutable, as-ingested events. Silver: cleaned, de-duplicated, conformed records. Gold: aggregated, business- or feature-ready tables that models and dashboards consume."),
           ("Why must an orchestrated task be idempotent?",
            "Retries and backfills re-execute tasks. A non-idempotent task double-writes or corrupts state when it runs twice.")],
 "take":["The lakehouse is lake storage plus table semantics; medallion stages the refinement.",
         "Most ML production bugs are data bugs.",
         "Pinning a data version is what makes a result reproducible."],
 "prac":None,
 "pit":["A specification without measurable SLOs is not a specification; name the numbers.",
        "Hardcoding 'today' in a pipeline breaks backfills; parameterise the run date."],
 "pres":"Presentation 1 &middot; Specification",
 "present":["Problem statement and success metrics (SLOs) for the chosen use case (IoT, chatbot, document processing, or another approved domain).",
            "System and data architecture, including the medallion layout of the data.",
            "DevOps plan: repository, CI skeleton, cloud services to be used.",
            "Risk and governance register."],
},
{
 "n":6,"part":"Part III &middot; DataOps",
 "title":"Data Quality, Contracts, Streaming & Feature Stores",
 "obj":["Enforce data quality continuously with validation rules.",
        "Define a data contract between a producer and a consumer.",
        "Explain streaming ingestion (Kafka) and where it beats batch.",
        "Explain feature stores and the cause of train/serve skew."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Lakes and pipelines; today: keeping the data trustworthy and fresh."),
        ("0:10-0:30",20,"Motivation","Upstream schema changes and silent quality drops break models without any error. Quality must be guarded at the boundary, continuously; and some use cases cannot wait for tonight's batch."),
        ("0:30-1:05",35,"Data quality & contracts",
            ["Validation with Great Expectations: schema, ranges, nullity, uniqueness, applied at the bronze-to-silver boundary.",
             "Data contracts: the schema, semantics, freshness, and quality a producer guarantees.",
             "Quality SLAs; when to fail the pipeline loudly versus quarantine bad rows."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:50",35,"Streaming & feature stores",
            ["Kafka in one lecture: topics, producers, consumers, consumer groups; at-least-once delivery.",
             "When streaming beats batch: the IoT use case (sensor alerts) versus nightly aggregates.",
             "Feature stores: offline versus online features, point-in-time correctness.",
             "Train/serve skew: when serving features differ from training features, and why it is silent."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview validating the project dataset and a first stream.")],
 "miss":("Data validation is a one-time cleaning step.",
         "Quality is a continuous contract checked on every run. Upstream producers keep changing, so validation must guard the boundary forever, not once."),
 "checks":[("What is train/serve skew and one cause?",
            "The features seen at serving differ from those at training, e.g. a transformation applied only in the training notebook, or time leakage in offline features."),
           ("When does streaming genuinely beat batch?",
            "When the value of the data decays faster than the batch period: fraud signals, sensor alarms, live personalisation. If a nightly aggregate is fine, batch is simpler and cheaper.")],
 "take":["Data quality is a continuous contract, not a one-off clean.",
         "Streams are the freshness lever; pay their complexity only when freshness pays.",
         "Train/serve skew is a top cause of silent model failure."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the project dataset and the validation suite."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Write Great Expectations suites for the bronze-to-silver boundary.",
             "Break the data on purpose; watch validation fail loudly and quarantine rows.",
             "Write a one-page data contract for the project's main source."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Stand up a single-broker Kafka; produce and consume a simulated sensor stream.",
             "Land the stream into the bronze layer and run the silver transform on top."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap quality gates and the stream-to-lake path.")],
 "pit":["Validate at the boundary you do not control, not only your own outputs.",
        "A consumer that silently trusts the producer's schema is the first thing to break."],
},
{
 "n":7,"part":"Part IV &middot; MLOps",
 "title":"Experiment Tracking, Model Registry & Serving",
 "obj":["Track experiments so any result is reproducible.",
        "Version models in a registry with governed stage transitions.",
        "Serve a model behind a REST endpoint and roll it out safely."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Trustworthy data; today: the model lifecycle from training run to live endpoint."),
        ("0:10-0:30",20,"Motivation","'Which run produced this model?' is a question most teams cannot answer, and training is the easy part: serving, versioning, and safely replacing models is where production ML lives."),
        ("0:30-1:10",40,"Tracking & the model registry",
            ["Logging parameters, metrics, and artifacts with MLflow; comparing runs and reading curves.",
             "Reproducibility: pinning the git SHA, the data version (week 5), and the environment to each run.",
             "Model versioning in a registry: staging, production, archived; governed promotion and rollback.",
             "Model cards: intended use, data, metrics, and limitations."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Model serving & safe rollout",
            ["Packaging a model with pinned dependencies; the serving runtime.",
             "Online versus batch serving; the REST endpoint as the model's API contract.",
             "Shadow, canary, and A/B for models; the offline-online gap."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview serving the project model.")],
 "miss":("A good offline metric guarantees a good online result.",
         "Offline metrics use historical data and proxy objectives. Feedback loops, latency, and distribution shift mean online behaviour can differ, so validate with shadow, canary, or A/B."),
 "checks":[("What three things must a tracked run pin to be reproducible?",
            "The code version (git SHA), the data version, and the environment plus hyperparameters."),
           ("What is a shadow deployment?",
            "Sending real traffic to the new model in parallel without using its responses, to compare it against production safely.")],
 "take":["A metric is reproducible only when tied to code, data, and environment.",
         "A registry gives governed, auditable model promotion and rollback.",
         "Offline metrics are a proxy; confirm online with shadow or canary."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open a training script for the project model."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Instrument training with MLflow: params, metrics, artifacts, plus git SHA and data version.",
             "Register the model; promote it staging to production; roll back.",
             "Wrap the model in a serving runtime behind a REST endpoint."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Deploy model v2 as a canary next to v1; compare latency and predictions.",
             "Measure p95 latency under load; warm the model to cut cold starts."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the lifecycle from run to endpoint.")],
 "pit":["An unpinned data version makes the run impossible to reproduce.",
        "Serving a pickled model without pinned library versions breaks silently."],
},
{
 "n":8,"part":"Part IV &middot; MLOps",
 "title":"Monitoring, Model Drift & Governance",
 "obj":["Monitor a deployed model and its inputs.",
        "Distinguish data drift from concept drift and detect each.",
        "Define retraining triggers and an audit trail."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Served models; the day-two problem; objectives."),
        ("0:10-0:30",20,"Motivation","Models decay silently as the world shifts. Labels often arrive late, so live accuracy is unknown and inputs become the early-warning signal."),
        ("0:30-1:05",35,"Monitoring & model drift",
            ["Data drift versus concept drift: which distribution changed.",
             "Detectors: population stability index, KS test, embedding distance.",
             "Prediction-distribution and proxy monitoring when labels are delayed.",
             "The IoT example: a recalibrated sensor shifts the inputs weeks before accuracy visibly drops."]),
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
 "prac":None,
 "pit":["A drift alarm with no playbook is noise; attach an action to every detector.",
        "Watching only accuracy misses drift while labels are delayed."],
 "pres":"Presentation 2 &middot; Interim",
 "present":["Working data pipeline through bronze and silver, with validation gates.",
            "Experiment tracking and a versioned model in the registry.",
            "A first deployed endpoint, with CI/CD demonstrated live.",
            "Monitoring and drift plan."],
},
{
 "n":9,"part":"Part V &middot; LLMOps &amp; AgentOps",
 "title":"LLM Foundations: AI APIs, Tokens & the Token Economy",
 "obj":["Explain what an LLM does, from an engineering standpoint.",
        "Call an AI API well: prompts, parameters, structured outputs.",
        "Reason about tokens, context windows, pricing, and model tiers.",
        "Survey the managed AI services (Bedrock-class platforms)."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From classical models to language models. No prior LLM experience assumed."),
        ("0:10-0:30",20,"Motivation","Most AI features today are built on a large model behind an API. The engineering questions are not 'how was it trained' but cost, latency, reliability, and correctness of something you do not control."),
        ("0:30-1:10",40,"LLMs for engineers",
            ["What the model does: next-token prediction over a context window; why that one sentence explains most behaviour.",
             "Tokens and tokenization: the unit of cost, latency, and length limits.",
             "The API call: system and user prompts, temperature, stop conditions.",
             "Structured outputs: JSON schemas and function signatures, turning free text into engineering-grade responses.",
             "Failure modes: hallucination, nondeterminism, prompt sensitivity; live demo on the document-processing use case."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"The token economy & managed AI services",
            ["Pricing per input and output token; estimating what a feature costs at scale.",
             "The cost levers: shorter context, prompt caching, batching, cheaper model tiers; flagship versus mini models.",
             "Rate limits, quotas, and why retries without backoff double the bill.",
             "Managed AI platforms (AWS Bedrock, Microsoft Foundry, Google Vertex AI): model catalog, guardrails, knowledge bases, evals behind one console; platform versus direct API trade-off."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview the first API calls and the cost measurements.")],
 "miss":("An LLM API call behaves like a normal deterministic function.",
         "The same input can produce different outputs (sampling), the contract is tokens rather than characters, and the model behind the endpoint can change. Engineering around it needs structured outputs, retries with backoff, pinned model versions, and evaluation."),
 "checks":[("Why does a longer context cost more and respond slower?",
            "Billing is per token on both input and output, and attention computation grows with sequence length, so every extra token costs money and latency."),
           ("Name two levers that cut an LLM feature's cost before switching models.",
            "Shorten the prompt and context, cache repeated calls; batching requests and routing easy queries to a cheaper tier are next.")],
 "take":["The model API is the new runtime; cost and latency are token-driven.",
         "Structured outputs turn LLM calls into engineering-grade components.",
         "Managed platforms bundle catalog, guardrails, and RAG; direct APIs trade that for control."],
 "prac":[("0:00-0:10",10,"Setup & recap","API keys issued through the course proxy; recap tokens."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["First API calls (OpenAI or Anthropic): system prompt, user prompt, temperature.",
             "Count the tokens; measure latency and compute the cost of each call.",
             "Extract structured fields from a sample invoice (document-processing use case) with a JSON schema."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Run the same task on a flagship and a mini model; compare quality, latency, and cost.",
             "Tour a managed platform console (Bedrock-class): catalog, guardrails, knowledge bases.",
             "Estimate the monthly bill for the project's LLM feature at 10k requests/day."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the token economy and brief the lab.")],
 "pit":["Never hardcode API keys; use environment configuration and the course proxy.",
        "Pin the model version: silent model updates change behaviour under you."],
},
{
 "n":10,"part":"Part V &middot; LLMOps &amp; AgentOps",
 "title":"LLMOps: RAG, Gateways, Evaluation & Guardrails",
 "obj":["Build a retrieval-augmented generation service.",
        "Route LLM traffic through a gateway with fallbacks and budgets.",
        "Evaluate generation quality with an eval set; know LLM-as-judge pitfalls.",
        "Apply guardrails against unsafe and injected behaviour."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From single calls to an operated LLM service; objectives."),
        ("0:10-0:30",20,"Motivation","'Looks good' is not evaluation, and a model that answers from its training data alone cannot answer about your documents. RAG grounds it; gateways, evals, and guardrails make it operable."),
        ("0:30-1:10",40,"RAG & the serving stack",
            ["Embeddings and vector databases; chunking and retrieval; assembling a grounded prompt with citations.",
             "The chatbot use case end to end: documents to index to retrieval to answer.",
             "Prompts as versioned program logic: review, rollback, regression-test.",
             "Serving choices: hosted APIs versus self-hosted open weights (vLLM); the gateway pattern (LiteLLM): one endpoint, many providers, fallbacks, keys, budgets."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"Evaluation & guardrails",
            ["Building an offline eval set that represents real usage; faithfulness and answer relevance.",
             "LLM-as-judge and its biases: position, verbosity, self-preference; calibrate against human labels.",
             "Guardrails: input and output filtering, PII handling, prompt injection and its defenses.",
             "Caching and cost in the operated service."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building the RAG service and its eval harness.")],
 "miss":("RAG means the model can no longer hallucinate.",
         "Retrieval grounds the answer, but the model can still ignore or misread the context. Faithfulness depends on retrieval quality, chunking, and citations, and must be measured rather than assumed."),
 "checks":[("Why version prompts like code?",
            "Prompts are program logic: a prompt change alters behaviour, so it must be tracked, reviewed, and rollback-able like any other code."),
           ("Name two biases of an LLM judge.",
            "Position bias (favouring the first answer), verbosity bias (favouring longer answers), and self-preference (favouring its own style); calibrate against human labels before trusting it.")],
 "take":["Retrieval quality bounds RAG quality; measure faithfulness, do not assume it.",
         "A gateway centralises routing, keys, fallbacks, and budgets.",
         "The eval set is the regression suite for prompts; run it on every change."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the course document corpus and the vector database."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Embed and index the corpus; retrieve and assemble a grounded prompt with citations.",
             "Stand up LiteLLM with two providers; demonstrate fallback and a budget cap.",
             "Version the prompt and swap versions live."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Build a small eval harness; score faithfulness on a labelled set; run a regression on a prompt change.",
             "Attempt a prompt injection; add input/output guardrails and re-test.",
             "Add a response cache and measure the cost drop."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap the operated RAG stack.")],
 "pit":["Embedding and querying with different models silently destroys retrieval.",
        "A 10-item eval set measures noise; build a representative one."],
},
{
 "n":11,"part":"Part V &middot; LLMOps &amp; AgentOps",
 "title":"Agents & AgentOps: Tools, MCP & Managed Agents",
 "obj":["Explain the agent loop and tool use (function calling), from zero.",
        "Build and trace a tool-using agent; evaluate it at the step level.",
        "Bound agents with step, cost, and permission limits.",
        "Compare self-built agents with managed agent services."],
 "lec":[("0:00-0:10",10,"Recap & objectives","From answering to acting. No prior agent experience assumed."),
        ("0:10-0:30",20,"Motivation","An agent is an LLM in a loop with tools: it can look things up, call APIs, and act. Autonomy plus tools is powerful and is also a brand-new failure surface: runaway loops, wrong tool calls, unbounded cost."),
        ("0:30-1:10",40,"Agents from first principles",
            ["The plan-act-observe loop; function calling: the model emits a structured tool call, your code executes it.",
             "Tools, memory (context versus long-term stores), and termination.",
             "MCP, the Model Context Protocol: a standard interface between agents and tools, adopted across vendors.",
             "Where agents fail: hallucinated arguments, tool errors, loops; live demo on the document-processing use case."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"AgentOps & managed agents",
            ["Tracing agents as spans: every step, tool call, and decision, in Langfuse or LangSmith.",
             "Step-level evaluation, not just final-output evaluation.",
             "Bounds: max steps, wall-clock and cost budgets, least-privilege tools, human-in-the-loop checkpoints.",
             "Managed agent services (Bedrock AgentCore, Foundry Agent Service): hosted loop, tools, and tracing; control versus toil, again."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview building and bounding the first agent.")],
 "miss":("An agent loop will stop on its own.",
         "Without explicit step, cost, and wall-clock bounds and a termination criterion, agents loop, retry, and burn budget. Bounds and an error classifier are mandatory: a retry-on-any-exception loop spins forever on a caller-side bug."),
 "checks":[("Why trace at the step level, not just the final output?",
            "Failures hide in intermediate tool calls and decisions; step traces localise exactly where the agent went wrong."),
           ("Name two bounds every agent loop needs.",
            "A maximum step or iteration cap and a wall-clock or cost budget, with an error classifier so caller-side bugs fail fast instead of retrying.")],
 "take":["An agent is an LLM in a loop with tools; autonomy is a new failure surface.",
         "MCP standardises the agent-tool interface across vendors.",
         "Trace and evaluate at the step level; bound steps, cost, and permissions."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open the agent scaffold and the tracing dashboard."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Give the agent two tools (a document search and a calculator); run the loop on real tasks.",
             "Add tracing; read the spans for a successful and a failing run.",
             "Trigger a failure (a hallucinated argument) and locate it in the trace."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Add a max-step cap, a cost budget, and an error classifier; watch a runaway loop get caught.",
             "Wrap one tool as an MCP server and connect the agent to it.",
             "Tour a managed agent service and map each concept onto it."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap tracing, bounds, and the MCP pattern.")],
 "pit":["Broad tool permissions are dangerous; grant least privilege.",
        "A retry-on-any-exception loop spins on caller bugs; classify the error first."],
},
{
 "n":12,"part":"Part VI &middot; AIOps, Security &amp; Governance",
 "title":"AIOps: AI for IT Operations",
 "obj":["Apply anomaly detection to service telemetry.",
        "Reduce alert noise through correlation and deduplication.",
        "Use LLM-assisted triage and automate a safe remediation."],
 "lec":[("0:00-0:10",10,"Recap & objectives","Operating AI, and now AI for operations; objectives."),
        ("0:10-0:30",20,"Motivation","No human can watch millions of metrics. Alert fatigue means real incidents get missed in the noise; the goal is fewer, sharper, actionable signals, with AI now helping triage them."),
        ("0:30-1:10",40,"AIOps techniques",
            ["Anomaly detection on metrics and logs; handling seasonality.",
             "Alert correlation and deduplication: a burst of symptoms becomes one incident.",
             "Root-cause hints: grouping symptoms to a likely cause; the IoT fleet as the running example.",
             "Precision over volume: an alert must be actionable, or it trains people to ignore alerts."]),
        ("1:10-1:20",10,"Break",None),
        ("1:20-1:50",30,"LLM-assisted operations & incident automation",
            ["LLM-assisted triage: summarising an incident from telemetry, suggesting probable causes and runbooks.",
             "Runbooks and auto-remediation for known failure modes; self-healing and its risks.",
             "Rate limits, circuit breakers, and human-in-the-loop for risky actions.",
             "An honest framing: AI helps where telemetry hygiene is good; it cannot fix missing observability."]),
        ("1:50-2:00",10,"Wrap-up & practice preview","Preview anomaly detection on the project telemetry.")],
 "miss":("More alerts means a safer system.",
         "Alert overload causes fatigue and missed real incidents. The goal is fewer, correlated, actionable alerts: precision over volume."),
 "checks":[("Why is seasonality important for anomaly detection?",
            "Normal traffic has daily and weekly cycles; a detector that ignores seasonality flags every Monday-morning spike as an anomaly."),
           ("Name one risk of automated remediation.",
            "A wrong auto-action, or a feedback loop, can amplify an incident. Guardrails, rate limits, and human-in-the-loop for risky actions are required.")],
 "take":["AIOps trades alert volume for alert precision.",
         "LLM-assisted triage accelerates humans; it does not replace telemetry hygiene.",
         "Automated remediation needs circuit breakers and rate limits."],
 "prac":[("0:00-0:10",10,"Setup & recap","Open a telemetry stream from the project service."),
         ("0:10-1:00",50,"Instructor demonstrations",
            ["Run anomaly detection on a seasonal metric and tune sensitivity.",
             "Correlate and deduplicate a burst of alerts into one incident.",
             "Use an LLM to summarise the incident from its telemetry and propose a runbook."]),
         ("1:00-1:10",10,"Break",None),
         ("1:10-1:50",40,"Instructor demonstrations (continued)",
            ["Write one auto-remediation rule with a rate limit and circuit breaker.",
             "Trigger it safely and confirm it backs off."]),
         ("1:50-2:00",10,"Wrap-up & lab brief","Recap AIOps and safe automation.")],
 "pit":["A self-healing action without a circuit breaker can flap; bound it.",
        "An anomaly is not an incident; tie every alert to impact."],
},
{
 "n":13,"part":"Part VI &middot; AIOps, Security &amp; Governance",
 "title":"Security, Governance & Synthesis",
 "obj":["Secure the software, data, and model supply chain.",
        "Apply the OWASP Top 10 for LLM applications.",
        "Synthesise the six layers into one operational stack."],
 "lec":[("0:00-0:10",10,"Recap & objectives","The whole stack; objectives."),
        ("0:10-0:30",20,"Motivation","AI systems widen both the attack surface and the governance surface: new data, new models, new autonomy, all of which can be abused or audited."),
        ("0:30-1:05",35,"Security & supply chain",
            ["Secrets management, least privilege, and dependency and SBOM hygiene.",
             "The model and data supply chain: poisoned datasets and backdoored weights; provenance and pinning.",
             "The OWASP Top 10 for LLM applications as the working checklist: prompt injection, insecure output handling, excessive agency, and the rest."]),
        ("1:05-1:15",10,"Break",None),
        ("1:15-1:40",25,"Governance & synthesis",
            ["Privacy, PII handling, and compliance obligations; audit trails across the stack.",
             "Responsible AI in operations: documentation that stays live.",
             "Synthesis: how DevOps through AIOps compose into one auditable system; what to learn next."]),
        ("1:40-2:00",20,"Wrap-up & course synthesis","Recap the course and brief the final presentation.")],
 "miss":("Security and governance are a final checklist.",
         "They are cross-cutting properties designed in from week one: secrets, least privilege, data contracts, and audit trails. Bolting them on at the end does not work."),
 "checks":[("Name one supply-chain risk unique to ML and LLM systems.",
            "A poisoned or backdoored pretrained model or dataset pulled from a public hub; verify provenance and pin versions."),
           ("Why keep audit trails across the whole stack?",
            "For compliance, incident forensics, and reproducibility: to answer which data, model, and prompt produced a decision, and who approved it.")],
 "take":["Security and governance are designed in from week one, not appended.",
         "The OWASP LLM Top 10 is the working checklist for LLM-app security.",
         "The six layers compose into one auditable operational stack."],
 "prac":None,
 "pit":["Secrets in client-side code or logs leak; keep them server-side and rotated.",
        "A model card nobody maintains is theatre; keep documentation live."],
 "pres":"Presentation 3 &middot; Final",
 "present":["End-to-end production demo of the chosen use case.",
            "Observability and an AIOps capability in place.",
            "Evaluation, guardrails, and a cost/latency report (the token economy of the feature).",
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

    # presentation weeks still carry pitfalls inside the lecture context
    extra_pit = ''
    if w.get("pres"):
        extra_pit = (f'<div class="callout hint"><b>Common pitfalls to pre-empt.</b>'
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
<nav><a href="../index.html">Home</a><a href="../prereq/index.html">Prerequisites</a><a href="../index.html#weekly">Weekly materials</a><a href="../index.html#project">Project</a><a href="../references/index.html">References</a></nav>
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
{extra_pit}

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
