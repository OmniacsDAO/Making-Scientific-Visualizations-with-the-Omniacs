import sys, json, subprocess, wave, numpy as np
sys.argv_saved = sys.argv; sys.argv = sys.argv[:1]
import finish
video, vo, secs, outp = sys.argv_saved[1:5]
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",video]).decode())
mus = finish.music(dur, json.loads(secs))
with wave.open('/tmp/_m2.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(44100); w.writeframes((mus*32767).astype(np.int16).tobytes())
fc = ("[0:a]aresample=44100,aformat=channel_layouts=stereo,volume=1.6,asplit=2[vo][sc];"
      "[1:a]volume=0.9[mu];[mu][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
      "[vo][duck]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]")
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",vo,"-i","/tmp/_m2.wav","-i",video,"-filter_complex",fc,
                "-map","2:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","256k","-shortest","-movflags","+faststart",outp],check=True)
print("done", outp, round(dur,1))
