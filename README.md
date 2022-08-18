# retico

Retico is an open-source framework for building state-of-the-art incremental processing
systems. This python package contains the functionality of the major supported retico
modules and makes them easily accessible.

## Example

```python
from retico import *
from retico.modules import *


def callback(update_msg):
    for x, ut in update_msg:
        print(f"{ut}: {x.text} ({x.stability}) - {x.final}")


m1 = MicrophoneModule()
m2 = Wav2VecModule()
m3 = TextDispatcherModule()
m4 = GoogleTTSModule("en-US", "en-US-Wavenet-A")
m5 = SpeakerModule()
m6 = CallbackModule(callback)

m1.subscribe(m2)
m2.subscribe(m3)
m3.subscribe(m4)
m4.subscribe(m5)
m2.subscribe(m6)

run(m1)

input()

stop(m1)
```