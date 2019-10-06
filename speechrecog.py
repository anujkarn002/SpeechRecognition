import json
import constants
import azure.cognitiveservices.speech as speechsdk


class SpeechRecognizer:
    def __init__(self, key, region):
        self.speech_key, self.service_region = key, region
        self.speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    def recognize(self):
        result = self.speech_recognizer.recognize_once()
        # Checks result.
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
            return False
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
            return False


ear = SpeechRecognizer(constants.KEY, constants.REGION)
import time
while True:
    print('starting in 2 seconds')
    time.sleep(2)
    print('listening..')
    print(ear.recognize())
    print('stopped')