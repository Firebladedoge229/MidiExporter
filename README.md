![Midi Exporter](https://github.com/Firebladedoge229/MidiExporter/blob/main/midiexporter.png?raw=true)

# Midi Exporter

A exporter that utilizes MIDI to MP3 conversion.

## Installation

Simply run the executable found at the [Releases](https://github.com/Firebladedoge229/MidiExporter/releases/latest) page.

When running, a [Windows Defender SmartScreen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) window may display as your anti-virus triggers, this is due to the application signing system by [PyInstaller](https://github.com/pyinstaller/pyinstaller).

If you are suspicious, feel free to compile the code yourself!

### Build Command
```py
pyinstaller --onefile --noconsole --icon=midi.ico --add-data="midi.ico;." --add-data="sv_ttk;sv_ttk" --add-data="ffmpeg;ffmpeg" --add-data="fluidsynth;fluidsynth" midiexporter.py
```
![Showcase](https://github.com/Firebladedoge229/MidiExporter/assets/72758695/c203d502-0aa9-4078-a647-42d83e713318)

## Requirements

~~[FFmpeg](https://ffmpeg.org/download.html)~~ - WAV to MP3\
~~[FluidSynth](https://github.com/FluidSynth/fluidsynth/releases/latest)~~ - MIDI to WAV

## Author

[Firebladedoge229](https://www.github.com/Firebladedoge229) - Creator

## Credits 

[SoftIcons](https://www.softicons.com/system-icons/toyfactory-icons-by-mira/file-midi-icon) - MIDI Icon
