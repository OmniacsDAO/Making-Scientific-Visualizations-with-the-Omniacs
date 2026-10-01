import json, soundfile as sf, numpy as np, re, sys
from kokoro_onnx import Kokoro

SEGMENTS = [
 ("hook", "Ask a normal language model to approve a loan, and it writes you an essay, one token at a time. But software doesn't want an essay. It wants a decision, a probability, and a confidence."),
 ("pitch", "That's the pitch behind Jev, a new model from TypeSafe. Unstructured state goes in. Typed, probabilistic decisions come out."),
 ("public", "TypeSafe says Jev uses a new architecture, a parallel sampler, and a training method called Reinforcement Learning for Calibrated Decisions. What they haven't published is the weights, the architecture details, or the training recipe."),
 ("vocab", "So why not just ask a chatbot? Because inside a language model, the word yes is one token among roughly a hundred and fifty thousand. The decision is buried in a vocabulary built for writing."),
 ("options", "A decision model flips that around. It scores only the options that matter, all at once, and returns a distribution your code can branch on."),
 ("calib", "And those numbers have to mean something. If a model says seventy percent, it should be right about seventy percent of the time. That's called calibration, and it's the hard part."),
 ("roots", "Before Jev launched, two open preprints explored a strikingly similar idea."),
 ("sales1", "The first, from March 2025, turned a sales conversation into a state. Each turn becomes a high dimensional embedding, combined with conversation features."),
 ("sales2", "A reinforcement learning policy, trained with P P O, doesn't pick the next word. Its action is a probability: how likely is this conversation to convert? As the chat unfolds, that probability rises and falls."),
 ("route1", "The second, from September 2025, turned confidence into control flow. Semantic alignment, internal convergence and a learned confidence head combine into a single score."),
 ("route2", "High confidence stays on a small local model. Medium pulls in retrieval. Low escalates to a bigger model. And very low goes to a human."),
 ("caution", "The author argues this work anticipated Jev's design, and the shape is similar. But there's no public evidence of shared code or direct lineage. Resemblance is not provenance."),
 ("wave", "Then the open source community got to work. Dozens of projects now copy Jev's interface: state in, probabilities out. Underneath, they are wildly different machines."),
 ("fam1", "Family one builds a real decision model. Small encoders like Julia, Laya, Von and Verdict score each option directly. Laya even trains with reinforcement learning against proper scoring rules."),
 ("fam2", "Family two argues the decision model was already inside. Freeze a model like Qwen, read the logits for A, B and C, apply a softmax, and never generate a single word."),
 ("fam3", "Family three fine tunes that readout. Projects like Hopper, Nimble, JevK5 and Decider train small LoRA adapters, so the option logits become better probabilities."),
 ("fam4", "Family four removes the language head entirely. Kev uses a pointer head that points at the right option. Open Jev uses a single scalar head, initialized from the difference between yes and no."),
 ("fam5", "And family five turns decisions into geometry. Embed the state, embed every action, and let similarity choose."),
 ("same", "Same contract. Five very different machines. None of them is Jev, but together they show just how many ways there are to build a model that decides."),
 ("close", "And that may be the real shift: from AI that writes what to say, to AI that estimates what to do, and how sure it is."),
]

def chunks(text, maxc=78):
    parts = re.split(r'(?<=[.?!:])\s+', text)
    out = []
    for p in parts:
        while len(p) > maxc:
            cut = p.rfind(',', 0, maxc)
            if cut < 25: cut = p.rfind(' ', 0, maxc)
            out.append(p[:cut + 1].strip()); p = p[cut + 1:].strip()
        if p: out.append(p)
    return out

if __name__ == "__main__":
    voice = sys.argv[1] if len(sys.argv) > 1 else "am_michael"
    k = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
    meta = []
    for sid, txt in SEGMENTS:
        spoken = txt.replace("JevK5", "Jev K five").replace("LoRA", "Laura").replace("Qwen", "Kwen")
        s, sr = k.create(spoken, voice=voice, speed=1.0, lang="en-us")
        s = np.concatenate([s, np.zeros(int(0.05 * sr))])
        sf.write(f"/home/claude/jev/flag/vo_{sid}.wav", s, sr)
        meta.append(dict(id=sid, text=txt, dur=len(s) / sr, captions=chunks(txt)))
        print(sid, round(len(s) / sr, 2))
    json.dump(meta, open("/home/claude/jev/flag/vo_meta.json", "w"), indent=1)
    print("total", round(sum(m['dur'] for m in meta), 1))
