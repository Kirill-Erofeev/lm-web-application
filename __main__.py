import os
import wave
import torch
import pyaudio
import whisper
import torchaudio
import streamlit as st
from transformers import HubertForSequenceClassification, Wav2Vec2FeatureExtractor


def record_audio(file_path, duration):
    sample_rate = 44100
    num_channels = 1
    chunk_size = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,                    
        channels=num_channels,
        rate=sample_rate,                    
        input=True,
        frames_per_buffer=chunk_size
    )

    frames = []
    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(num_channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))


def listen_audio(file_path):
    with wave.open(file_path, 'rb') as wf:
        audio = pyaudio.PyAudio()

        sample_rate = wf.getframerate()
        channels = wf.getnchannels()
        format = audio.get_format_from_width(wf.getsampwidth())

        stream = audio.open(
            rate=sample_rate,
            channels=channels,
            format=format,
            output=True
        )

        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        audio.terminate()


def audio_to_text(file_path):
    model = whisper.load_model('medium')
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    transcribed_text = result.text

    st.write(f'Язык: {max(probs, key=probs.get)}')
    st.write('Текст:', transcribed_text)


def predict_emotion(file_path):
    feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained('facebook/hubert-large-ls960-ft')
    model = HubertForSequenceClassification.from_pretrained('xbgoose/hubert-large-speech-emotion-recognition-russian-dusha-finetuned')
    num2emotion = {0: 'neutral', 1: 'angry', 2: 'positive', 3: 'sad', 4: 'other'}

    waveform, sample_rate = torchaudio.load(file_path, normalize=True)
    transform = torchaudio.transforms.Resample(sample_rate, 10000)
    waveform = transform(waveform)

    inputs = feature_extractor(
        waveform,
        sampling_rate=feature_extractor.sampling_rate,
        return_tensors='pt',
        padding=True,
        max_length=160000,
        truncation=True
    )

    logits = model(inputs['input_values'][0]).logits
    predictions = torch.argmax(logits, dim=-1)
    predicted_emotion = num2emotion[predictions.numpy()[0]]

    st.write(f'{predicted_emotion}')


st.title('Веб-приложение, использующее языковую модель')
file_path = 'audio.wav'

duration = st.slider(
    'Выберите продолжительность записи',
    min_value=2,
    max_value=10,
    value=6
)

if st.button('Записать аудио'):
    record_audio(file_path, duration)
    
if st.button('Воспроизвести аудио'):
    listen_audio(file_path)

if st.button('Вывести текст и язык'):
    audio_to_text(file_path)

if st.button('Предсказать эмоцию'):
    predict_emotion(file_path)