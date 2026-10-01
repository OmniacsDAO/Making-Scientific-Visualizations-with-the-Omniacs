# Transcript

## 1. JEV, Explained — flagship (4:10)

| Time | Section | Narration |
|---|---|---|
| 0:04.4 | hook | Ask a normal language model to approve a loan, and it writes you an essay, one token at a time. But software doesn't want an essay. It wants a decision, a probability, and a confidence. |
| 0:17.7 | pitch | That's the pitch behind Jev, a new model from TypeSafe. Unstructured state goes in. Typed, probabilistic decisions come out. |
| 0:27.2 | public | TypeSafe says Jev uses a new architecture, a parallel sampler, and a training method called Reinforcement Learning for Calibrated Decisions. What they haven't published is the weights, the architecture details, or the training recipe. |
| 0:43.8 | vocab | So why not just ask a chatbot? Because inside a language model, the word yes is one token among roughly a hundred and fifty thousand. The decision is buried in a vocabulary built for writing. |
| 0:57.4 | options | A decision model flips that around. It scores only the options that matter, all at once, and returns a distribution your code can branch on. |
| 1:07.7 | calib | And those numbers have to mean something. If a model says seventy percent, it should be right about seventy percent of the time. That's called calibration, and it's the hard part. |
| 1:19.1 | roots | Before Jev launched, two open preprints explored a strikingly similar idea. |
| 1:24.8 | sales1 | The first, from March 2025, turned a sales conversation into a state. Each turn becomes a high dimensional embedding, combined with conversation features. |
| 1:37.1 | sales2 | A reinforcement learning policy, trained with P P O, doesn't pick the next word. Its action is a probability: how likely is this conversation to convert? As the chat unfolds, that probability rises and falls. |
| 1:52.7 | route1 | The second, from September 2025, turned confidence into control flow. Semantic alignment, internal convergence and a learned confidence head combine into a single score. |
| 2:06.0 | route2 | High confidence stays on a small local model. Medium pulls in retrieval. Low escalates to a bigger model. And very low goes to a human. |
| 2:16.6 | caution | The author argues this work anticipated Jev's design, and the shape is similar. But there's no public evidence of shared code or direct lineage. Resemblance is not provenance. |
| 2:29.2 | wave | Then the open source community got to work. Dozens of projects now copy Jev's interface: state in, probabilities out. Underneath, they are wildly different machines. |
| 2:41.4 | fam1 | Family one builds a real decision model. Small encoders like Julia, Laya, Von and Verdict score each option directly. Laya even trains with reinforcement learning against proper scoring rules. |
| 2:56.3 | fam2 | Family two argues the decision model was already inside. Freeze a model like Qwen, read the logits for A, B and C, apply a softmax, and never generate a single word. |
| 3:09.8 | fam3 | Family three fine tunes that readout. Projects like Hopper, Nimble, JevK5 and Decider train small LoRA adapters, so the option logits become better probabilities. |
| 3:23.0 | fam4 | Family four removes the language head entirely. Kev uses a pointer head that points at the right option. Open Jev uses a single scalar head, initialized from the difference between yes and no. |
| 3:37.3 | fam5 | And family five turns decisions into geometry. Embed the state, embed every action, and let similarity choose. |
| 3:45.9 | same | Same contract. Five very different machines. None of them is Jev, but together they show just how many ways there are to build a model that decides. |
| 3:56.1 | close | And that may be the real shift: from AI that writes what to say, to AI that estimates what to do, and how sure it is. |
