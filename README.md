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

## Available Modules

---

### [retico-core](https://github.com/retico-team/retico-core)
- [abstract](https://github.com/retico-team/retico-core/blob/main/retico_core/abstract.py)
  - AbstractModule
    - An abstract module that is able to incrementally process data.
  - AbstractProducingModule
    - An abstract producing module that is able to incrementally process data. The producing module has no input queue and thus does not wait for any input. The producing module is called continuously and may return new output when it becomes available.
  - AbstractConsumingModule
    - An abstract consuming module that is able to incrementally process data. The consuming module consumes IUs but does not return any data.
  - AbstractTriggerModule
    - An abstract trigger module that produces an update message once a trigger method is called. Unless the module is triggered no updates are produced.
- [audio](https://github.com/retico-team/retico-core/blob/main/retico_core/audio.py)
  - MicrophoneModule
    - A producing module that records audio from microphone.
  - SpeakerModule
    - A consuming module that plays audio from speakers.
  - StreamingSpeakerModule
    - A consuming module that streams audio from speakers.
  - AudioDispatcherModule
    - A module that transmits audio by splitting it up into streamable packets.
  - AudioRecorderModule
    - A module that saves incoming audio to disk.
- [await_contingent_iu](https://github.com/retico-team/retico-core/blob/main/retico_core/await_contingent_iu.py)
  - AwaitContingentIUsModule
    - Wait for all required IUs to arrive before proceeding.
- [debug](https://github.com/retico-team/retico-core/blob/main/retico_core/debug.py)
  - DebugModule
    - A consuming module that displays IU infos in the console.
  - CallbackModule
    - A consuming module that calls a callback function whenever an update message arrives.
  - TextPrinterModule
    - A debug module that prints the incoming text and updates it as text IUs are arriving. Once an IU is committed, the next incoming text is printed in a new line.
- [dialogue](https://github.com/retico-team/retico-core/blob/main/retico_core/dialogue.py)
  - DialogueActRecorderModule
    - A module that writes dialogue acts into a file.
  - DialogueActTriggerModule
    - A trigger module that emits a dialogue act when triggered.
- [text](https://github.com/retico-team/retico-core/blob/main/retico_core/text.py)
  - TextRecorderModule
    - A module that writes received TextIUs to file.
  - TextTriggerModule
    - A trigger module that creates a TextIU once it is triggered.
  - TextDispatcherModule
    - A module that uses SpeechRecognitionIUs and outputs dispatchable IUs.
  - IncrementalizeASRModule
    - A module that takes SpeechRecognitionIUs and emits only the increments from the previous IU.
  - EndOfUtteranceModule
    - A module that forwards the end of utterance from the ASR output.

---

### [retico-alfred](https://github.com/retico-team/retico-alfred)
- [AlfredModule](https://github.com/retico-team/retico-alfred/blob/main/retico_alfred/retico_alfred.py)
  - An interfacing module for the ALFRED benchmark, allowing real-time human annotations.

---

### [retico-chatgpt](https://github.com/retico-team/retico-chatgpt)
- [ChatGPTDialogueModule](https://github.com/retico-team/retico-chatgpt/blob/main/retico_chatgpt/chatgpt.py)
  - ChatGPT dialogue module that uses the OpenAI API to generate responses to user input.

---

### [retico-clip](https://github.com/retico-team/retico-clip)
- [ClipObjectFeatures](https://github.com/retico-team/retico-clip/blob/main/retico_clip/clip.py)
  - A module for extracting visual features from images.

---

### [retico-CLIP-zeroShot](https://github.com/retico-team/retico-CLIP-zeroShot)
- [debug_modules](https://github.com/retico-team/retico-CLIP-zeroShot/blob/main/retico_CLIP_zeroShot/debug_modules.py)
    - ObjectClassificationConsumer
      - Prints object classification results.
    - ClassificationConsumer
      - Prints classification results.
- [image_classification](https://github.com/retico-team/retico-CLIP-zeroShot/blob/main/retico_CLIP_zeroShot/image_classification.py)
    - CLIPImageClassificationModule
      - A module that performs zero-shot image classification using CLIP.
- [object_classification](https://github.com/retico-team/retico-CLIP-zeroShot/blob/main/retico_CLIP_zeroShot/object_classification.py)
    - CLIPObjectClassificationModule
      - A module that performs zero-shot classification of detected objects using CLIP.

---

### [retico-coppelia](https://github.com/retico-team/retico-coppelia)
- [coppelia](https://github.com/retico-team/retico-coppelia/blob/main/retico_coppelia/coppelia.py)
    - CoppeliaModule
      - A controller module for CoppeliaSim
- [coppelia_camera](https://github.com/retico-team/retico-coppelia/blob/main/retico_coppelia/coppelia_camera.py)
    - CoppeliaCameraModule
      - A camera module for CoppeliaSim that produces virtual images.
- [coppelia_cozmo](https://github.com/retico-team/retico-coppelia/blob/main/retico_coppelia/coppelia_cozmo.py)
    - CoppeliaCozmoModule
      - A module for controlling a Cozmo robot inside a CoppeliaSim scene.
- [coppelia_cozmo_state](https://github.com/retico-team/retico-coppelia/blob/main/retico_coppelia/coppelia_cozmo_state.py)
    - CozmoStateModule
      - A module that tracks the state of a CoppeliaSim Cozmo robot.

---

### [retico-cozmoAgent](https://github.com/retico-team/retico-cozmoAgent)
- [CozmoSmolAgentsModule](https://github.com/retico-team/retico-cozmoAgent/blob/main/cozmoAgent/cozmoSmolAgents.py)
  - SmolAgents module for processing speech and generating robot commands.

---

### [retico-cozmorobot](https://github.com/retico-team/retico-cozmorobot)
- [cozmo_camera](https://github.com/retico-team/retico-cozmorobot/blob/main/retico_cozmorobot/cozmo_camera.py)
    - CozmoCameraModule
      - A module that tracks Cozmo camera frames.
- [cozmo_refer](https://github.com/retico-team/retico-cozmorobot/blob/main/retico_cozmorobot/cozmo_refer.py)
    - CozmoReferModule
      - A module that maps from DM decisions to Cozmo robot actions in a reference task.
- [cozmo_state](https://github.com/retico-team/retico-cozmorobot/blob/main/retico_cozmorobot/cozmo_state.py)
    - CozmoStateModule
      - A module that tracks the state of Cozmo, including camera frames.

---

### [retico-crisperasr](https://github.com/retico-team/retico-crisperasr)
- [CrisperASRModule](https://github.com/retico-team/retico-crisperasr/blob/main/retico_crisperasr/crisperasr.py)
  - A module that recognizes speech using CrisperWhisper.

---

### [retico-dino](https://github.com/retico-team/retico-dino)
- [retico_dino](https://github.com/retico-team/retico-dino/blob/main/retico_dino/dino.py)
    - Dinov2ObjectFeatures
      - Module for extracting visual features from images.
    - Dinov3ObjectFeatures
      - Module for extracting visual features from images with DINOv3.

---

### [retico-dopetrack](https://github.com/retico-team/retico-dopetrack)
- [DopeTrackingModule](https://github.com/retico-team/retico-dopetrack/blob/main/retico_dopetrack/dopetrack.py)
  - A pose tracking module using Distillation of Part Experts (DOPE).

---

### [retico-emro](https://github.com/retico-team/retico-emro)
- [action_formatter](https://github.com/retico-team/retico-emro/blob/main/retico_emro/action_formatter.py)
    - ActionExecutionModule
      - Execute GRED-generated actions on the robot.
- [emro_module](https://github.com/retico-team/retico-emro/blob/main/retico_emro/emro_module.py)
    - EMROActionClassifier
      - Classify robot actions into one of 6 EMRO emotion categories.

---

### [retico-facedetection](https://github.com/retico-team/retico-facedetection)
- [FaceDetectionModule](https://github.com/retico-team/retico-facedetection/blob/main/retico_facedetection/face-detect)
  - A module that detects faces in a photo.

---

### [retico-fer](https://github.com/retico-team/retico-fer)
- [fer_data_image_writer_module](https://github.com/retico-team/retico-fer/blob/master/retico_fer/fer_data_image_writer_module.py)
    - FERDataImageWriterModule
      - A module that writes FER data on its frame as an ImageIU.
- [fer_module](https://github.com/retico-team/retico-fer/blob/master/retico_fer/fer_module.py)
    - FERModule
      - A Facial Expression Recognition (FER) module that processes input IUs and outputs text IUs with emotion data.

---

### [retico-gemini](https://github.com/retico-team/retico-gemini)
- [GeminiModule](https://github.com/retico-team/retico-gemini/blob/main/retico_gemini/gemini.py)
  - Queries Gemini and streams response tokens.

---

### [retico-googleasr](https://github.com/retico-team/retico-googleasr)
- [GoogleASRModule](https://github.com/retico-team/retico-googleasr/blob/main/retico_googleasr/googleasr.py)
  - A module that incrementally recognizes speech.

---

### [retico-googletts](https://github.com/retico-team/retico-googletts)
- [GoogleTTSModule](https://github.com/retico-team/retico-googletts/blob/main/retico_googletts/googletts.py)
  - A module that uses Google TTS to synthesize audio.

---

### [retico-gred](https://github.com/retico-team/retico-gred)
- [GREDActionGenerator](https://github.com/retico-team/retico-gred/blob/main/retico_gred/gred_module.py)
  - Generate robot-behavior sequences from emotion labels.

---

### [retico-hftranslate](https://github.com/retico-team/retico-hftranslate)
- [HFTranslateModule](https://github.com/retico-team/retico-hftranslate/blob/main/retico_hftranslate/hftranslate.py)
  - A module that translates between languages using Hugging Face Transformers.

---

### [retico-huggingfacelm](https://github.com/retico-team/retico-huggingfacelm)
- [HuggingfaceLM](https://github.com/retico-team/retico-huggingfacelm/blob/main/retico_huggingfacelm/huggingface_lm.py)
  - A module running Hugging Face language model for real-time dialogue.

---

### [retico-keyboard](https://github.com/retico-team/retico-keyboard)
- [KeyboardModule](https://github.com/retico-team/retico-keyboard/blob/main/retico_keyboard/keyboard.py)
  - A module that produces IUs from keyboard input.

---

### [retico-language-detection](https://github.com/retico-team/retico-language-detection)
- [LanguageDetectionModule](https://github.com/retico-team/retico-language-detection/blob/main/retico_language_detection/language_detection.py)
  - A module that detects the language of a raw audio or text.

---

### [retico-maai](https://github.com/retico-team/retico-maai)
- [MaAI](https://github.com/retico-team/retico-maai/blob/main/retico_maai/MaAI.py)
    - TurnTakingModule
      - Turn-taking module for MaAI turn-taking models.
    - BackchannelModule
      - Backchannel module for MaAI models.
    - NodPredictionModule
      - Nod prediction module for MaAI models.

---

### [retico-mistyrobot](https://github.com/retico-team/retico-mistyrobot)
- [retico_misty_camera_stream/retico_misty_camera_stream](https://github.com/retico-team/retico-mistyrobot/blob/main/retico_mistyrobot/retico_misty_camera_stream/retico_misty_camera_stream/misty_camera_stream_module.py)
    - MistyCameraStreamModule
      - A module that tracks the Misty II robot camera.
- [misty_action](https://github.com/retico-team/retico-mistyrobot/blob/main/retico_mistyrobot/misty_action.py)
    - MistyActionModule
      - A module that maps from DM decisions to Misty II robot actions.
- [misty_camera](https://github.com/retico-team/retico-mistyrobot/blob/main/retico_mistyrobot/misty_camera.py)
    - MistyCameraModule
      - A module that tracks the Misty II robot camera.
- [misty_camera_video](https://github.com/retico-team/retico-mistyrobot/blob/main/retico_mistyrobot/misty_camera_video.py)
    - MistyCameraVideoModule
      - A module that tracks the Misty II robot camera as video feed.
- [misty_refer](https://github.com/retico-team/retico-mistyrobot/blob/main/retico_mistyrobot/misty_refer.py)
    - MistyReferModule
      - A module that maps from DM decisions to Misty II robot actions for a simple reference task.
- [misty_state](https://github.com/retico-team/retico-mistyrobot/blob/main/retico_mistyrobot/misty_state.py)
    - MistyStateModule
      - A module that tracks the Misty II robot states.

---

### [retico-modelscope](https://github.com/retico-team/retico-modelscope)
- [ChatbotModule](https://github.com/retico-team/retico-modelscope/blob/main/retico_modelscope/chatbot.py)
  - A chatbot module using modelscope.

---

### [retico-multilingual-tts](https://github.com/retico-team/retico-multilingual-tts)
- [MultilingualTTSModule](https://github.com/retico-team/retico-multilingual-tts/blob/main/retico_multilingual_tts/multilingual_tts.py)
  - A module that synthesizes speech in various languages using Coqui.

---

### [retico-object-permanence](https://github.com/retico-team/retico-object-permanence)
- [CozmoObjectPermanenceModule](https://github.com/retico-team/retico-object-permanence/blob/main/retico_object_permanence/cozmo_object_permanence.py)
  - A module that tracks the pose information of objects viewed by Cozmo and manages them in Cozmo's memory map.

---

### [retico-objectFeatures](https://github.com/retico-team/retico-objectFeatures)
- [ObjectFeaturesExtractor](https://github.com/retico-team/retico-objectFeatures/blob/main/retico_objectFeatures/objects_feat_extr.py)
  - Module for extracting visual features from images.
---

### [retico-opendialdm](https://github.com/retico-team/retico-opendialdm)
- [OpenDialModule](https://github.com/retico-team/retico-opendialdm/blob/main/retico_opendialdm/dm.py)
  - A module providing dialogue management provided by OpenDial.

---

### [retico-rasanlu](https://github.com/retico-team/retico-rasanlu)
- [RasaNLUModule](https://github.com/retico-team/retico-rasanlu/blob/main/retico_rasanlu/rasanlu.py)
  - A module providing natural language understanding by rasa_nlu.

---

### [retico-respeakermic](https://github.com/retico-team/retico-respeakermic)
- [RespeakerMicrophoneModule](https://github.com/retico-team/retico-respeakermic/blob/main/retico_respeakermic/respeaker.py)
  - A producing module that records audio from a seed respeaker microphone array.

---

### [retico-robot-filter](https://github.com/retico-team/retico-robot-filter)
- [filter](https://github.com/retico-team/retico-robot-filter/blob/main/retico_robot_filter/filter.py)
    - RobotASRFilterModule
      - A module that filters out text generated by an NLG component.
- [misty_filter](https://github.com/retico-team/retico-robot-filter/blob/main/retico_robot_filter/misty_filter.py)
    - MistyRobotASRFilterModule
      - A module that filters out utterances from the Misty robot when taking voice input.

---

### [retico-rosbridge](https://github.com/retico-team/retico-rosbridge)
- [retico_ros2/joint_angles_to_text](https://github.com/retico-team/retico-rosbridge/blob/main/retico_ros2/joint_angles_to_text.py)
    - JointAnglesToTextModule
      - A module that generates joint angles from text command.
- [retico_ros2/ros2_publisher](https://github.com/retico-team/retico-rosbridge/blob/main/retico_ros2/ros2_publisher.py)
    - ROS2PublisherModule
      - A module providing publisher to a ROS2 topic.
- [retico_ros2/ros2_subscriber](https://github.com/retico-team/retico-rosbridge/blob/main/retico_ros2/ros2_subscriber.py)
    - ROS2SubscriberModule
      - A module providing reading from a ROS2 topic.
- [retico_ros2/text_to_joint_angles](https://github.com/retico-team/retico-rosbridge/blob/main/retico_ros2/text_to_joint_angles.py)
    - TextToJointAnglesModule
      - A module that generates joint angles from text command.
- [retico_textinput/textinput](https://github.com/retico-team/retico-rosbridge/blob/main/retico_textinput/textinput.py)
    - TextInput
      - A producing module that receives input text from keyboard.
- [retico_textoutput/textoutput](https://github.com/retico-team/retico-rosbridge/blob/main/retico_textoutput/textoutput.py)
    - TextOutputModule
      - A module that receives text and prints it in the console.

---

### [retico-rtdetr](https://github.com/retico-team/retico-rtdetr)
- [RTDETR](https://github.com/retico-team/retico-rtdetr/blob/main/retico_rtdetr/rtdetr.py)
  - An object detection module using RT-DETR.

---

### [retico-sam](https://github.com/retico-team/retico-sam)
- [hfsam](https://github.com/retico-team/retico-sam/blob/main/retico_sam/hfsam.py)
  - SAMModule
    - An object detection module using SAM.
- [sam](https://github.com/retico-team/retico-sam/blob/main/retico_sam/sam.py)
  - SAMModule
    - An object detection module using SAM.

---

### [retico-sceneGraph](https://github.com/retico-team/retico-sceneGraph)
- [graph_memory](https://github.com/retico-team/retico-sceneGraph/blob/main/retico_sceneGraph/graph_memory.py)
    - SceneGraphMemory
      - A module for managing the memory of a scene graph and the RAG system. It embeds triplets in the scene graph and provides access to the embeddings.
- [scene_graph](https://github.com/retico-team/retico-sceneGraph/blob/main/retico_sceneGraph/scene_graph.py)
    - SceneGraphModule
      - A Retico module for scene graph generation from images. It processes images to extract objects, their relationships, and generates a scene graph.
    - SceneGraphDrawingModule
      - A Retico module for drawing scene graphs onto images. It takes SceneGraphUnit as input and outputs an ImageIU with the drawn scene graph.

---

### [retico-simplelogger](https://github.com/retico-team/retico-simplelogger)
- [SimpleLoggerModule](https://github.com/retico-team/retico-simplelogger/blob/main/retico_simplelogger/simplelogger.py)
  - Logs incoming IUs as JSON.

---

### [retico-smolAgent](https://github.com/retico-team/retico-smolAgent)
- [SmolAgentsModule](https://github.com/retico-team/retico-smolAgent/blob/main/smolAgent/smolAgents.py)
  - SmolAgents module for conversational using CodeAgent.

---

### [retico-speakerdiarization](https://github.com/retico-team/retico-speakerdiarization)
- [speaker_diarization](https://github.com/retico-team/retico-speakerdiarization/blob/main/retico_speakerdiarization/speaker_diarization.py)
    - SpeakerDiarizationModule
      - A module that recognizes speakers in audio input.
- [utterance](https://github.com/retico-team/retico-speakerdiarization/blob/main/retico_speakerdiarization/utterance.py)
    - UtteranceModule
      - A module that connects text to its speaker.

---

### [retico-speechbraintts](https://github.com/retico-team/retico-speechbraintts)
- [SpeechBrainTTSModule](https://github.com/retico-team/retico-speechbraintts/blob/main/retico_speechbraintts/speechbraintts.py)
  - A module that synthesizes speech using SpeechBrain.

---

### [retico-tracking](https://github.com/retico-team/retico-tracking)
- [retico_handtrack/handtrack](https://github.com/retico-team/retico-tracking/blob/main/retico_handtrack/handtrack.py)
    - HandTrackingModule
      - A module for hand tracking using Google MediaPipe hand tracking library.
- [retico_posetrack/posetrack](https://github.com/retico-team/retico-tracking/blob/main/retico_posetrack/posetrack.py)
    - PoseTrackingModule
      - A pose tracking module using Google MediaPipe pose tracking library.

---

### [retico-vision](https://github.com/retico-team/retico-vision)
- [vision](https://github.com/retico-team/retico-vision/blob/main/retico_vision/vision.py)
    - WebcamModule
      - A producing module that records images from a web camera.
    - VideoPlaybackModule
      - A producing module that plays back video files frame by frame.
    - IPCameraModule
      - A producing module that captures images from IP camera feeds.
    - ImageCropperModule
      - A module that crops images.
    - ExtractedObjectsModule
      - A module that produces images of individual objects from segmentations produced by SAM or Yolo.
    - ScreenModule
      - A module that displays images on the screen.
    - Convert_DetectedObjectsIU_ImageIU
      - Converts DetectedObjectsIU to ImageIU for display.

---

### [retico-wacnlu](https://github.com/retico-team/retico-wacnlu)
- [WordsAsClassifiersModule](https://github.com/retico-team/retico-wacnlu/blob/main/retico_wacnlu/words_as_classifiers.py)
  - WAC Visually-Grounded Model

---

### [retico-wav2vecasr](https://github.com/retico-team/retico-wav2vecasr)
- [Wav2VecASRModule](https://github.com/retico-team/retico-wav2vecasr/blob/main/retico_wav2vecasr/wav2vecasr.py)
  - A module that recognizes speech using Wav2Vec.

---

### [retico-whisperasr](https://github.com/retico-team/retico-whisperasr)
- [WhisperASRModule](https://github.com/retico-team/retico-whisperasr/blob/main/retico_whisperasr/whisperasr.py)
  - A module that recognizes speech using Whisper.

---

### [retico-yolo](https://github.com/retico-team/retico-yolo)
- [ObjectDetectionModule](https://github.com/retico-team/retico-yolo/blob/main/retico_yolo/yolo.py)
  - An object detection module using YOLO.

---

### [retico-yolov11](https://github.com/retico-team/retico-yolov11)
- [Yolov11](https://github.com/retico-team/retico-yolov11/blob/main/retico_yolov11/yolov11.py)
  - An object detection module using YOLOv11.

---

### [retico-yolov8](https://github.com/retico-team/retico-yolov8)
- [Yolov8](https://github.com/retico-team/retico-yolov8/blob/main/retico_yolov8/yolov8.py)
  - An object detection module using YOLOv8.

---

### [retico-zmq](https://github.com/retico-team/retico-zmq)
- [zmq](https://github.com/retico-team/retico-zmq/blob/main/retico_zmq/zmq.py)
    - ReaderSingleton
      - A module providing reading from a ZeroMQ bus. Kept for backwards compatibility.
    - ZMQReaderModule
      - A module providing reading from a ZeroMQ bus. Supports ZMQ objects.
    - WriterSingleton
      - A module providing writing onto a ZeroMQ bus. Allows messages as JSON.
