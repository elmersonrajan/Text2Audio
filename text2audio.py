from gtts import gTTS
from pydub import AudioSegment

# Speaker 1 (Commenter)
speaker1 = [
 
]

# Speaker 2 (Reply)
speaker2 = [

]

dialogue = [
    ("s1", speaker1[0]),
    ("s2", speaker2[0]),
    ("s1", speaker1[1]),
    ("s2", speaker2[1]),
    ("s1", speaker1[2]),
    ("s2", speaker2[2]),
    ("s1", speaker1[3]),
]

combined = AudioSegment.empty()

for i, (speaker, text) in enumerate(dialogue):
    filename = f"part_{i}.mp3"

    # Tamil voice
    tts = gTTS(text=text, lang="ta")
    tts.save(filename)

    audio = AudioSegment.from_mp3(filename)

    # Make Speaker 1 slightly higher pitch
    if speaker == "s1":
        audio = audio._spawn(
            audio.raw_data,
            overrides={"frame_rate": int(audio.frame_rate * 1.12)}
        ).set_frame_rate(audio.frame_rate)

    # Make Speaker 2 slightly deeper pitch
    else:
        audio = audio._spawn(
            audio.raw_data,
            overrides={"frame_rate": int(audio.frame_rate * 0.90)}
        ).set_frame_rate(audio.frame_rate)

    combined += audio + AudioSegment.silent(duration=700)

combined.export("tamil_conversation.wav", format="wav")

print("Created: tamil_conversation.wav")